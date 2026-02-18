# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfannotationeditor\flatten-annotation
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Forms import Form

def flatten_annotation_from_pdf():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.bind_pdf(os.path.join(data_dir, "AnnotationsInput.pdf"))

    # Create FlattenSettings
    flatten_settings = Form.FlattenSettings()
    flatten_settings.ApplyRedactions = True
    flatten_settings.CallEvents = False
    flatten_settings.HideButtons = True
    flatten_settings.UpdateAppearances = True

    # Flatten annotations with the specified settings
    annotation_editor.FlatteningAnnotations(flatten_settings)

    # Save updated PDF document
    annotation_editor.save(os.path.join(data_dir, "FlattenAnnotation_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()

    print("Annotations flattened successfully into the PDF.")
