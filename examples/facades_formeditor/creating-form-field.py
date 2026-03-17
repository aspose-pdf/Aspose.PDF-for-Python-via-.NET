import sys
from os import path
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def create_checkbox_field(infile, outfile):
    """Create CheckBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add CheckBox field to PDF form
    pdf_form_editor.add_field(pdf_facades.FieldType.CHECK_BOX, "checkbox1", "Check Box 1", 1, 240, 498, 256, 514)
    
    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)

def create_combobox_field(infile, outfile):
    """Create ComboBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ComboBox field to PDF form
    pdf_form_editor.add_field(pdf_facades.FieldType.COMBO_BOX, "combobox1", "Australia", 1, 230, 498, 350, 514)
    pdf_form_editor.add_list_item("combobox1", ["Australia","Australia"])
    pdf_form_editor.add_list_item("combobox1", ["New Zealand","New Zealand"])

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)

def create_textbox_field(infile, outfile):
    """Create TextBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add TextBox field to PDF form
    pdf_form_editor.add_field(pdf_facades.FieldType.TEXT, "first_name", "Alexander", 1, 50, 570, 150, 590)
    pdf_form_editor.add_field(pdf_facades.FieldType.TEXT, "last_name", "Smith", 1, 235, 570, 330, 590)

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)

def create_radiobutton_field(infile, outfile):
    """Create RadioButton field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add RadioButton field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"];    
    pdf_form_editor.add_field(pdf_facades.FieldType.RADIO, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514)
    

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)

def create_listbox_field(infile, outfile):
    """Create ListBox field in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add ListBox field to PDF form
    pdf_form_editor.items = ["Australia", "New Zealand", "Malaysia"];
    pdf_form_editor.add_field(pdf_facades.FieldType.LIST_BOX, "listbox1", "Australia", 1, 230, 398, 350, 514)

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)

def create_submit_button(infile, outfile):
    """Create Submit Button in PDF document."""
    pdf_form_editor = pdf_facades.FormEditor()
    pdf_form_editor.bind_pdf(infile)

    # Add Submit Button to PDF form
    pdf_form_editor.add_submit_btn("submitbtn1", 1, "Submit Button", "http://example.com/submit", 100, 450, 200, 470)

    # Save updated PDF document with form fields
    pdf_form_editor.save(outfile)

def run_all_examples(data_dir=None, license_path=None):
    """Run all TextBox field examples with status reporting."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Create TextBox Field", create_textbox_field),
        ("Create CheckBox Field", create_checkbox_field),
        ("Create ComboBox Field", create_combobox_field),
        ("Create RadioButton Field", create_radiobutton_field),
        ("Create ListBox Field", create_listbox_field),
        ("Create Submit Button", create_submit_button),
    ]

    for name, func in examples:
        try:
            infile = path.join(input_dir, "sample_empty.pdf")
            outfile = path.join(output_dir, func.__name__ + ".pdf")
            func(infile, outfile)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()