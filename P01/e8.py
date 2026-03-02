from Seq1 import Seq
print("----|Practise 1, Exercise 8|-----")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid Sequence")
print(f"""
Sequence 0: (length: {s1.len()}) {s1} 
Bases: {s1.count()}
Rev: {s1.reverse()}
Comp: {s1.complement()}""")
print(f"""
Sequence 1: (length: {s2.len()}) {s2} 
Bases: {s2.count()}
Rev: {s2.reverse()}
Comp: {s2.complement()}""")
print(f"""
Sequence 2: (length: {s3.len()}) {s3} 
Bases: {s3.count()}
Rev: {s3.reverse()}
Comp: {s3.complement()}""")
