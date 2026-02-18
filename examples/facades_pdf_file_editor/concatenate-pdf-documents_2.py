# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\concatenate-pdf-documents
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def concatenate_pdf_files_using_file_paths_copy_outlines_disabled():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Disable copying of outlines (bookmarks)
    pdf_editor.copy_outlines = False

    # Concatenate PDF files
    pdf_editor.concatenate(
        data_dir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled1.pdf",
        data_dir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled2.pdf",
        data_dir + "ConcatenateUsingPath_CopyOutlinesDisabled_out.pdf"
    )
