import http.client
import json
from e2 import genes

SERVER = "rest.ensembl.org"
gene_name = "MIR633"
gene_id = genes[gene_name]

ENDPOINT = "/sequence/id/" + gene_id
PARAMS = ("?content-type=application/json")
URL = SERVER + ENDPOINT + PARAMS

print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)

r = conn.getresponse()
print(f"Response received: {r.status} {r.reason}")

data = r.read().decode("utf-8")
response = json.loads(data)

print(f"\nGene: {gene_name}")
print(f"Description: {response["desc"]}")
print(f"Bases: {response["seq"]}")