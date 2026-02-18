# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\concatenate-pdf-documents
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor

def concatenate_pdf_forms_and_keep_fields_unique():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Set input and output file paths
    input_file1 = data_dir + "ConcatenatePdfFormsAndKeepFieldsUnique1.pdf"
    input_file2 = data_dir + "ConcatenatePdfFormsAndKeepFieldsUnique2.pdf"
    out_file = data_dir + "ConcatenatePDFForms_out.pdf"

    # Create PdfFileEditor object
    file_editor = PdfFileEditor()

    # Ensure unique field IDs for all form fields
    file_editor.keep_fields_unique = True

    # Format of the suffix added to field names to make them unique
    file_editor.unique_suffix = "_%NUM%"

    # Concatenate the PDF forms into a single output file
    file_editor.concatenate(input_file1, input_file2, out_file)
