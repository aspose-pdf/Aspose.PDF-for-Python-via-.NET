# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\concatenate-pdf-documents
# Code fence language: python


from aspose.pdf.facades import PdfFileEditor
from io import BytesIO

def concatenate_multiple_pdf_files_using_memory_streams():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()
    
    document1_path = data_dir + "ConcatenateMultiplePdfFilesUsingMemoryStreams1.pdf"
    document2_path = data_dir + "ConcatenateMultiplePdfFilesUsingMemoryStreams2.pdf"
    result_pdf_path = data_dir + "concatenated_out.pdf"

    # Read PDF files into memory
    with open(document1_path, "rb") as f1, open(document2_path, "rb") as f2:
        buffer1 = f1.read()
        buffer2 = f2.read()

    # Convert byte arrays into memory streams
    with BytesIO(buffer1) as stream1, BytesIO(buffer2) as stream2, BytesIO() as output_stream:
        # Create PdfFileEditor object
        pdf_editor = PdfFileEditor()

        # Concatenate both input streams and save to output stream
        pdf_editor.concatenate(stream1, stream2, output_stream)

        # Write the output stream to a file
        with open(result_pdf_path, "wb") as out_file:
            out_file.write(output_stream.getvalue())
