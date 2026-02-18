# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\insert-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def insert_array_of_pdf_pages_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Pages to insert (1-based page numbers)
    pages_to_insert = [2, 3]

    # Insert selected pages into destination PDF
    pdf_editor.insert(
        data_dir + "MultiplePages.pdf",  # destination PDF
        1,                               # insert after page 1
        data_dir + "InsertPages.pdf",    # source PDF
        pages_to_insert,                 # pages to insert
        data_dir + "InsertArrayOfPages_out.pdf"
    )
