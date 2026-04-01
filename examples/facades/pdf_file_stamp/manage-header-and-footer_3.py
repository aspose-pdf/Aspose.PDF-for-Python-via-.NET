# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilestamp\manage-header-and-footer
# Code fence language: python


from aspose.pdf.facades import PdfFileStamp

def add_image_header():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    file_stamp = PdfFileStamp()
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Open image stream and add as header
    with open(data_dir + "ImageHeader.png", "rb") as image_stream:
        file_stamp.add_header(image_stream, 10)

    # Save output PDF
    file_stamp.save(data_dir + "AddImageHeader_out.pdf")
    file_stamp.close()
