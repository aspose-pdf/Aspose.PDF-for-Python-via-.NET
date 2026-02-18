# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\extract-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def extract_pdf_pages_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Extract pages (from page 1 to page 3, inclusive)
    pdf_editor.extract(
        data_dir + "MultiplePages.pdf",
        1,
        3,
        data_dir + "ExtractPagesBetweenNumbers_out.pdf"
    )
