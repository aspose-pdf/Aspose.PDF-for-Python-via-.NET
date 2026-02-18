# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\set-viewer-preference-of-an-existing-pdf-file
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def set_viewer_preference():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "Sample.pdf"))

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor(document)

    # Change Viewer Preferences
    editor.ChangeViewerPreference(pdf_facades.ViewerPreference.CenterWindow)
    editor.ChangeViewerPreference(pdf_facades.ViewerPreference.HideMenubar)
    editor.ChangeViewerPreference(pdf_facades.ViewerPreference.PageModeFullScreen)

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "PdfContentEditorDemo_SetViewerPreference_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Viewer preferences set successfully.")
