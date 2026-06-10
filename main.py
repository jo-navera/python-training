from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'records.txt'

if not file_path.exists():
    print("File does not exist.")
    print("Creating file...")

array = range(10)

with open(file_path, 'r') as file:
    content = file.read()
print(content)
