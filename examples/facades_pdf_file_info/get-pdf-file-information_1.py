# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileinfo\get-pdf-file-information
# Code fence language: python


from aspose.pdf.facades import PdfFileInfo

def get_pdf_info():
    data_dir = RunExamples.get_data_dir_aspose_pdf()

    # Open PDF document
    pdf_info = PdfFileInfo(data_dir + "sample.pdf")

    # Get and display PDF information
    print(f"Subject: {pdf_info.subject}")
    print(f"Title: {pdf_info.title}")
    print(f"Keywords: {pdf_info.keywords}")
    print(f"Creator: {pdf_info.creator}")
    print(f"Creation Date: {pdf_info.creation_date}")
    print(f"Modification Date: {pdf_info.mod_date}")

    # Check PDF status
    print(f"Is Valid PDF: {pdf_info.is_pdf_file}")
    print(f"Is Encrypted: {pdf_info.is_encrypted}")

    # Get dimensions of the first page (1-based index)
    print(f"Page width: {pdf_info.get_page_width(1)}")
    print(f"Page height: {pdf_info.get_page_height(1)}")
