from pathlib import Path
from Seq0 import seq_count_base

if __name__ == "__main__":
    print("----| Exercise 4 |----")
    FOLDER = "sequences/"
    FILENAME = ["U5", "ADA", "FRAT1", "FXN"]
    for gene in FILENAME:
        file_name = gene +".txt"
        file = Path(FOLDER + file_name).read_text()
        BASES = ["A", "C", "T", "G"]
        print(f"Gene {gene}:")
        for base in BASES:
            print(f"{base}: {seq_count_base(file, base)}")
