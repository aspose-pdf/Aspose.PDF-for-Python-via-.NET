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

def add_footer():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    file_stamp = PdfFileStamp()
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Create formatted text for footer
    footer_text = FormattedText(
        "Aspose - Your File Format Experts!",
        Color.Blue,
        Color.Gray,
        FontStyle.courier,
        EncodingType.winansi,
        False,
        14
    )

    # Add footer with bottom margin
    file_stamp.add_footer(footer_text, 10)

    # Save output PDF
    file_stamp.save(data_dir + "AddFooter_out.pdf")
    file_stamp.close()
