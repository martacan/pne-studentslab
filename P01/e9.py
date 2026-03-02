# -- Create a Null sequence
from Seq1 import Seq
print("----|Practise 1, Exercise 9|-----")
s = Seq()
s.read_fasta("U5.txt")
print(f"""
Sequence : (length: {s.len()}) {s} 
Bases: {s.count()}
Rev: {s.reverse()}
Comp: {s.complement()}""")
