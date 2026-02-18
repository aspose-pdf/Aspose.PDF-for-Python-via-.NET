# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\page-break-in-existing-pdf
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def add_page_break_example02():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_page_break()

    file_editor = PdfFileEditor()

    # Insert page break into a PDF via file paths
    page_break = PdfFileEditor.PageBreak(1, 450)

    file_editor.add_page_break(
        data_dir + "PageBreak.pdf",
        data_dir + "PageBreakWithDestPath_out.pdf",
        [page_break]
    )
