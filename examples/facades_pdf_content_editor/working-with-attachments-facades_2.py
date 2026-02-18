# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\working-with-attachments-facades
# Code fence language: python


import os
import clr

# Add references to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from System.IO import File

def add_attachment():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor with a PDF document
    document = pdf.Document(os.path.join(data_dir, "AddAttachment.pdf"))
    editor = pdf_facades.PdfContentEditor(document)

    # Open file stream for the attachment
    file_stream = File.OpenRead(os.path.join(data_dir, "Demo_MP3.mp3"))

    # Add attachment to the PDF
    editor.AddDocumentAttachment(file_stream, "Demo_MP3.mp3", "Demo MP3 file")

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "AddAttachment_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Attachment added successfully using file stream.")
