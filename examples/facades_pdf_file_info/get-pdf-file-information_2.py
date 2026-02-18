# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileinfo\get-pdf-file-information
# Code fence language: python


from aspose.pdf.facades import PdfFileInfo

def get_meta_info():
    data_dir = RunExamples.get_data_dir_aspose_pdf()

    # Create PdfFileInfo object
    pdf_info = PdfFileInfo(data_dir + "SetMetaInfo_out.pdf")

    # Retrieve all custom metadata (header dictionary)
    meta_info = pdf_info.header

    # Enumerate and display all custom attributes
    for key, value in meta_info.items():
        print(f"{key} {value}")

    # Retrieve and display a specific custom attribute
    print("Reviewer:", pdf_info.get_meta_info("Reviewer"))
