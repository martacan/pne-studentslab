from pathlib import Path
from Seq0 import seq_len

if __name__ == "__main__":
    print("----| Exercise 3 |----")
    SEQUENCES = "sequences/"
    FILENAME = ["U5", "ADA", "FRAT1", "FXN"]
    for gene in FILENAME:
        file_name = gene + ".txt"
        file = Path(SEQUENCES + file_name).read_text()
        print(f"Gene {gene} --> lENGHT: {seq_len(file)}")

