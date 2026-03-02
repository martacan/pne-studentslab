from pathlib import Path
from Seq0 import *

if __name__ == "__main__":
    print("----| Exercise 5 |----")
    SEQUENCES = "sequences/"
    GENE_NAMES = ["U5", "ADA", "FRAT1", "FXN"]
    for gene in GENE_NAMES:
        file_name = gene + ".txt"
        file = Path(SEQUENCES + file_name).read_text()
        print(f"Gene {gene}: {seq_count(file)}")
