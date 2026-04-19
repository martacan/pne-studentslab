import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as template
from Seq1 import Seq
from urllib.parse import parse_qs, urlparse




PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        #PART 1- PING METHOD
        if path == "/":
            contents = Path('html/index.html').read_text()
            self.send_response(200)  # -- Status line: OK!
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))

        elif path == "/ping":
            contents = Path('html/ping.html').read_text()
            self.send_response(200)  # -- Status line: OK!
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))
        #PART 2- GET METHOD
        elif path == "/get":
            sequences = {
                "0": Seq("AAGTCAACCUUCC"),
                "1": Seq("CCGTAAAACGT"),
                "2": Seq("TTUATCCGGGG"),
                "3": Seq("AGCCTAAACGAT"),
                "4": Seq("AGTTCCGATTACG")
            }
            seq_number = arguments.get["seq_number"]
            contents = Path("html/get.html").read_text()




        else:
            contents = Path('html/error.html').read_text()



        self.send_response(200)  # -- Status line: OK!
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
