from pathlib import Path

from Seq0 import seq_read_fasta

if __name__ == "__main__":
    SEQUENCES = "sequences/"
    FILENAME = "U5.txt"
    print("Dna file:", FILENAME)
    file_contents = Path(SEQUENCES + FILENAME).read_text()
    print(f"The first 20 bases are: {seq_read_fasta(file_contents)[:20]}")


