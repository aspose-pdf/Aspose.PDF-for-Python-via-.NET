# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\adding-annotations-to-existing-pdf-file
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")  # Needed for Rectangle

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Text import TextFragmentAbsorber
from System.Drawing import Rectangle

def add_free_text_annotation():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "input.pdf"))

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor(document)

    # Search for the text "PDF" on the first page
    tfa = TextFragmentAbsorber("PDF")
    tfa.Visit(document.Pages[1])

    # Define rectangle above the found text fragment
    rect = Rectangle(
        int(tfa.TextFragments[1].Rectangle.LLX),
        int(tfa.TextFragments[1].Rectangle.URY) + 5,
        100,   # Width
        18     # Height
    )

    # Add free text annotation on page 1
    editor.CreateFreeText(rect, "Free Text Demo", 1)

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "AddFreeTextAnnotation_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Free text annotation added successfully.")
