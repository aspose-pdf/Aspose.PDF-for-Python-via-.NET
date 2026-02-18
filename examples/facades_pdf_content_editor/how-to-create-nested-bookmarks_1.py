# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\how-to-create-nested-bookmarks
# Code fence language: python


import os
import clr

# Add references to Aspose.PDF and System.Drawing
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from System.Drawing import Color

def add_bookmarks_action():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "Sample.pdf"))

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor(document)

    # Create a bookmark with action
    editor.CreateBookmarksAction(
        "Bookmark 1",     # Bookmark title
        Color.Green,      # Bookmark color
        True,             # Bold
        False,            # Italic
        "",               # Destination (empty string for default)
        "GoTo",           # Action type
        "2"               # Destination page number
    )

    # Save updated PDF document
    editor.save(os.path.join(data_dir, "PdfContentEditorDemo_Bookmark_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Bookmark with action added successfully.")
