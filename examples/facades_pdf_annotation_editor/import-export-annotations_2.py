# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfannotationeditor\import-export-annotations
# Code fence language: python


import os
import clr

# Add references to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from System.IO import File, FileMode

def import_export_xfdf01():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind source PDF document
    annotation_editor.bind_pdf(os.path.join(data_dir, "ExportAnnotations.pdf"))

    # Export annotations to XFDF
    xfdf_output_path = os.path.join(data_dir, "exportannotations_out.xfdf")
    xml_output_stream = File.OpenWrite(xfdf_output_path)
    annotation_editor.ExportAnnotationsToXfdf(xml_output_stream)
    xml_output_stream.Close()

    # Create a new PDF document
    document = pdf.Document()
    document.Pages.Add()

    # Bind the new PDF document
    annotation_editor.bind_pdf(document)

    # Import annotations from XFDF file
    xfdf_input_stream = File.OpenRead(xfdf_output_path)
    annotation_editor.ImportAnnotationsFromXfdf(xfdf_input_stream)
    xfdf_input_stream.Close()

    # Save the updated PDF document
    annotation_editor.save(os.path.join(data_dir, "ImportedAnnotation_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()
    document.Dispose()

    print("Annotations exported to XFDF and imported into a new PDF successfully.")
