# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilestamp\add-text-and-image-stamp
# Code fence language: python


from aspose.pdf.facades import (
    PdfFileStamp,
    Stamp,
    FormattedText,
    FontStyle,
    EncodingType
)
from System.Drawing import Color

def add_text_stamp_on_particular_pages_in_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind source PDF document
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Create stamp object
    stamp = Stamp()

    # Create formatted text and bind it as a logo (text stamp)
    text = FormattedText(
        "Hello World!",
        Color.Blue,
        Color.Gray,
        FontStyle.helvetica,
        EncodingType.winansi,
        True,
        14
    )
    stamp.bind_logo(text)

    # Configure stamp properties
    stamp.set_origin(10, 400)
    stamp.rotation = 90.0
    stamp.is_background = True

    # Apply stamp only to selected pages (page 2)
    stamp.pages = [2]

    # Add stamp to the PDF
    file_stamp.add_stamp(stamp)

    # Save output PDF
    file_stamp.save(data_dir + "AddTextStampOnParticularPages_out.pdf")

    # Close the stamp object
    file_stamp.close()
