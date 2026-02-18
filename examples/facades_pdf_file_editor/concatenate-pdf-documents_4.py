# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\concatenate-pdf-documents
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def concatenate_array_of_pdf_files_using_file_paths():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # List of PDF files to concatenate
    files_array = [
        data_dir + "Concatenate1.pdf",
        data_dir + "Concatenate2.pdf"
    ]

    # Concatenate the array of PDF files
    pdf_editor.concatenate(files_array, data_dir + "ConcatenateArrayOfPdfFilesUsingFilePaths_out.pdf")
