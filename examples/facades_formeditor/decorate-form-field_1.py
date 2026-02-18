# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\formeditor\decorate-form-field
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")  # Needed for colors

import Aspose.Pdf.Facades as pdf_facades
from System.Drawing import Color

def decorate_field():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of FormEditor to manipulate form fields
    editor = pdf_facades.FormEditor()

    # Bind PDF document
    editor.bind_pdf(os.path.join(data_dir, "Sample-Form-01.pdf"))

    # Create a FormFieldFacade object to define decoration properties
    city_decoration = pdf_facades.FormFieldFacade()
    city_decoration.Font = pdf_facades.FontStyle.Courier
    city_decoration.FontSize = 12
    city_decoration.BorderColor = Color.Black
    city_decoration.BorderWidth = 2

    # Assign the decoration facade to the FormEditor
    editor.Facade = city_decoration

    # Apply the decoration to the field named "City"
    editor.DecorateField("City")

    # Save modified PDF document
    editor.save(os.path.join(data_dir, "Sample-Form-02.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Field 'City' decorated successfully with custom font and border settings.")
