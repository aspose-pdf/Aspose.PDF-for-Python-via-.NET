# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\split-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def split_pdf_pages_to_end_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    pdf_editor.split_to_end(
        data_dir + "MultiplePages.pdf",
        3,
        data_dir + "SplitPagesToEndUsingPaths_out.pdf"
    )
