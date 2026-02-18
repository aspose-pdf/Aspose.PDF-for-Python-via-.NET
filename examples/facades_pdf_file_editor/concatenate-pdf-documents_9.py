# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\concatenate-pdf-documents
# Code fence language: python


import aspose.pdf as pdf

def insert_blank_page():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Open the PDF document
    doc = pdf.Document(data_dir + "ConcatenatePdfFilesAndCreateTOC_out.pdf")

    # Insert a blank page at the beginning (page index 1)
    doc.pages.insert(1, pdf.Page(doc))

    # Save changes
    doc.save(data_dir + "ConcatenatePdfFilesAndCreateTOC_out.pdf")
