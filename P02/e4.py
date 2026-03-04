from pathlib import Path
from Client0 import Client
from Seq1 import Seq


print(f"-----| Practice 2, Exercise 4 |------")

IP = "212.128.255.80"
PORT = 8080
c = Client(IP, PORT)
print(c)
c.__str__()
folder = "../P01/"
genes = ["U5", "FRAT1", "ADA"]
s = Seq()
for gene in genes:
    print(f"\nSending the {gene} gene to the server")
    s.read_fasta(folder + gene + ".txt")
    print(f"From Server:")
    response = c.talk(s.__str__())
    print(f"To server: {s.__str__()}")
    print(f"Response: {response}\n")