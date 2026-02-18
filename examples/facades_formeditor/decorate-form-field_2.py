# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\formeditor\decorate-form-field
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def decorate_field2():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of FormEditor to manipulate form fields
    editor = pdf_facades.FormEditor()

    # Bind PDF document
    editor.bind_pdf(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Create a FormFieldFacade object to define alignment properties
    text_field_decoration = pdf_facades.FormFieldFacade()
    text_field_decoration.Alignment = pdf_facades.FormFieldFacade.AlignCenter

    # Assign the decoration facade to the FormEditor
    editor.Facade = text_field_decoration

    # Apply the alignment decoration to all text fields in the PDF
    editor.DecorateField(pdf_facades.FieldType.Text)

    # Save modified PDF document
    editor.save(os.path.join(data_dir, "Sample-Form-01-align-text.pdf"))

    # Dispose resources
    editor.Dispose()

    print("All text fields aligned to center successfully.")
