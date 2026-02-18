# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\extract-image-and-change-position-of-a-stamp
# Code fence language: python


import os
import clr

# Add references to Aspose.PDF and System.Drawing
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")

import Aspose.Pdf.Facades as pdf_facades

def extract_image_from_stamp():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    pdf_content_editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    pdf_content_editor.bind_pdf(os.path.join(data_dir, "ExtractImage-ImageStamp.pdf"))

    # Get stamp info for the first page
    infos = pdf_content_editor.GetStamps(1)

    # Get the image from the first stamp
    image = infos[0].Image

    # Save the extracted image
    image.save(os.path.join(data_dir, "image_out.jpg"))

    # Dispose resources
    pdf_content_editor.Dispose()

    print("Image extracted successfully from stamp and saved as image_out.jpg.")
