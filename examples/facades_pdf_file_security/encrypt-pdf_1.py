# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesecurity\encrypt-pdf
# Code fence language: python


from aspose.pdf.facades import (
    PdfFileSecurity,
    DocumentPrivilege,
    KeySize,
    Algorithm
)

def encrypt_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "input.pdf"
    output_pdf = data_dir + "SampleEncrypted_out.pdf"

    file_security = PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(input_pdf)

    # Encrypt PDF using 256-bit AES encryption
    file_security.encrypt_file(
        "User_P@ssw0rd",          # user password
        "OwnerP@ssw0rd",          # owner password
        DocumentPrivilege.print, # permissions
        KeySize.x256,             # key size
        Algorithm.AES             # encryption algorithm
    )

    # Save encrypted PDF
    file_security.save(output_pdf)
