# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\formeditor\copy-inner-and-outer-field
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def copy_outer_field():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create empty PDF document
    document = pdf.Document()

    # Add a new blank page
    document.Pages.Add()

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Bind the new PDF document
    form_editor.bind_pdf(document)

    # Copy the outer field "First Name" from the original document to the new document
    form_editor.CopyOuterField(os.path.join(data_dir, "Sample-Form-01.pdf"), "First Name", 1)

    # Copy the outer field "Last Name" from the original document to the new document
    form_editor.CopyOuterField(os.path.join(data_dir, "Sample-Form-01.pdf"), "Last Name", 1)

    # Save the modified PDF document
    form_editor.save(os.path.join(data_dir, "Sample-Form-02-mod.pdf"))

    # Dispose resources
    form_editor.Dispose()
    document.Dispose()

    print("Outer fields 'First Name' and 'Last Name' copied successfully into new PDF.")
