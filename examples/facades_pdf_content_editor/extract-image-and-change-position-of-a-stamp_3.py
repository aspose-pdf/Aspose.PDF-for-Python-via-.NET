# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\extract-image-and-change-position-of-a-stamp
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def move_stamp_by_id():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    pdf_content_editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    pdf_content_editor.bind_pdf(os.path.join(data_dir, "ChangeStampPosition.pdf"))

    # Define page ID, stamp ID, and new coordinates
    page_id = 1
    stamp_id = 1
    x = 200
    y = 200

    # Change the position of the stamp to new x and y position
    pdf_content_editor.MoveStamp(page_id, stamp_id, x, y)

    # Save updated PDF document
    pdf_content_editor.save(os.path.join(data_dir, "ChangeStampPositionByID_out.pdf"))

    # Dispose resources
    pdf_content_editor.Dispose()

    print("Stamp moved successfully by ID.")
