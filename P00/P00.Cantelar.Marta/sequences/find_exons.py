from pathlib import Path

FILENAME = "ADA.EXONS"

file_contents = Path(FILENAME).read_text()
print(file_contents)


