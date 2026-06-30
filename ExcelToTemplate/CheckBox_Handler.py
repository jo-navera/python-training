from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


def checkedElement():
    elm = OxmlElement('w:checked')
    elm.set(qn('w:val'), "true")
    return elm


template = Document("ExcelToTemplate\RMI - Combined Declaration Form.docx")
for table in template.tables:
    for row in table.rows:
        for cell in row.cells:
            checked = cell._element.xpath('.//w:checked')
            if checked:
                checked[0].set(qn('w:val'), "true")

template.save("RMI - Combined Declaration Form_checked.docx")
