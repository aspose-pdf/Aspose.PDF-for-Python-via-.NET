# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\split-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def split_pdf_to_individual_pages_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    with open(data_dir + "splitPdfToIndividualPagesInput.pdf", "rb") as inp:
        buffers = pdf_editor.split_to_pages(inp)

        i = 1
        for b in buffers:
            with open(f"{data_dir}File_{i}_out.pdf", "wb") as outp:
                b.write_to(outp)
            i += 1
