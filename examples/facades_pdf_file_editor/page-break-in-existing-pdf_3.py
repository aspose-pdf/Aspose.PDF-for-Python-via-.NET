# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\page-break-in-existing-pdf
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def add_page_break_example03():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_page_break()

    file_editor = PdfFileEditor()
    page_break = PdfFileEditor.PageBreak(1, 450)

    with open(data_dir + "PageBreak.pdf", "rb") as src_stream, \
         open(data_dir + "PageBreakWithStream_out.pdf", "wb") as dest_stream:

        file_editor.add_page_break(src_stream, dest_stream, [page_break])
