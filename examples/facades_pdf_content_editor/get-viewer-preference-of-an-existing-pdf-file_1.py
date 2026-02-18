# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\get-viewer-preference-of-an-existing-pdf-file
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def get_viewer_preference():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "SetViewerPreference.pdf"))

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor(document)

    # Get Viewer Preferences
    preferences = editor.GetViewerPreference()

    # Check specific preferences
    if (preferences & pdf_facades.ViewerPreference.CenterWindow) != 0:
        print("CenterWindow")

    if (preferences & pdf_facades.ViewerPreference.HideMenubar) != 0:
        print("Menu bar hidden")

    if (preferences & pdf_facades.ViewerPreference.PageModeFullScreen) != 0:
        print("Page Mode Full Screen")

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Viewer preferences retrieved successfully.")
