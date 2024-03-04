from pathlib import Path

file_path = Path('path/to/file.txt')

#check if the file exists
if file_path.exists():
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
