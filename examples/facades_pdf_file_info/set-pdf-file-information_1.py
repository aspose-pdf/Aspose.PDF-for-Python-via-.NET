# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileinfo\set-pdf-file-information
# Code fence language: python


from aspose.pdf.facades import PdfFileInfo

def set_pdf_info():
    data_dir = RunExamples.get_data_dir_aspose_pdf()

    # Create PdfFileInfo object to work with PDF metadata
    pdf_info = PdfFileInfo(data_dir + "sample.pdf")

    # Set PDF information
    pdf_info.author = "Aspose"
    pdf_info.title = "Hello World!"
    pdf_info.keywords = "Peace and Development"
    pdf_info.creator = "Aspose"

    # Save the PDF with updated information
    pdf_info.save_new_info(data_dir + "SetFileInfo_out.pdf")
