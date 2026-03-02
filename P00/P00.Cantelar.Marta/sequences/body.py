from pathlib import Path

FILENAME = "U5.txt"

file_contents = Path(FILENAME).read_text()
print("Body of the U5.txt file:")
lines = file_contents.split("\n")
for content in lines[1:]:
    print(content)

