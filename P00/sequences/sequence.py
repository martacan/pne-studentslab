from pathlib import Path



FILENAME = "ADA.txt"

file_contents = Path(FILENAME).read_text()
lines = file_contents.split("\n")
body = lines[1:]
seq = "".join(body)
print(len(seq))
