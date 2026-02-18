# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\extract-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def extract_array_pdf_pages_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()
    pages_to_extract = [1, 2]  # 1-based page numbers

    # Extract pages using streams
    with open(data_dir + "MultiplePages.pdf", "rb") as input_stream:
        with open(data_dir + "ExtractArrayOfPagesUsingStreams_out.pdf", "wb") as output_stream:
            pdf_editor.extract(input_stream, pages_to_extract, output_stream)
