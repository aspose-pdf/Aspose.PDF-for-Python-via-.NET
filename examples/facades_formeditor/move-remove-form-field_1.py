# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\formeditor\move-remove-form-field
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def move_field():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create FormEditor instance
    editor = pdf_facades.FormEditor()

    # Bind PDF document
    editor.bind_pdf(os.path.join(data_dir, "MoveField.pdf"))

    # Move the field "textbox1" to new coordinates (left, bottom, right, top)
    editor.MoveField("textbox1", 262.56, 496.75, 382.28, 514.03)

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "MoveField_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Field 'textbox1' moved successfully to new position.")
