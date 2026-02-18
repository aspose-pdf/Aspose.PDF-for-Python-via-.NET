# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\concatenate-pdf-documents
# Code fence language: python


import os
from aspose.pdf.facades import PdfFileEditor

def concatenate_pdf_files_in_folder():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Retrieve all PDF files in the directory
    file_entries = [
        os.path.join(data_dir, file_name)
        for file_name in os.listdir(data_dir)
        if file_name.lower().endswith(".pdf")
    ]

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Concatenate all PDF files into a single output file
    pdf_editor.concatenate(
        file_entries,
        data_dir + "ConcatenatePdfFilesInFolder_out.pdf"
    )
