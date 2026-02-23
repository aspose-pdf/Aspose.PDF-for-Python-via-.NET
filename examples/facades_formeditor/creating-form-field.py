from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Creating Form Fields
# AddField
# AddSubmitBtn
def create_form_fields(infile, outfile):
    """Create form fields in PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form.add_field(ap.facades.FormFieldType.Text, "textbox1", "Text Box 1", 100, 700, 200, 720)

    # Add CheckBox field to PDF form
    pdf_form.add_field(ap.facades.FormFieldType.CheckBox, "checkbox1", "Check Box 1", 100, 650, 120, 670)

    # Add RadioButton field to PDF form
    pdf_form.add_field(ap.facades.FormFieldType.RadioButton, "radiobutton1", "Radio Button 1", 100, 600, 120, 620)

    # Add ComboBox field to PDF form
    pdf_form.add_field(ap.facades.FormFieldType.ComboBox, "combobox1", "Combo Box 1", 100, 550, 200, 570)

    # Add ListBox field to PDF form
    pdf_form.add_field(ap.facades.FormFieldType.ListBox, "listbox1", "List Box 1", 100, 500, 200, 520)

    # Add Submit Button to PDF form
    pdf_form.add_submit_btn("submitbtn1", "Submit Button", "http://example.com/submit")

    # Save updated PDF document with form fields
    pdf_form.save(outfile)