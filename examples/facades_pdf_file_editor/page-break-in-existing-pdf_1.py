# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\page-break-in-existing-pdf
# Code fence language: python


from aspose.pdf import Document
from aspose.pdf.facades import PdfFileEditor

def add_page_break_example01():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_page_break()

    # Open source PDF
    with Document(data_dir + "PageBreak.pdf") as src:
        # Create an empty destination PDF
        with Document() as dest:
            file_editor = PdfFileEditor()

            # Define page break: insert at page 1, position 450 units down
            page_break = PdfFileEditor.PageBreak(1, 450)

            # Add the page break
            file_editor.add_page_break(src, dest, [page_break])

            # Save the modified PDF
            dest.save(data_dir + "PageBreak_out.pdf")
