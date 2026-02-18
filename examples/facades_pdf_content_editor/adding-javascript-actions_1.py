# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfcontenteditor\adding-javascript-actions
# Code fence language: python


import os
import clr

# Add references to Aspose.PDF and System.Drawing
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")

import Aspose.Pdf.Facades as pdf_facades
from System.Drawing import Rectangle, Color

def add_javascript_action():
    # Path to documents directory
    data_dir = "/path/to/documents/"  # <-- update to your actual path

    # Create PdfContentEditor
    editor = pdf_facades.PdfContentEditor()

    # Bind input PDF
    editor.bind_pdf(os.path.join(data_dir, "sample.pdf"))

    # Define rectangle area for JavaScript link (x, y, width, height)
    rect = Rectangle(50, 750, 150, 30)

    # JavaScript code to execute
    code = "app.alert('Welcome to Aspose!');"

    # Create JavaScript link annotation on page 1
    editor.CreateJavaScriptLink(code, rect, 1, Color.Green)

    # Save updated PDF
    editor.save(os.path.join(data_dir, "JavaScriptAdded_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("JavaScript action added successfully.")
