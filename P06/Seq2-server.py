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


        elif path == "/gene":

            selected_gene = arguments.get("gene", [""])[0]

            filepath = Path(f"genes/{selected_gene}.txt")
            try:
                gene_sequence = filepath.read_text().strip()

                if "\n" in gene_sequence:
                    lines = gene_sequence.split("\n")
                    if lines[0].startswith(">"):
                        gene_sequence = "\n".join(lines[1:])


                template_loader = template.FileSystemLoader("html")
                template_env = template.Environment(loader=template_loader)
                template_obj = template_env.get_template("gene.html")
                contents = template_obj.render(gene_name=selected_gene, gene_sequence=gene_sequence)

                self.send_response(200)  # -- Status line: OK!
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(str.encode(contents)))
                self.end_headers()
                self.wfile.write(str.encode(contents))

            except FileNotFoundError:
                contents = Path('html/error.html').read_text()
                self.send_response(200)  # -- Status line: OK!
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(str.encode(contents)))
                self.end_headers()
                self.wfile.write(str.encode(contents))

        elif path == "/operation":
            sequence = arguments.get("sequence", [""])[0]
            operation = arguments.get("operation", [""])[0]

            seq_obj = Seq(sequence)

            if operation == "info":
                lenght = seq_obj.len()

                count_a = seq_obj.count_base("A")
                count_c = seq_obj.count_base("C")
                count_g = seq_obj.count_base("G")
                count_t = seq_obj.count_base("T")

                if lenght > 0:
                    perc_a = round((count_a / lenght) * 100, 2)
                    perc_c = round((count_c / lenght) * 100, 2)
                    perc_g = round((count_g / lenght) * 100, 2)
                    perc_t = round((count_t / lenght) * 100, 2)
                else:
                    perc_a = perc_c = perc_g = perc_t = 0

                result = f"""
-Total lenght: {lenght}<br>
-A: {count_a} ({perc_a}%)<br>
-C: {count_c} ({perc_c}%)<br>
-G: {count_g} ({perc_g}%)<br>
-T: {count_t} ({perc_t}%)"""

            elif operation == "comp":
                result = seq_obj.complement()
            elif operation == "rev":
                result = seq_obj.reverse()
            else:
                result = "Invalid Operation"

            template_loader = template.FileSystemLoader("html")
            template_env = template.Environment(loader=template_loader)
            template_obj = template_env.get_template("operation.html")
            contents = template_obj.render(sequence=sequence, operation=operation, result=result)

            self.send_response(200)  # -- Status line: OK!
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))

        else:
            contents = Path('html/error.html').read_text()
            self.send_response(200)  # -- Status line: OK!
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(contents)))
            self.end_headers()
            self.wfile.write(str.encode(contents))



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
