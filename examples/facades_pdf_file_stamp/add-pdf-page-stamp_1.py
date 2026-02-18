# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilestamp\add-pdf-page-stamp
# Code fence language: python


from aspose.pdf.facades import PdfFileStamp, Stamp

def add_page_stamp_on_all_pages():
    data_dir = RunExamples.get_data_dir_aspose_pdf_images()

    # Create PdfFileStamp object
    file_stamp = PdfFileStamp()

    # Bind source PDF document
    file_stamp.bind_pdf(data_dir + "SourcePDF.pdf")

    # Create stamp object
    stamp = Stamp()

    # Bind PDF page to be used as stamp (page 1)
    stamp.bind_pdf(data_dir + "AddPageStampOnAllPages.pdf", 1)

    # Set stamp position and appearance
    stamp.set_origin(20, 20)
    stamp.rotation = 90.0
    stamp.is_background = True

    # Add stamp to all pages
    file_stamp.add_stamp(stamp)

    # Save output PDF
    file_stamp.save(data_dir + "PageStampOnAllPages_out.pdf")

    # Close the stamp object
    file_stamp.close()
