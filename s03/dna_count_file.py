from dna_count import count_bases

#option 1
f = open("dna.txt", "r")
lines = f.readlines()

f.close()

#option 2
with open("dna.txt", "r") as f:
    lines = f.readlines()

#print("from file:", lines)
total_number = 0

bases = {"A": 0, "C": 0, "G": 0, "T": 0}

for sequence in lines:
    sequence = sequence.strip() # remove the spaces and newline characters at the end of the string
    total_number += len(sequence)

    result = count_bases(sequence)
    for key in result:
        bases[key] += result[key]





print("the total number of bases", total_number)
for base, count in bases.items():
    print(f"{base}: {count}")