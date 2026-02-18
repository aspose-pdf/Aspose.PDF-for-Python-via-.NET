# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\stamp\rotating-stamp-about-the-center-point
# Code fence language: python


import aspose.pdf as pdf

def add_rotating_stamp_to_pdf():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_technical_articles()

    # PdfFileInfo is used to get page width and height
    file_info = pdf.facades.PdfFileInfo(data_dir + "RotatingStamp.pdf")

    try:
        # Create Stamp object
        stamp = pdf.facades.Stamp()

        # Bind image to stamp
        stamp.bind_image(data_dir + "RotatingStamp.jpg")

        # Specify whether the stamp is background
        stamp.is_background = False

        # Specify pages where the stamp will be applied
        stamp.pages = [1]

        # Rotate stamp around its center (0–360 degrees)
        stamp.rotation = 90

        # Set the origin (lower-left corner of the stamp)
        stamp.set_origin(
            file_info.get_page_width(1) / 2,
            file_info.get_page_height(1) / 2
        )

        # Set image size
        stamp.set_image_size(100, 100)

        # Open PDF document
        document = pdf.Document(data_dir + "RotatingStamp_out.pdf")

        try:
            # Create PdfFileStamp to apply the stamp
            stamper = pdf.facades.PdfFileStamp(document)

            try:
                # Add stamp to the PDF
                stamper.add_stamp(stamp)
            finally:
                stamper.close()
                document.close()
                file_info.close()
