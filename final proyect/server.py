import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as template
from urllib.parse import parse_qs, urlparse
import http.client
import json

PORT = 8080
SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        status = 200

        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        contents = ""

        #PART 1-
        if path == "/":
            contents = Path('index.html').read_text()

        elif path == "/listSpecies":
            try:
                ENDPOINT = "/info/species"
                limit_str = arguments.get("limit", [""])[0]

                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                response = conn.getresponse()
                data = response.read().decode()
                d = json.loads(data)

                species_list = d["species"]


                if "limit" not in arguments or not limit_str or "":
                    limit = None
                    filtered_species = species_list

                else:
                    try:
                        limit = int(limit_str)

                        if  not 0 < limit <= len(species_list):
                            raise ValueError
                        filtered_species = species_list[:limit]


                    except ValueError:
                        self.send_error(400, "Error:Please enter a number")


                species_names = ""

                for species in filtered_species:
                    if "common_name" in species:
                        species_names += "<li>" + (species["common_name"]) + "</li>"
                    else:
                        species_names += "<li>" + (species.get("name", "Unknown")) + "</li>"


                # 3. Cargar template y renderizar
                template_loader = template.FileSystemLoader("html")
                template_env = template.Environment(loader=template_loader)
                template_obj = template_env.get_template("listSpecies.html")
                contents = template_obj.render(
                    context={
                        "limit": limit,
                        "names" : species_names,
                        "length": len(species_list)
                    }
                )
            except:
                status = 404
                contents = Path('error.html').read_text()


        elif path == "/karyotype":
            try:
                species = arguments.get("species", [""])[0]
                ENDPOINT = f"/info/assembly/:{species}"

                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                response = conn.getresponse()
                data = response.read().decode()
                d = json.loads(data)

                karyotype = d["karyotype"]

                chromosomes_name = ""

                for chromo in karyotype:
                    chromosomes_name += "<li>" + (chromo["name"]) + "</li>"

                template_loader = template.FileSystemLoader("html")
                template_env = template.Environment(loader=template_loader)
                template_obj = template_env.get_template("chromosomes.html")
                contents = template_obj.render(
                    context={
                        "name": chromosomes_name,
                    }
                )
            except Exception as e:
                print(e)
                status = 404
                contents = Path('error.html').read_text()


            # 4. Enviar respuesta
        self.send_response(status)
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
