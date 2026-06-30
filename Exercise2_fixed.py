#Feature 1 (Dex): Add new validation for hiredate. It should be numerical and it should be 8 characters long. If not, return an error message "Invalid Hiredate: {hiredate}".
#Feature 2 (Rachelle): Add new validation for lastdate. It should be numerical and it should be 8 characters long. If not, return an error message "Invalid Lastdate: {lastdate}".
#Feature 3 (Roselyn): Add new validation for birthdate. Only 18 years old and above should be valid.
#Feature 4 (Jayson): Add new validation to check last date should not be earlier than hire date.

from pathlib import Path
import argparse
from ObjectFolder.Objects import PersonRecord

def main():
    file = parse_arguments()
    contents = load_file(file)
    content_list = contents.splitlines()
    line_number = 1
    for line in content_list:
        process_line(line, line_number)
        line_number += 1

def func():
    return

def process_line(line: str, line_number: int):
    record = parse_line(line)
    error = validate_record(record)
    if error:
        print(f"Error on Line {line_number}: {error}")
    else:
        print(f"Line {line_number} is valid!")
        print_record(record)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    args = parser.parse_args()
    return args.file


def load_file(file: str):
    script_dir = Path(__file__).parent
    file_name = file if file else 'records.txt'
    file_path = script_dir / file_name

    with open(file_path, 'r') as file:
        content = file.read()
    return content


def print_record(record: PersonRecord):
    print(f"ID: {record.id}")
    print(f"Name: {record.first_name.strip()} {record.last_name.strip()}")
    print(f"Birthdate: {record.birthdate}")
    print(f"Role: {record.role}")


def parse_line(line: str) -> PersonRecord:
    person_object = PersonRecord(
        id=line[0:3],
        last_name=line[3:23],
        first_name=line[23:43],
        birthdate=line[44:52],
        role=line[52:62],
        hiredate=line[62:70],
        lastdate=line[70:78]    
    )
    return person_object


def validate_record(record: PersonRecord) -> str:
    error_message = ""
    if not record.id.isdigit():
        error_message = f"Invalid ID: {record.id}"
    if not record.birthdate.isdigit() or len(record.birthdate) != 8:
        error_message = f"Invalid Birthdate: {record.birthdate}"
    if not record.role:
        error_message = "Role cannot be empty."
    return error_message


if __name__ == "__main__":
    main()
