# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfannotationeditor\modify-annotations
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Annotations import TextAnnotation

def modify_annotations():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "AnnotationsInput.pdf"))

    # Create PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.bind_pdf(document)

    # Create a new TextAnnotation object
    rect = pdf.Rectangle(200, 400, 400, 600)
    new_text_annotation = TextAnnotation(document.Pages[1], rect)
    new_text_annotation.Title = "Updated title"
    new_text_annotation.Subject = "Updated subject"
    new_text_annotation.Contents = "Updated sample contents for the annotation"

    # Modify annotations in the PDF file (page 1 only)
    annotation_editor.ModifyAnnotations(1, 1, new_text_annotation)

    # Save updated PDF document
    annotation_editor.save(os.path.join(data_dir, "ModifyAnnotations_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()
    document.Dispose()

    print("Annotations modified successfully on page 1.")
