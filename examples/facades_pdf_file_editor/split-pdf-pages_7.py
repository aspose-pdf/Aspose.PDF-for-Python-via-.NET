# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\split-pdf-pages
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def split_pdf_to_individual_pages_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    out_buffers = pdf_editor.split_to_pages(data_dir + "splitPdfToIndividualPagesInput.pdf")

    count = 1
    for buf in out_buffers:
        with open(f"{data_dir}File_{count}_out.pdf", "wb") as outp:
            buf.write_to(outp)
        count += 1
