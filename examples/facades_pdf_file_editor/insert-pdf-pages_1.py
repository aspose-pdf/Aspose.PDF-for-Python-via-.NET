# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\insert-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def insert_pdf_pages_between_two_numbers_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Insert pages:
    # - Insert pages 2–5 from InsertPages.pdf
    # - Into MultiplePages.pdf after page 1
    pdf_editor.insert(
        data_dir + "MultiplePages.pdf",  # destination PDF
        1,                               # position to insert after
        data_dir + "InsertPages.pdf",    # source PDF
        2,                               # start page
        5,                               # end page
        data_dir + "InsertPagesBetweenNumbers_out.pdf"
    )
