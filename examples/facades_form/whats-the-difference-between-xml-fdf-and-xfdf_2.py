# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\form\whats-the-difference-between-xml-fdf-and-xfdf
# Code fence language: python


from System.IO import FileStream, FileMode

form = pdf_facades.Form()
form.bind_pdf(os.path.join(data_dir, "input.pdf"))

fdf_stream = FileStream(os.path.join(data_dir, "student.fdf"), FileMode.Open)
form.ImportFdf(fdf_stream)

form.save(os.path.join(data_dir, "filled_from_fdf.pdf"))

fdf_stream.Close()
form.Dispose()
