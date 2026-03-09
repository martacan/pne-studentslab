from Client0 import Client
from Seq1 import Seq


PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.80"
PORT = 8080

c = Client(IP, PORT)
print(c)

s = Seq()
s.read_fasta("../P01/FRAT1.txt")
full_sequence = str(s)

print(f"Gene FRAT1: {full_sequence[:76]}...")

for i in range(5):
    start = i * 10
    end = start + 10
    fragment = full_sequence[start:end]
    print(f"Fragment {i + 1}: {fragment}")
    response = c.talk(fragment)
