import pandas as pd
import argparse
import docx
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", help="Name of the source file to load")
    parser.add_argument("--template", help="Name of the template file to load")
    args = parser.parse_args()
    return args.source, args.template


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
            if f"<<{key.upper()}>>" in paragraph.text:
                paragraph.text = paragraph.text.replace(
                    f"<<{key.upper()}>>", str(value))
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


def handle_checkboxes(template):
    doc = template

    # 1. Handle Legacy Form Checkboxes (<w:checkBox>)
    # Find all legacy checkbox elements using XPath
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
    # source_file, template_file = parse_arguments()
    source_file, template_file = "ExcelToTemplate\Source.xlsx", "ExcelToTemplate\Template - Copy.docx"
    loaded_df = load_spreadsheet(source_file)
    processed_data = arrange_data_for_processing(loaded_df)
    loaded_template = load_template(template_file)
    process_data(processed_data, loaded_template)
