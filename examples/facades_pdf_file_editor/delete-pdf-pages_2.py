# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\delete-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def delete_pages_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    pages_to_delete = [1, 2]  # 1-based page indexes

    with open(data_dir + "DeletePagesInput.pdf", "rb") as input_stream:
        with open(data_dir + "DeletePagesUsingStream_out.pdf", "wb") as output_stream:
            pdf_editor.delete(input_stream, pages_to_delete, output_stream)
