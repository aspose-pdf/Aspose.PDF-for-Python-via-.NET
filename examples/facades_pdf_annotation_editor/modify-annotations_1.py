# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfannotationeditor\modify-annotations
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def modify_annotations_author():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.bind_pdf(os.path.join(data_dir, "AnnotationsInput.pdf"))

    # Modify annotations author on pages 1–2
    annotation_editor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user")

    # Save updated PDF document
    annotation_editor.save(os.path.join(data_dir, "ModifyAnnotationsAuthor_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()

    print("Annotations author modified successfully on pages 1–2.")
