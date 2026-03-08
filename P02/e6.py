from Client0 import Client
from Seq1 import Seq

print(f"-----| Practice 2, Exercise 6 |------")

IP = "212.128.255.80"
PORT = 8080
PORT2 = 8081

c1 = Client(IP, PORT)
c2 = Client(IP, PORT2)
print(c1)
print(c2)

s = Seq()
s.read_fasta("../P01/FRAT1.txt")
full_sequence = str(s)
print(f"Gene FRAT1: {full_sequence[:70]}...")

fragment_size = 10

for i in range(10):
    start = i * fragment_size
    end = start + fragment_size
    fragment = full_sequence[start:end]
    num_fragment = i + 1

    print(f"Fragment {num_fragment}: {fragment}")

    if num_fragment % 2 != 0:
        response = c1.talk(fragment)
    else:
        response = c2.talk(fragment)

