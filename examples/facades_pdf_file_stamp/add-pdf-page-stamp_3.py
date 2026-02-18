# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilestamp\add-pdf-page-stamp
# Code fence language: python


from aspose.pdf.facades import (
    PdfFileStamp,
    PdfFileInfo,
    FormattedText,
    FontStyle,
    EncodingType
)
from aspose.pdf.facades import PageNumPosition
from System.Drawing import Color

def add_page_number_in_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    input_pdf = data_dir + "StampPDF.pdf"
    output_pdf = data_dir + "AddPageNumber_out.pdf"

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind PDF document
    file_stamp.bind_pdf(input_pdf)

    # Get total number of pages
    pdf_info = PdfFileInfo(input_pdf)
    total_pages = pdf_info.number_of_pages

    # Create formatted text for page number ("#" is replaced by current page number)
    formatted_text = FormattedText(
        f"Page # of {total_pages}",
        Color.AntiqueWhite,
        Color.Gray,
        FontStyle.times_bold_italic,
        EncodingType.winansi,
        False,
        12
    )

    # Set starting page number
    file_stamp.starting_number = 1

    # Add page number at upper-right position
    file_stamp.add_page_number(
        formatted_text,
        PageNumPosition.pos_upper_right
    )

    # Save output PDF
    file_stamp.save(output_pdf)

    # Close the stamp object
    file_stamp.close()
