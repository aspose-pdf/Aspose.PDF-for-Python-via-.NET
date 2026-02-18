# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\make-booklet-of-pdf
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def make_booklet_left_right_only_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    left_pages = [1, 5]
    right_pages = [2, 3]

    pdf_editor.make_booklet(
        data_dir + "MakeBookletMultiplePagesInput.pdf",
        data_dir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf",
        left_pages,
        right_pages
    )
