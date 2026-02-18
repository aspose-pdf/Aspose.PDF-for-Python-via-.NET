import sys
import os
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir

def add_field(infile, outfile):
    # Create an instance of FormEditor to manipulate form fields
    editor = pdf_facades.FormEditor()

    # Bind PDF document
    editor.bind_pdf(infile)

    # Add a text field named "Country" to the first page of the PDF
    # Coordinates: left, bottom, right, top
    editor.add_field(
        pdf_facades.FieldType.Text,
        "Country",
        1,
        232.56, 496.75, 352.28, 514.03
    )

    # Set a character limit for the "Country" field to 20 characters
    editor.set_field_limit("Country", 20)

    # Save modified PDF document
    editor.save(outfile)


def add_submit_button(infile, outfile):
    # Create an instance of FormEditor to manipulate form fields
    editor = pdf_facades.FormEditor()

    # Bind PDF document
    editor.bind_pdf(infile)

    # Add a submit button named "Submit" to the first page of the PDF
    # Parameters: field name, page number, button text, submit URL, coordinates (left, bottom, right, top)
    editor.add_submit_btn(
        "Submit",
        1,
        "Submit",
        "http://localhost:3000",
        232.56, 466.75, 352.28, 484.03
    )

    # Save modified PDF document
    editor.save(outfile)

    # Dispose resources
    editor.Dispose()

    print("Submit button added successfully to the PDF form.")

    # os.path.join(data_dir, "Sample-Form-01.pdf")
    # os.path.join(data_dir, "Sample-Form-01-mod.pdf")

def add_field_script():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of FormEditor to manipulate form fields
    editor = pdf_facades.FormEditor()

    # Bind PDF document
    editor.bind_pdf(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Add a JavaScript action to the field named "Last Name"
    # The script displays an alert box with the message "Only one last name"
    editor.add_field_script("Last Name", "app.alert(\"Only one last name\",3);")

    # Save modified PDF document
    editor.save(os.path.join(data_dir, "Sample-Form-01-mod.pdf"))