# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\replace-text-facades
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def replace_text02():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    editor.bind_pdf(os.path.join(data_dir, "sample.pdf"))

    # Replace text: "Value" -> "Label" with font size 12
    editor.ReplaceText("Value", "Label", 12)

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "PdfContentEditorDemo02_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Text replaced successfully with new font size.")
