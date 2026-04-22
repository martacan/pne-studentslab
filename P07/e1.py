import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping" + gene_id
PARAMS = ("?content-type=application/json")
URL = SERVER + ENDPOINT + PARAMS

print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPSConnection(SERVER)
conn.request("GET", ENDPOINT + PARAMS)

response = conn.getresponse()
data = response.read().decode("utf-8")
response = json.loads(data)

print(f"Response received! {response}")
if response["ping"] == 1:
    print(f"PING1 OK! the database is running")