# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesecurity\change-password
# Code fence language: python


from aspose.pdf.facades import PdfFileInfo, PdfFileSecurity, DocumentPrivilege, KeySize

def change_password():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    pdf_path = data_dir + "sample_encrypted.pdf"
    output_path = data_dir + "sample_encrypted1.pdf"

    # Check if the PDF is encrypted
    pdf_info = PdfFileInfo(pdf_path)
    if pdf_info.is_encrypted:
        file_security = PdfFileSecurity()

        # Bind PDF document
        file_security.bind_pdf(pdf_path)

        # Change password
        file_security.change_password(
            "OwnerP@ssw0rd",        # current owner password
            "Pa$$w0rd1",            # new user password
            "Pa$$w0rd2",            # new owner password
            DocumentPrivilege.print,
            KeySize.x256
        )

        # Save updated PDF
        file_security.save(output_path)
