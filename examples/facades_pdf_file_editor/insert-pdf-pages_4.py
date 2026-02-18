# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\insert-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def insert_array_of_pdf_pages_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Pages to insert (1-based page numbers)
    pages_to_insert = [2, 3]

    with open(data_dir + "MultiplePages.pdf", "rb") as input_stream, \
         open(data_dir + "InsertPages.pdf", "rb") as port_stream, \
         open(data_dir + "InsertPagesUsingStreams_out.pdf", "wb") as output_stream:

        # Insert selected pages into destination PDF
        pdf_editor.insert(
            input_stream,        # destination stream
            1,                   # insert after page 1
            port_stream,         # source stream
            pages_to_insert,     # pages to insert
            output_stream        # output stream
        )
