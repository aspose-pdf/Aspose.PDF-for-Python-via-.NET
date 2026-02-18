# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\adding-annotations-to-existing-pdf-file
# Code fence language: python


import os
import clr

# Add references to Aspose.PDF and System.Drawing
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from System.Drawing import Rectangle, Color

def add_line_annotation():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "input.pdf"))

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor(document)

    # Create Line Annotation
    editor.CreateLine(
        Rectangle(550, 93, 562, 439),   # Bounding rectangle
        "Test",                         # Title
        556, 99,                        # Starting coordinates (X1, Y1)
        556, 443,                       # Ending coordinates (X2, Y2)
        1,                              # Starting border style
        2,                              # Ending border style
        Color.Red,                      # Line color
        "dash",                         # Line style
        [1, 0, 3],                      # Dash pattern
        ["Open", "Open"]                # Line ending styles
    )

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "AddLineAnnotation_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Line annotation added successfully.")
