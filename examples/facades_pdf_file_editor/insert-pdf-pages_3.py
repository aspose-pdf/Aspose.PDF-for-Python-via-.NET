# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\insert-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def insert_pdf_pages_between_two_numbers_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    with open(data_dir + "MultiplePages.pdf", "rb") as input_stream, \
         open(data_dir + "InsertPages.pdf", "rb") as port_stream, \
         open(data_dir + "InsertPagesBetweenNumbersUsingStreams_out.pdf", "wb") as output_stream:

        # Insert pages:
        # Insert pages 1–4 from InsertPages.pdf into MultiplePages.pdf after page 1
        pdf_editor.insert(
            input_stream,
            1,
            port_stream,
            1,
            4,
            output_stream
        )
