

dna = "ATGCGATCGATCGATCGATCGA"
lenght = len(dna)
print("Lenght: ", lenght)
print("Fist 5", dna[:5])
print("Last 3", dna[19:])
print("Lowercase: ", dna.lower())
print("ATC count: ", dna.count("ATC"))
print("RNA: ", dna.replace("T", "U"))