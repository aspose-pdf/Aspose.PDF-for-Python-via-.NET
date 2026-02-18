# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\extract-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def extract_pdf_pages_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Extract pages using streams (1-based page numbers)
    with open(data_dir + "MultiplePages.pdf", "rb") as input_stream:
        with open(data_dir + "ExtractPagesBetweenTwoNumbers_out.pdf", "wb") as output_stream:
            pdf_editor.extract(input_stream, 1, 3, output_stream)
