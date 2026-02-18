# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\how-to-concatenate-pdf-files-in-different-ways
# Code fence language: python


import aspose.pdf.facades as apf

def concatenate_streams(file1: str, file2: str, output: str):
    pdf_editor = apf.PdfFileEditor()

    with open(file1, "rb") as pdf1, \
         open(file2, "rb") as pdf2, \
         open(output, "wb") as out_stream:

        pdf_editor.concatenate(pdf1, pdf2, out_stream)

# Example usage
concatenate_streams(
    "FirstDocument.pdf",
    "SecondDocument.pdf",
    "ConcatenatedOutput_byStreams.pdf"
)
