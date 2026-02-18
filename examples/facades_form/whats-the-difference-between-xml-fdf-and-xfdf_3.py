# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\form\whats-the-difference-between-xml-fdf-and-xfdf
# Code fence language: python


xfdf_stream = FileStream(os.path.join(data_dir, "formdata.xfdf"), FileMode.Create)
form = pdf_facades.Form()
form.bind_pdf(os.path.join(data_dir, "input.pdf"))

form.ExportXfdf(xfdf_stream)
form.save(os.path.join(data_dir, "exported_xfdf.pdf"))

xfdf_stream.Close()
form.Dispose()
