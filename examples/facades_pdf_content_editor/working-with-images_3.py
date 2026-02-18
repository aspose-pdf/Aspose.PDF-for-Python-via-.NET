# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\working-with-images
# Code fence language: python


import os
import clr

# Add references to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def replace_image():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor with a PDF document
    document = pdf.Document(os.path.join(data_dir, "sample_cats_dogs.pdf"))
    editor = pdf_facades.PdfContentEditor(document)

    # Replace image on page 2, image index 4 with a new image
    editor.ReplaceImage(2, 4, os.path.join(data_dir, "Image.jpg"))

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "PdfContentEditorDemo12.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Image replaced successfully in the PDF.")
