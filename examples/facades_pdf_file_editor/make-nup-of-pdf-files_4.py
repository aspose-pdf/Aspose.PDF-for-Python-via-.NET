# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\make-nup-of-pdf-files
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def make_nup_array_of_files_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    files = [
        data_dir + "MakeNupInput.pdf",
        data_dir + "MakeNupInput2.pdf"
    ]

    pdf_editor.make_nup(
        files,
        data_dir + "MakeNUpUsingArrayOfFilesAndPaths_out.pdf",
        is_sidewise=True
    )
