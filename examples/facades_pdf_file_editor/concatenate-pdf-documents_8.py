# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\concatenate-pdf-documents
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor
from io import BytesIO

def concatenate_pdf_files():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Set input and output file paths
    input_file1 = data_dir + "ConcatenateInput1.pdf"
    input_file2 = data_dir + "ConcatenateInput2.pdf"
    out_file = data_dir + "ConcatenatePdfFilesAndCreateTOC_out.pdf"

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Open PDF files as byte streams
    with open(input_file1, "rb") as f1, open(input_file2, "rb") as f2:
        stream1 = BytesIO(f1.read())
        stream2 = BytesIO(f2.read())

        # Concatenate streams into an output stream
        with BytesIO() as output_stream:
            pdf_editor.concatenate(stream1, stream2, output_stream)

            # Save the output stream to a file
            with open(out_file, "wb") as out_file_stream:
                out_file_stream.write(output_stream.getvalue())
