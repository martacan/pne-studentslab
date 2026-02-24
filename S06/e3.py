class Seq:
    def __init__(self, str_bases):
        valid_bases = "ACGT"
        is_valid = True

        for base in str_bases:
            if base not in valid_bases:
                is_valid = False
                break
        if is_valid:
            self.str_bases = str_bases
        else:
            self.str_bases = "ERROR"
            print("ERROR!!")

    def __str__(self):
        return self.str_bases


def print_seqs(seq_list):
    index = 0
    for i in seq_list:
        length = len(i.str_bases)
        print(f"Sequence {index}: (Length: {length}) {i}")
        index += 1


def generate_seqs(pattern, number):
    sequences = []
    count = 1

    while count <= number:
        repeated_pattern = pattern * count
        new_seq = Seq(repeated_pattern)
        sequences.append(new_seq)
        count = count + 1

    return sequences

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)
print()
print("List 2:")
print_seqs(seq_list2)