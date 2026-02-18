# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\working-with-attachments-facades
# Code fence language: python


import os
import clr

# Add references to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def delete_all_attachments():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor with a PDF document
    document = pdf.Document(os.path.join(data_dir, "DeleteAllAttachments.pdf"))
    editor = pdf_facades.PdfContentEditor(document)

    # Delete all attachments from the PDF
    editor.DeleteAttachments()

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "DeleteAllAttachments_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("All attachments deleted successfully.")
