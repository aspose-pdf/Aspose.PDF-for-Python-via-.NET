# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\make-booklet-of-pdf
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor, PageSize

def make_booklet_size_and_left_right_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    left_pages = [1, 5]
    right_pages = [2, 3]

    with open(data_dir + "MakeBookletMultiplePagesInput.pdf", "rb") as inp, \
         open(data_dir + "MakeBookletUsingPageSizeLeftRightPagesAndStreams_out.pdf", "wb") as outp:

        pdf_editor.make_booklet(inp, outp, PageSize.A5, left_pages, right_pages)
