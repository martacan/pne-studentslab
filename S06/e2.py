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

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)