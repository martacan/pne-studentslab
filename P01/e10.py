from Seq1 import Seq
print("----|Practise 1, Exercise 10|-----")
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in genes:
    s = Seq()
    s.read_fasta(f"{gene}.txt")
    print(f"Gene {gene}: Most frequent base: {s.most_frequent_base()}")
