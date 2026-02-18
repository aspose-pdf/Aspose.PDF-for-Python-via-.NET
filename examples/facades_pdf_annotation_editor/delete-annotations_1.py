# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfannotationeditor\delete-annotations
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def delete_all_annotations():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create an instance of PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.bind_pdf(os.path.join(data_dir, "DeleteAllAnnotationsFromPage.pdf"))

    # Delete all annotations from the document
    annotation_editor.DeleteAnnotations()

    # Save the updated PDF document
    annotation_editor.save(os.path.join(data_dir, "DeleteAllAnnotationsFromPage_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()

    print("All annotations deleted successfully from the PDF.")
