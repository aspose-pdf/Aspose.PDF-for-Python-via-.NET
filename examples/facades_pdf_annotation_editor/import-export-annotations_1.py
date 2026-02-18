# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfannotationeditor\import-export-annotations
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def import_annotation():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Sources of PDF with annotations
    sources = [os.path.join(data_dir, "ImportAnnotations.pdf")]

    # Create PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind target PDF document
    annotation_editor.bind_pdf(os.path.join(data_dir, "input.pdf"))

    # Import annotations from source PDFs
    annotation_editor.ImportAnnotations(sources)

    # Save updated PDF document
    annotation_editor.save(os.path.join(data_dir, "ImportAnnotations_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()

    print("Annotations imported successfully from source PDF into target document.")
