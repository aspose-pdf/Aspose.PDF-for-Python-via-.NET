# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\working-with-images
# Code fence language: python


import os
import clr

# Add references to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def delete_images():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor with a PDF document
    document = pdf.Document(os.path.join(data_dir, "sample.pdf"))
    editor = pdf_facades.PdfContentEditor(document)

    # Delete all images from the PDF
    editor.DeleteImage()

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "PdfContentEditorDemo11.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("All images deleted successfully from the PDF.")
