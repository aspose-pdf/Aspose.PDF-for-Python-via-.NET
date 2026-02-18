# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\formeditor\working-with-list-item
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def del_list_item():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of FormEditor to manipulate form fields
    form_editor = pdf_facades.FormEditor()

    # Bind PDF document
    form_editor.bind_pdf(os.path.join(data_dir, "Sample-Form-04.pdf"))

    # Delete the list item "France" from the 'Country' ListBox field
    form_editor.DelListItem("Country", "France")

    # Save modified PDF document
    form_editor.save(os.path.join(data_dir, "Sample-Form-04-mod.pdf"))

    # Dispose resources
    form_editor.Dispose()

    print("List item 'France' removed successfully from the 'Country' ListBox field.")
