# Run this exercise with the following command:
# python Exercise2.py --file "recordsad.txt"
# Modify the code to validate the records in the file and print an error message for any invalid records.
# The error message should indicate which row the error occurred in and what the error is.
# Expected output with the above command:
# Line 1: Invalid ID: 12A
# Adobo is not a fruit.
# Banana is a fruit.

from pathlib import Path
import argparse
from Models import PersonRecord


def main():
    file = parse_arguments()
    contents = load_file(file)
    content_list = contents.splitlines()
    line_number = 1
    for line in content_list:
        record = parse_line(line)
        error = validate_record(record)
        if error != "":
            print(f"Error on Line {line_number}: {error}")
        else:
            print(f"Line {line_number} is valid!")
            print_record(record)
        line_number += 1


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    args = parser.parse_args()
    return args.file


def load_file(file: str):
    script_dir = Path(__file__).parent
    file_name = file if file else 'records.txt'
    file_path = script_dir / file_name

    if not file_path.exists():
        raise FileNotFoundError("File does not exist.")

    with open(file_path, 'r') as file:
        content = file.read()
    return content


def print_record(record: PersonRecord):
    print(f"ID: {record.id}")
    print(f"Last Name: {record.last_name}")
    print(f"First Name: {record.first_name}")
    print(f"Birthdate: {record.birthdate}")
    print(f"Role: {record.role}")


def parse_line(line: str) -> PersonRecord:
    return PersonRecord(
        id=line[0:3],
        last_name=line[3:23],
        first_name=line[23:43],
        birthdate=line[44:52],
        role=line[52:62]
    )


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
