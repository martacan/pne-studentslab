import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as template
from urllib.parse import parse_qs, urlparse

PORT = 8080
ENSEMBL_URL = "https://rest.ensembl.org"

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        #PART 1- PING METHOD
        if path == "/":
            contents = Path('index.html').read_text()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))


        elif path == "/listSpecies":

            limit_str = arguments.get("limit", ["100"])[0]
            limit = int(limit_str)


            url = f"{ENSEMBL_URL}/info/species?content-type=application/json"
            response = requests.get(url)
            data = response.json()

            # Slicing para limitar la lista (sin for)
            species_list = data["species"][:limit]

            # 3. Cargar template y renderizar
            template_loader = template.FileSystemLoader("html")
            template_env = template.Environment(loader=template_loader)
            template_obj = template_env.get_template("listSpecies.html")
        
            contents = template_obj.render(species=species_list)

            # 4. Enviar respuesta
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))

        #PART 2- GET METHOD
        elif path == "/get":
            sequences = {
                "0": "AAGTCAACCUUCC",
                "1": "CCGTAAAACGT",
                "2": "TTUATCCGGGG",
                "3": "AGCCTAAACGAT",
                "4": "AGTTCCGATTACG"
            }

            #parse convierte la url en un diccionario [arguments] y esta [] porque podria haber multiples valores lista, el .get busca una clave y devuelve una lista por eso se usa [0[ acceder al primer elemtno lista
            seq_number = arguments.get("seq_number", ["0"])[0]


            #acceder al valor en el diccionario de sequences
            seq_value = sequences[seq_number]

            #render
            template_loader = template.FileSystemLoader("html")
            template_env = template.Environment(loader=template_loader)
            template_obj = template_env.get_template("get.html")
            contents = template_obj.render(seq_number=seq_number, seq_value=seq_value)

            self.send_response(200)  # -- Status line: OK!
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))


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
