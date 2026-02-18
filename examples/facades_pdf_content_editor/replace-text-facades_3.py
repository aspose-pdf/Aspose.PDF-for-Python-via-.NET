# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\replace-text-facades
# Code fence language: python


import os
import clr

# Add references to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Text import TextState
import Aspose.Pdf as pdf

def replace_text03():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    editor.bind_pdf(os.path.join(data_dir, "sample.pdf"))

    # Define text state with formatting
    text_state = TextState()
    text_state.ForegroundColor = pdf.Color.Red
    text_state.FontSize = 12

    # Replace text: "Value" -> "Label" with formatting
    editor.ReplaceText("Value", "Label", text_state)

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "PdfContentEditorDemo03_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Text replaced successfully with formatting applied.")
