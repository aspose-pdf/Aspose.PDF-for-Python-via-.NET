# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilestamp\manage-header-and-footer
# Code fence language: python


from aspose.pdf.facades import (
    PdfFileStamp,
    FormattedText,
    FontStyle,
    EncodingType
)
from System.Drawing import Color

def add_header():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    file_stamp = PdfFileStamp()
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Create formatted text for header
    header_text = FormattedText(
        "Aspose - Your File Format Experts!",
        Color.Yellow,
        Color.Black,
        FontStyle.courier,
        EncodingType.winansi,
        False,
        14
    )

    # Add header with top margin
    file_stamp.add_header(header_text, 10)

    # Save output PDF
    file_stamp.save(data_dir + "AddHeader_out.pdf")
    file_stamp.close()
