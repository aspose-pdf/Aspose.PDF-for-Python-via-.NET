# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfannotationeditor\import-export-annotations
# Code fence language: python


import os
import clr

# Add references to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Annotations import AnnotationType
from System.IO import File

def import_export_xfdf02():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind source PDF document
    annotation_editor.bind_pdf(os.path.join(data_dir, "ExportAnnotations.pdf"))

    # Export annotations to XFDF (pages 1–5, only FreeText and Text types)
    xfdf_output_path = os.path.join(data_dir, "exportannotations_out.xfdf")
    xml_output_stream = File.OpenWrite(xfdf_output_path)
    annotation_types = [AnnotationType.FreeText, AnnotationType.Text]
    annotation_editor.ExportAnnotationsXfdf(xml_output_stream, 1, 5, annotation_types)
    xml_output_stream.Close()

    # Import annotations into another PDF
    document = pdf.Document(os.path.join(data_dir, "input.pdf"))
    document.Pages.Add()

    # Bind the new PDF document
    annotation_editor.bind_pdf(document)

    # Import annotations from XFDF file
    xfdf_input_stream = File.OpenRead(os.path.join(data_dir, "annotations.xfdf"))
    annotation_editor.ImportAnnotationsFromXfdf(xfdf_input_stream)
    xfdf_input_stream.Close()

    # Save the updated PDF document
    annotation_editor.save(os.path.join(data_dir, "ImportedAnnotation_XFDF02_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()
    document.Dispose()

    print("Annotations exported to XFDF and imported into another PDF successfully.")
