import socket
from P01.Seq1 import Seq

PORT = 8080
IP= "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()

print(f"Seq Server configured!")

while True:
    print("Waiting for clients to connect...")
    (cs, client_ip_port) = ls.accept()

    msg_raw = cs.recv(2048)
    request = msg_raw.decode().strip()
    divided = request.split(" ", 1)
    if len(divided) == 2:
        info = divided[1]
        command = divided[0]


    if request == "PING":
        print("PING command!")
        response = "Ok\n"

        print(response.strip())
        cs.send(response.encode())

    elif command == "GET":

        print("GET command!")

        if info == "0":
            response = "AGGTTCCG"
        if info == "1":
            response = "TTAAGC"
        if info == "2":
            response = "TCCG"
        if info == "3":
            response = "AGAAAGT"
        if info == "4":
            response = "GGCCTTAAA"
        else:
            response = "INVALID NUMBER"
        print(response)
        cs.send(response.encode())










