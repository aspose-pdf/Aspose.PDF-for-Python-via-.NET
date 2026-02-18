# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\split-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def split_pdf_pages_from_first_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    with open(data_dir + "MultiplePages.pdf", "rb") as inp, \
         open(data_dir + "SplitPagesUsingStreams_out.pdf", "wb") as outp:

        pdf_editor.split_from_first(inp, 3, outp)
