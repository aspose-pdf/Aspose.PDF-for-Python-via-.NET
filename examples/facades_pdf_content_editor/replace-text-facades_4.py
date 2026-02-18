# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\replace-text-facades
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def replace_text04():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    editor.bind_pdf(os.path.join(data_dir, "sample.pdf"))

    # Replace all occurrences of "Value" with "Label"
    count = 0
    while editor.ReplaceText("Value", "Label"):
        count += 1

    print(f"{count} occurrences have been replaced.")

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "PdfContentEditorDemo04_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Text replacement completed successfully.")
