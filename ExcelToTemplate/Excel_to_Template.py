#Feature 1: change saved filename to include rigname "rigname.docx"
#Feature 2: change process_paragraphs to replace placeholder text with the corresponding value from the datarow
#Feature 3: change process_tables to replace placeholder text with the corresponding value from the datarow
#Feature 4: change parse_arguments to accept command line arguments for source file and template file

import pandas as pd
import argparse
import docx
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


def parse_arguments():
    return "ExcelToTemplate\Source.xlsx", "ExcelToTemplate\Template - Copy.docx"


def checkedElement():
    elm = OxmlElement('w:checked')
    elm.set(qn('w:val'), "true")    
    return elm


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
    process_tables(datarow, template)
    handle_checkboxes(template)
    return template


def process_paragraphs(datarow, template):
    # Process the paragraphs in the template and fill them with the data from the datarow
    for paragraph in template.paragraphs:
        for key, value in datarow.items():
            paragraph.text = value
            
    return template


def process_tables(datarow, template):
    # Process the tables in the template and fill them with the data from the datarow
    for table in template.tables:
        for row in table.rows:
            for cell in row.cells:
                for key, value in datarow.items():
                   cell.text = value
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


def handle_checkboxes(template):
    doc = template

    legacy_boxes = doc._element.xpath('.//w:checkBox')
    for box in legacy_boxes:
        # Check if <w:checked> element already exists
        checked_el = box.find(qn('w:checked'))

        if checked_el is not None:
            checked_el.set(qn('w:val'), '1')  # '1' or 'true' means checked
        else:
            # Create and append a new <w:checked> tag if missing
            new_checked = docx.oxml.shared.OxmlElement('w:checked')
            new_checked.set(qn('w:val'), '1')
            box.append(new_checked)
    return template


if __name__ == "__main__":
    source_file, template_file = parse_arguments()
    loaded_df = load_spreadsheet(source_file)
    processed_data = arrange_data_for_processing(loaded_df)
    loaded_template = load_template(template_file)
    process_data(processed_data, loaded_template)
