from pathlib import Path
class Seq:
    def __init__(self, strbases=None):
        if strbases is None :
            self.strbases = "NULL"
            print("NULL sequence was created")
            return
        if all(base in "ACGT" for base in strbases):
            self.strbases = strbases
            print("New sequence was created")
        else:
            self.strbases = "ERROR"
            print("INVALID sequence!")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases in ["NULL", "ERROR"]:
            return 0
        return len(self.strbases)

    def count_base(self, base):
        if self.strbases in ["NULL", "ERROR"]:
            return 0
        return self.strbases.count(base)

    def count(self):
        if self.strbases in ["NULL", "ERROR"]:
            return {"A": 0, "T": 0, "G": 0, "C": 0}
        return {base: self.strbases.count(base) for base in "ATCG"}

    def reverse(self):
        if self.strbases in ["NULL", "ERROR"]:
            return self.strbases
        return self.strbases[::-1]

    def complement(self):
        if self.strbases in ["NULL", "ERROR"]:
            return self.strbases
        complement_bases = str.maketrans("ATGC", "TACG")
        return self.strbases.translate(complement_bases)

    def read_fasta(self, filename):
        file_path = Path(filename)
        if not file_path.exists():
            print(f"File{filename} does not exist")
            self.strbases = "ERROR"
            return
        file_content = file_path.read_text()
        lines = file_content.split("\n")
        self.strbases = "".join(lines[1:]).replace("\n", "")
        print("File loaded!")
    def most_frequent_base(self):
        if self.strbases in ["NULL", "ERROR"]:
            return "ERROR"
        base_counts = self.count()
        return max(base_counts, key=base_counts.get)


