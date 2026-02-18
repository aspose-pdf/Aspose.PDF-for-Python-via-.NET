# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilestamp\add-text-and-image-stamp
# Code fence language: python


from aspose.pdf.facades import PdfFileStamp, Stamp

def add_image_stamp_on_all_pages_in_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind source PDF document
    file_stamp.bind_pdf(data_dir + "sample.pdf")

    # Create stamp object
    stamp = Stamp()

    # Bind image to stamp
    stamp.bind_image(data_dir + "StampImage.png")

    # Configure stamp properties
    stamp.set_origin(10, 200)
    stamp.rotation = 90.0
    stamp.is_background = True

    # OPTIONAL:
    # If you want to apply the stamp only to selected pages, uncomment below
    # stamp.pages = [2]

    # Add stamp to PDF file (applies to all pages by default)
    file_stamp.add_stamp(stamp)

    # Save output PDF
    file_stamp.save(data_dir + "AddImageStampOnAllPages_out.pdf")

    # Close the stamp object
    file_stamp.close()
