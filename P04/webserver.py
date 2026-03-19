from pathlib import Path
import socket

if __name__== "__main__":
    IP = "127.0.0.1"
    PORT = 8080

    def process_client(s):
        req_raw = s.recv(2000)
        req = req_raw.decode()

        if not req:
            return

        lines = req.split('\n')
        req_line = lines[0]

        parts = req_line.split(' ')

        path = parts[1]

        print("Request line: ", end="")

        if len(path) > 1:
            if path == "/info/A":
                FILENAME = "./html/info/A.html"

            elif path == "/info/C":
                FILENAME = "./html/info/C.html"
            elif path == "/info/G":
                FILENAME = "./html/info/G.html"
            elif path == "/info/T":
                FILENAME = "./html/info/T.html"

            else:
                FILENAME = "./html/info/error.html"
        else:
            if path == "/":
                FILENAME = "./html/info/index.html"

        b = Path(FILENAME).read_text()


        body = b
        status_line = "HTTP/1.1 200 OK\n"


        header = "Content-Type: text/html\r\n"
        header += f"Content-Length: {len(body.encode('utf-8'))}\r\n"

        response_msg = status_line + header + "\n" + body
        s.send(response_msg.encode())


    ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ls.bind((IP, PORT))
    ls.listen()

    print(f"Server configured on {IP}:{PORT}!")

    while True:
        try:
            (cs, client_ip_port) = ls.accept()
            process_client(cs)
            cs.close()
        except KeyboardInterrupt:
            print("\nServer stopped!")
            ls.close()
            break