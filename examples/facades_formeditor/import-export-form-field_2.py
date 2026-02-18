# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\formeditor\import-export-form-field
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

def export_data():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(os.path.join(data_dir, "input.pdf"))

    # Export to FDF
    fdf_stream = FileStream(os.path.join(data_dir, "data_out.fdf"), FileMode.Create)
    form.ExportFdf(fdf_stream)
    fdf_stream.Close()

    # Export to XML
    xml_stream = FileStream(os.path.join(data_dir, "data_out.xml"), FileMode.Create)
    form.ExportXml(xml_stream)
    xml_stream.Close()

    # Export to XFDF
    xfdf_stream = FileStream(os.path.join(data_dir, "data_out.xfdf"), FileMode.Create)
    form.ExportXfdf(xfdf_stream)
    xfdf_stream.Close()

    # Dispose resources
    form.Dispose()

    print("Form data exported successfully to FDF, XML, and XFDF formats.")
