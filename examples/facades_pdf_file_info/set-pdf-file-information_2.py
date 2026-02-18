# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileinfo\set-pdf-file-information
# Code fence language: python


from aspose.pdf.facades import PdfFileInfo

def set_meta_info():
    data_dir = RunExamples.get_data_dir_aspose_pdf()

    # Create PdfFileInfo object
    pdf_info = PdfFileInfo(data_dir + "sample.pdf")

    # Set a custom metadata attribute
    pdf_info.set_meta_info("Reviewer", "Aspose.PDF user")

    # Save the updated PDF
    pdf_info.save_new_info(data_dir + "SetMetaInfo_out.pdf")
