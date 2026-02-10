def lenght():
    n = input("please enter a dna sequence").upper()
    print("total length of the sequence is", len(n))
    a = 0
    c = 0
    g = 0
    t = 0
    for i in n:
        if i == "A":
            a += 1
        elif i == "G":
            g += 1
        elif i == "C":
            c += 1
        else:
            t += 1
    print("number of A bases", a)
    print("number of C bases", c)
    print("number of G bases", g)
    print("number of T bases", t)

lenght()

#sequence= input("introduce the dna seq)
#print the total len
# crear diccionario con las bases "A":0
#for bse in sequence:
# if base in bases:
#bases[base] += 1
# printear for base, count in bases.items():
#print(f{base}:{count}")

def count_bases(sequence):
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}

    for base in sequence:
        if base in sequence:
            bases[base]+=1
    return bases
if __name__ == "__main__":
    sequence = input("please enter a dna sequence").upper()
    print("total length of the sequence is", len(sequence))

    result = count_bases(sequence)
    for base, count in bases.items():
        print(f"{base}: {count}")

