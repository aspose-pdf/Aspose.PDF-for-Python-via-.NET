# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\formeditor\import-export-form-field
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

def import_data():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(os.path.join(data_dir, "input.pdf"))

    # Import data from FDF
    fdf_stream = FileStream(os.path.join(data_dir, "student.fdf"), FileMode.Open)
    form.ImportFdf(fdf_stream)
    fdf_stream.Close()

    # Import data from XML
    xml_stream = FileStream(os.path.join(data_dir, "input.xml"), FileMode.Open)
    form.ImportXml(xml_stream)
    xml_stream.Close()

    # Import data from XFDF
    xfdf_stream = FileStream(os.path.join(data_dir, "input.xfdf"), FileMode.Open)
    form.ImportXfdf(xfdf_stream)
    xfdf_stream.Close()

    # Save updated PDF document
    form.save(os.path.join(data_dir, "ImportDataUpdated_out.pdf"))

    # Dispose resources
    form.Dispose()

    print("Data imported from FDF, XML, and XFDF successfully into the PDF form.")
