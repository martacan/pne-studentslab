import http.client
import json
from e2 import genes
from P01.Seq1 import Seq


SERVER = "rest.ensembl.org"
gene_name = input(f"Write the gene: ").upper()
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

sequence = response["seq"]
print(f"New sequence created!")

lenght = len(sequence)
print(f"Total length {lenght}")

count_a = sequence.count("A")
count_c = sequence.count("C")
count_g = sequence.count("G")
count_t = sequence.count("T")

perc_a = round((count_a / lenght) * 100, 2)
perc_c = round((count_c / lenght) * 100, 2)
perc_g = round((count_g / lenght) * 100, 2)
perc_t = round((count_t / lenght) * 100, 2)

print(f"A: {count_a} ({perc_a}%)")
print(f"C: {count_c} ({perc_c}%)")
print(f"G: {count_g} ({perc_g}%)")
print(f"T: {count_t} ({perc_t}%)")

print(f"Most frequent base: ")