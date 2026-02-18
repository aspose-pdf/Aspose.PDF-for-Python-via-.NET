# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\concatenate-pdf-documents
# Code fence language: python


import os
from aspose.pdf.facades import PdfFileEditor

def concatenating_all_pdf_files_in_particular_folder():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Retrieve all PDF files in the directory
    file_entries = [
        os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.lower().endswith(".pdf")
    ]

    result_pdf_path = os.path.join(data_dir, "ConcatenatingAllPdfFilesInParticularFolder_out.pdf")

    # Instantiate PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Concatenate all input files into a single output file
    pdf_editor.concatenate(file_entries, result_pdf_path)
