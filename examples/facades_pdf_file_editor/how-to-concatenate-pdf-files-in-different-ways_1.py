# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\how-to-concatenate-pdf-files-in-different-ways
# Code fence language: python


import aspose.pdf.facades as apf

def concatenate_two_files(input1: str, input2: str, output: str):
    pdf_editor = apf.PdfFileEditor()
    pdf_editor.concatenate(input1, input2, output)

# Example usage
concatenate_two_files(
    "FirstDocument.pdf",
    "SecondDocument.pdf",
    "ConcatenatedOutput.pdf"
)
