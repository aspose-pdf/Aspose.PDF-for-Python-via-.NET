# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\extract-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def extract_array_pdf_pages_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Pages to extract (1-based indexes)
    pages_to_extract = [1, 2]

    # Extract pages
    pdf_editor.extract(
        data_dir + "Extract.pdf",
        pages_to_extract,
        data_dir + "ExtractArrayOfPages_out.pdf"
    )
