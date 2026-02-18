# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\make-nup-of-pdf-files
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor, PageSize

def make_nup_page_size_horizontal_vertical_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    pdf_editor.make_nup(
        data_dir + "MakeNupInput.pdf",
        data_dir + "MakeNUpUsingPageSizeHorizontalAndVerticalValues_out.pdf",
        page_size=PageSize.A5,
        horizontal_pages=2,
        vertical_pages=3
    )
