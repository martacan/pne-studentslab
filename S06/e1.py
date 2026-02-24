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
            print("New sequence created!")
        else:
            self.str_bases = "ERROR"
            print("ERROR!!")

    def __str__(self):
        return self.str_bases



s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")

print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")