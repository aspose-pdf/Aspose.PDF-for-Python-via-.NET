# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\form\whats-the-difference-between-xml-fdf-and-xfdf
# Code fence language: python


import os, clr
clr.AddReference("Aspose.PDF")
import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

data_dir = "/path/to/docs/"

form = pdf_facades.Form()
form.bind_pdf(os.path.join(data_dir, "input.pdf"))

xml_stream = FileStream(os.path.join(data_dir, "formdata.xml"), FileMode.Create)
form.ExportXml(xml_stream)

xml_stream.Close()
form.Dispose()

