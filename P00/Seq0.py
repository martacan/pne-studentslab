from IPython.testing.tools import full_path

def seq_ping():
    print("OK")

from pathlib import Path
def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    d = file_contents.find("\n")
    sequence = file_contents[d:].replace("\n", "")
    return sequence


def seq_len(seq):
    body = seq.find("\n")
    seq = seq[body:]
    seq = seq.replace("\n", "")
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in seq:
        if base in bases:
            bases[base] += 1

    return bases

def seq_reverse(seq, n):
    body = seq.find("\n")
    seq = seq[body:]
    seq = seq.replace("\n", "")
    fragment = seq[:n]
    print(f"Fragment: {fragment}")
    reverse_fragment = fragment[::-1]

    return reverse_fragment









































































































































































































































































