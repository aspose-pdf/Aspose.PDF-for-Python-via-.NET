# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilestamp\manage-header-and-footer
# Code fence language: python


from aspose.pdf.facades import PdfFileStamp

def add_image_footer():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    file_stamp = PdfFileStamp()
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Open image stream and add as footer
    with open(data_dir + "ImageFooter.png", "rb") as image_stream:
        file_stamp.add_footer(image_stream, 10)

    # Save output PDF
    file_stamp.save(data_dir + "AddImageFooter_out.pdf")
    file_stamp.close()
