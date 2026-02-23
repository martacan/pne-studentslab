from pathlib import Path
from Seq0 import seq_reverse

if __name__ == "__main__":
    print("----| Exercise 6 |----")
    file_path = Path("sequences/U5.txt")
    gene_contents = file_path.read_text().replace("\n", "").strip()
    fragment = gene_contents[:20]
    reverse_fragment = seq_reverse(gene_contents, 20)
    print(f"Gene U5")
    print(f"Fragment: ´{fragment}")
    print(f"Reverse: ´{reverse_fragment}")
