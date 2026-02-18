# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\formeditor\copy-inner-and-outer-field
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def copy_inner_field():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Add a new blank page to the document
    document.Pages.Add()

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Bind PDF document
    form_editor.bind_pdf(document)

    # Copy the field "Last Name" from the first page to "Last Name 2" on the second page
    form_editor.CopyInnerField("Last Name", "Last Name 2", 2)

    # Save modified PDF document
    form_editor.save(os.path.join(data_dir, "Sample-Form-01-mod.pdf"))

    # Dispose resources
    form_editor.Dispose()
    document.Dispose()

    print("Field 'Last Name' copied successfully to page 2 as 'Last Name 2'.")
