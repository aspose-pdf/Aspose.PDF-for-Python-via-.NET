# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\how-to-concatenate-pdf-files-in-different-ways
# Code fence language: python


import aspose.pdf.facades as apf

def concatenate_multiple_streams(inputs: list[str], output: str):
    pdf_editor = apf.PdfFileEditor()

    # Open all input streams
    input_streams = [open(f, "rb") for f in inputs]

    try:
        with open(output, "wb") as out_stream:
            pdf_editor.concatenate(input_streams, out_stream)
    finally:
        # Always close streams
        for st in input_streams:
            st.close()

# Example usage
concatenate_multiple_streams(
    ["file1.pdf", "file2.pdf", "file3.pdf"],
    "Concatenated_Multiple.pdf"
)
