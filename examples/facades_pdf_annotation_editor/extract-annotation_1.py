# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfannotationeditor\extract-annotation
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Annotations import AnnotationType

def extract_annotation():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "AnnotationsInput.pdf"))

    # Create PdfAnnotationEditor instance
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.bind_pdf(document)

    # Define annotation types to extract (FreeText and Text)
    annotation_types = [AnnotationType.FreeText, AnnotationType.Text]

    # Extract annotations from page 1 to page 2
    annotations = annotation_editor.ExtractAnnotations(1, 2, annotation_types)

    # Display annotation contents
    for ann in annotations:
        print(ann.Contents)

    # Dispose resources
    annotation_editor.Dispose()
    document.Dispose()

    print("Annotations extracted successfully from pages 1–2.")
