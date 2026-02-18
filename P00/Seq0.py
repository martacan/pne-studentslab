def seq_ping():
    print("OK")

from pathlib import Path

def seq_read_fasta(FILENAME):
    file_contents = Path(FILENAME).read_text()
    t = file_contents.find("\n")
    sequence = file_contents[t:].replace("\n", "")
    return sequence


