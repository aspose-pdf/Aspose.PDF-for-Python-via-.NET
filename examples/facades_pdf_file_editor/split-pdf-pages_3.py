# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\split-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def split_pdf_pages_to_bulk_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    page_ranges = [[1, 2], [3, 4]]

    out_streams = pdf_editor.split_to_bulks(
        data_dir + "MultiplePages.pdf",
        page_ranges
    )

    index = 1
    for stream in out_streams:
        with open(f"{data_dir}File_{index}_out.pdf", "wb") as outp:
            stream.write_to(outp)
        index += 1
