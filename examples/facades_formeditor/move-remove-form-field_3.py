# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\formeditor\move-remove-form-field
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def rename_fields():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create FormEditor instance
    editor = pdf_facades.FormEditor()

    # Bind PDF document
    editor.bind_pdf(os.path.join(data_dir, "ModifyFormField.pdf"))

    # Rename the field "textbox1" to "FirstName"
    editor.RenameField("textbox1", "FirstName")

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "RenameField_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Field 'textbox1' renamed successfully to 'FirstName'.")
