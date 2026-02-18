# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\concatenate-pdf-documents
# Code fence language: python


from aspose.pdf.facades import Stamp, FormattedText, PdfFileInfo, FontStyle, EncodingType
from aspose.pdf.facades import Color

def add_text_stamp_for_table_of_contents():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()
    input_pdf_file = data_dir + "ConcatenateInput1.pdf"

    # Create a Stamp object
    stamp = Stamp()

    # Bind text to the stamp
    formatted_text = FormattedText(
        "Table Of Contents",      # Text to display
        Color.maroon,             # Text color
        Color.transparent,        # Background color
        FontStyle.Helvetica,      # Font
        EncodingType.Winansi,     # Encoding type
        True,                     # Bold
        18                        # Font size
    )
    stamp.bind_logo(formatted_text)

    # Specify the origin of the stamp
    page_width = PdfFileInfo(input_pdf_file).get_page_width(1)
    stamp.set_origin(page_width / 3, 700)

    # Apply stamp to specific pages
    stamp.pages = [1]
