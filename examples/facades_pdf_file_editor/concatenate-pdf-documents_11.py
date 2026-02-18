# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\concatenate-pdf-documents
# Code fence language: python


from aspose.pdf.facades import PdfContentEditor
from aspose.pdf.facades import Color
from aspose.pdf import Rectangle

def create_local_links():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Create PdfContentEditor object
    content_editor = PdfContentEditor()

    # Bind the PDF document
    content_editor.bind_pdf(
        data_dir + "ConcatenatePdfFilesAndCreateTOC_out.pdf"
    )

    # Create a local link for the first document
    content_editor.create_local_link(
        Rectangle(150, 650, 100, 20),  # Link rectangle (x, y, width, height)
        2,                             # Destination page number
        1,                             # Source page number
        Color.transparent              # Border color
    )
