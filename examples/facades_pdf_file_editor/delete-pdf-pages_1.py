# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\delete-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def delete_pages():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Pages to delete 
    pages_to_delete = [1, 2]

    # Delete pages
    pdf_editor.delete(
        data_dir + "DeletePagesInput.pdf",
        pages_to_delete,
        data_dir + "DeletePagesUsingFilePath_out.pdf"
    )
