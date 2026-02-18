# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\replace-text-facades
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def replace_text06():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor with ReplaceTextStrategy
    strategy = pdf_facades.ReplaceTextStrategy()
    strategy.IsRegularExpressionUsed = True
    strategy.ReplaceScope = pdf_facades.ReplaceTextStrategy.Scope.ReplaceAll

    editor = pdf_facades.PdfContentEditor()
    editor.ReplaceTextStrategy = strategy

    # Bind PDF document
    editor.bind_pdf(os.path.join(data_dir, "sample.pdf"))

    # Replace all 4-digit numbers with "ABCDE"
    editor.ReplaceText(r"\d{4}", "ABCDE")

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "PdfContentEditorDemo06_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Text replaced successfully using regex strategy.")
