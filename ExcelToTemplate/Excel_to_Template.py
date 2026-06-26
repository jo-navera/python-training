from cmath import nan

import pandas as pd
import argparse
from docx import Document


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", help="Name of the source file to load")
    parser.add_argument("--template", help="Name of the template file to load")
    args = parser.parse_args()
    return args.source, args.template


def get_spreadsheet_data(df):
    # Get the data from the DataFrame as a list of lists
    data = df.values.tolist()
    return data


def load_spreadsheet(file_path):
    # Load the spreadsheet into a pandas DataFrame
    df = pd.read_excel(file_path)
    return df


def load_template(file_path):
    # Load the template into a python-docx Document
    doc = Document(file_path)
    return doc


def arrange_data_for_processing(df):
    # Arrange the data from the DataFrame into a list of dictionaries
    data = df.to_dict(orient='records')
    return data


def process_data_row(datarow, template):
    # Process a single row of data and fill the template with the data
    process_paragraphs(datarow, template)
    process_bookmarks(datarow, template)
    process_tables(datarow, template)

    return template


def process_paragraphs(datarow, template):
    # Process the paragraphs in the template and fill them with the data from the datarow
    for paragraph in template.paragraphs:
        for key, value in datarow.items():
            if f"<<{key.upper()}>>" in paragraph.text:
                paragraph.text = paragraph.text.replace(
                    f"<<{key.upper()}>>", str(value))
    return template


def process_bookmarks(datarow, template):
    # Process the bookmarks in the template and fill them with the data from the datarow
    for bookmark in template:
        for key, value in datarow.items():
            if f"<<{key.upper()}>>" in bookmark.name:
                bookmark.text = str(value)
    return template


def process_tables(datarow, template):
    # Process the tables in the template and fill them with the data from the datarow
    for table in template.tables:
        for row in table.rows:
            for cell in row.cells:
                for key, value in datarow.items():
                    if f"<<{key.upper()}>>" in cell.text:
                        cell.text = cell.text.replace(
                            f"<<{key.upper()}>>", str(value))
    return template


def save_filled_template(template, output_file):
    # Save the filled template to a new file
    template.save(output_file)


def process_data(data, template):
    # Process all rows of data and fill the template with the data
    for i, datarow in enumerate(data):
        filled_template = process_data_row(datarow, template)
        output_file = f"filled_template_{i+1}.docx"
        save_filled_template(filled_template, output_file)
        print(f"Saved filled template to {output_file}")
        break


def test_process_tables():
    # Test the process_tables function with a sample datarow and template
    datarow = {
        'Rig Name': 'Noble BlackHawk', 'Run Robot': 'Yes', 'IMO Number': 9618898, 'Official Number': 5061, 'Company Name': 'Noble Drilling (U.S.) LLC', 'IMO Company Number': 3018270.0, 'ISM Code applicable': 'Yes', 'Company Registered Owner': 'Diamond Offshore Limited', 'MLC, 2006 Certification applicable': 'No', 'National Statement of Compliance being requested': 'No', 'RO for MLC': nan, 'RO for SMC': nan, 'DP or DPA': 'DPA', 'Name of Designated Person': 'Ann Bow', 'DP Daytime Telephone': '+1 346-209-2834', 'DP Nighttime Telephone': '+1 346-253-4584', 'DP 24Hr Telephone': '+1 346-253-4584', 'DP Email': 'dpa@testing.com', 'Alternate DP or DPA': 'Alternate DPA', 'Name of Alternate DP': 'Don Draper', 'Alternate DP Telephone': '+1 713-239-6320, +1 281-750-5351', 'Alternate DP Email': 'ddraper@testing.com', 'ISPS Code applicable': 'Yes', 'RO for ISSC': 'RMI', 'Name of CSO': 'TEST John Doe', 'CSO Daytime Telephone': '+1 123-456-789', 'CSO Nighttime Telephone': '+1 123-456-789', 'CSO 24Hr Telephone': '+1 123-456-789', 'CSO Email': 'jdtest@testing.com', 'Alternate CSO': 'jdtest@testing.com', 'Alternate CSO Telephone': '+1 123-456-789', 'Alternate CSO Email': 'alternateemail@testing.com', 'Name on Behalf of the Company': 'Jane Doe', 'Title on Behalf of the Company': 'Title on Behalf of the Company', 'IMO ISM Code Company Number': nan, 'RO for ISM Document': nan, 'Company Address1': nan, 'Company Address2': nan, 'Company Address3': nan, 'Company Telephone': nan, 'Company Email': nan, 'Company Registered Owner Title': nan, 'CSR Document Number': nan, 'Date Applied': NaT, 'Flag State': 'N/C', 'Date of Registration': 'N/C', 'Name of Ship': 'N/C', 'Port of Registration': 'N/C', 'Registered Owner Name': 'N/C', 'Registered Owner Address': 'N/C', 'IMO Registered Owner Number': 'N/C', 'Name of Registered Bareboat Charterer': nan, 'Registered Bareboat Charterer Address': nan, 'Company Name 203': nan, 'Company Address': nan, 'Company Safety Management Activity Address': nan, 'IMO Company No': 'N/C', 'RO for Vessel': 'N/C', 'Flag Name': 'N/C'}
    template = Document("ExcelToTemplate\RMI - Combined Declaration Form.docx")
    filled_template = process_tables(datarow, template)
    filled_template.save("test_filled_template.docx")
    print("Saved test filled template to test_filled_template.docx")


if __name__ == "__main__":
    source_file, template_file = "ExcelToTemplate\RMI - Rig Information - TEST.xlsx", "ExcelToTemplate\RMI - Combined Declaration Form.docx"  # parse_arguments()
    loaded_df = load_spreadsheet(source_file)
    processed_data = arrange_data_for_processing(loaded_df)
    loaded_template = load_template(template_file)
    process_data(processed_data, loaded_template)
