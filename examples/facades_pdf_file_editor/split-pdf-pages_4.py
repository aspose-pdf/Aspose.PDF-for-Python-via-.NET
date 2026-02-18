# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\split-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def split_pdf_pages_to_bulk_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    ranges = [[1, 2], [3, 4]]

    with open(data_dir + "MultiplePages.pdf", "rb") as inp:
        out_streams = pdf_editor.split_to_bulks(inp, ranges)

        i = 1
        for s in out_streams:
            with open(f"{data_dir}File_{i}_out.pdf", "wb") as outp:
                s.write_to(outp)
            i += 1
