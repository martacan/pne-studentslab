import http.client
import json
from e2 import genes
from P01.Seq1 import Seq

SERVER = "rest.ensembl.org"
conn = http.client.HTTPSConnection(SERVER)

for gene_name in genes:

    gene_id = genes[gene_name]

    ENDPOINT = "/sequence/id/" + gene_id
    PARAMS = ("?content-type=application/json")
    URL = SERVER + ENDPOINT + PARAMS

    print(f"Server: {SERVER}")
    print(f"URL: {URL}")


    conn.request("GET", ENDPOINT + PARAMS)

    r = conn.getresponse()
    print(f"Response received: {r.status} {r.reason}")

    data = r.read().decode("utf-8")
    response = json.loads(data)

    print(f"\nGene: {gene_name}")
    print(f"Description: {response["desc"]}")

    sequence = response["seq"]
    s = Seq(sequence)


    lenght = s.len()
    print(f"Total length {lenght}")


    perc_a = round((s.count_base("A") / lenght) * 100, 2)
    perc_c = round((s.count_base("C") / lenght) * 100, 2)
    perc_g = round((s.count_base("G") / lenght) * 100, 2)
    perc_t = round((s.count_base("T") / lenght) * 100, 2)

    print(f"A: {s.count_base("A")} ({perc_a}%)")
    print(f"C: {s.count_base("C")} ({perc_c}%)")
    print(f"G: {s.count_base("G")} ({perc_g}%)")
    print(f"T: {s.count_base("T")} ({perc_t}%)")

    print(f"Most frequent base: {s.most_frequent_base()}")