# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\make-nup-of-pdf-files
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def make_nup_array_of_files_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    with open(data_dir + "MakeNupInput.pdf", "rb") as s1, \
         open(data_dir + "MakeNupInput2.pdf", "rb") as s2, \
         open(data_dir + "MakeNUpUsingArrayOfFilesAndStreams_out.pdf", "wb") as outp:

        streams = [s1, s2]
        pdf_editor.make_nup(streams, outp, is_sidewise=True)
