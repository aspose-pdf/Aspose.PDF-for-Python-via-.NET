# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilestamp\add-pdf-page-stamp
# Code fence language: python


from aspose.pdf.facades import PdfFileStamp, Stamp

def add_page_stamp_on_certain_pages():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind source PDF document
    file_stamp.bind_pdf(data_dir + "SourcePDF.pdf")

    # Create stamp object
    stamp = Stamp()

    # Bind PDF page to be used as stamp (page 1)
    stamp.bind_pdf(data_dir + "PageStampOnCertainPages.pdf", 1)

    # Configure stamp properties
    stamp.set_origin(20, 20)
    stamp.rotation = 90.0
    stamp.is_background = True

    # Apply stamp only to selected pages (1 and 3)
    stamp.pages = [1, 3]

    # Add stamp to the PDF
    file_stamp.add_stamp(stamp)

    # Save output PDF
    file_stamp.save(data_dir + "PageStampOnCertainPages_out.pdf")

    # Close the stamp object
    file_stamp.close()
