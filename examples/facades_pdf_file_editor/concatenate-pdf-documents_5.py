# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\concatenate-pdf-documents
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor
from io import BytesIO

def concatenate_array_of_pdf_files_using_streams():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()
    
    document1_path = data_dir + "Concatenate1.pdf"
    document2_path = data_dir + "Concatenate2.pdf"
    result_pdf_path = data_dir + "ConcatenateArrayOfPdfUsingStreams_out.pdf"

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Open PDF files as byte streams
    with open(document1_path, "rb") as f1, open(document2_path, "rb") as f2:
        stream1 = BytesIO(f1.read())
        stream2 = BytesIO(f2.read())

        # Array (list) of input streams
        input_streams = [stream1, stream2]

        # Output stream
        with BytesIO() as output_stream:
            # Concatenate the input streams
            pdf_editor.concatenate(input_streams, output_stream)

            # Save the output stream to a file
            with open(result_pdf_path, "wb") as out_file:
                out_file.write(output_stream.getvalue())
