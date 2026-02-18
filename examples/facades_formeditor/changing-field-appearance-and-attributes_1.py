# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\formeditor\changing-field-appearance-and-attributes
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def add_field_and_set_attributes():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    doc = pdf.Document(os.path.join(data_dir, "FilledForm.pdf"))

    # Create an instance of FormEditor to manipulate form fields
    form_editor = pdf_facades.FormEditor(doc)

    # Add a new text field to the form on page 1 at the specified coordinates
    form_editor.AddField(
        pdf_facades.FieldType.Text,
        "text1",
        1,
        200, 550, 300, 575
    )

    # Set the field attribute to make the text field required
    form_editor.SetFieldAttribute("text1", pdf_facades.PropertyFlag.Required)

    # Set a character limit for the field (maximum 20 characters)
    form_editor.SetFieldLimit("text1", 20)

    # Save the updated PDF document
    form_editor.save(os.path.join(data_dir, "ChangingFieldAppearance_out.pdf"))

    # Dispose resources
    form_editor.Dispose()
    doc.Dispose()

    print("Text field 'text1' added successfully with required attribute and 20-character limit.")
