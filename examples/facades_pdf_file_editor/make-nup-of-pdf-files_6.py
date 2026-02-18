# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\make-nup-of-pdf-files
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor, PageSize

def make_nup_page_size_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    with open(data_dir + "MakeNupInput.pdf", "rb") as inp, \
         open(data_dir + "MakeNUpUsingPageSizeAndStreams_out.pdf", "wb") as outp:

        pdf_editor.make_nup(inp, outp, 2, 3, page_size=PageSize.A5)
