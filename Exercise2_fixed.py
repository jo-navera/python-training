# Run this exercise with the following command:
# python Exercise2.py --file "recordsad.txt"
# Modify the code to validate the records in the file and print an error message for any invalid records.
# The error message should indicate which row the error occurred in and what the error is.
# The code should also print a message for valid records.
# Expected output with the above command:
# Line 1 is valid!
# ID: 001
# Last Name: Smith
# First Name: Johnson
# Birthdate: 19821115
# Role: Developer
# Error on Line 2: Invalid ID: 0x2
# Error on Line 3: Invalid Birthdate:  1995040
# Error on Line 4: Invalid Birthdate:  1988061
# Line 5 is valid!
# ID: 005
# Last Name: Jones
# First Name: David
# Birthdate: 19920211
# Role: Designer
# Error on Line 6: Role cannot be empty.
# Line 7 is valid!
# ID: 007
# Last Name: Rodriguez
# First Name: Thomas
# Birthdate: 19960830
# Role: Manager
# Line 8 is valid!
# ID: 008
# Last Name: Lee
# First Name: Jennifer
# Birthdate: 19791203
# Role: Analyst
# Line 9 is valid!
# ID: 009
# Last Name: Taylor
# First Name: Christopher
# Birthdate: 19850422
# Role: Technician
# Line 10 is valid!
# ID: 010
# Last Name: Anderson
# First Name: Sarah
# Birthdate: 19910918
# Role: Designer


from pathlib import Path
import argparse


class PersonRecord:
    def __init__(self, id, last_name, first_name, birthdate, role, hiredate, lastdate):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.role = role
        self.hiredate = hiredate
        self.lastdate = lastdate

    def __repr__(self):
        return (
            f"PersonRecord("
            f"id={self.id}, "
            f"last_name='{self.last_name}', "
            f"first_name='{self.first_name}', "
            f"birthdate={self.birthdate}, "
            f"role='{self.role}', "
            f"hiredate={self.hiredate},
            f"lastdate={self.lastdate}"
        )


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
        role=line[52:62]
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
