# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\make-booklet-of-pdf
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def make_booklet_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    pdf_editor.make_booklet(
        data_dir + "MakeBookletInput.pdf",
        data_dir + "MakeBookletUsingPaths_out.pdf"
    )
