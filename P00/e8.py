from pathlib import Path
from Seq0 import most_frequent_base

if __name__ == "__main__":
    print("----| Exercise 8 |----")
    FOLDER = "sequences/"
    GENE_NAMES = ["U5", "ADA", "FRAT1", "FXN"]
    for gene in GENE_NAMES:
        file_name = gene + ".txt"
        file = Path(FOLDER + file_name).read_text()
        print(f"Gene {gene}: Most frequent base: {most_frequent_base(file)}")
