# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\formeditor\working-with-list-item
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def add_list_item():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of FormEditor to manipulate form fields
    form_editor = pdf_facades.FormEditor()

    # Bind PDF document
    form_editor.bind_pdf(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Add a ListBox field for selecting country, placed at the specified coordinates on page 1
    form_editor.AddField(
        pdf_facades.FieldType.ListBox,
        "Country",
        1,
        232.56, 476.75, 352.28, 514.03
    )

    # Add list items to the 'Country' ListBox field
    form_editor.AddListItem("Country", "USA")
    form_editor.AddListItem("Country", "Canada")
    form_editor.AddListItem("Country", "France")
    form_editor.AddListItem("Country", "Spain")

    # Save modified PDF document
    form_editor.save(os.path.join(data_dir, "Sample-Form-01-mod.pdf"))

    # Dispose resources
    form_editor.Dispose()

    print("ListBox 'Country' added successfully with items: USA, Canada, France, Spain.")
