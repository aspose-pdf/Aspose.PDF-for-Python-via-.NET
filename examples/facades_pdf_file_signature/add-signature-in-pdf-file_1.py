# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesignature\add-signature-in-pdf-file
# Code fence language: python


from aspose.pdf.facades import (
    PdfFileSignature,
    PKCS7Detached,
    Rectangle
)

def add_signature_to_pdf():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "input.pdf"
    output_pdf = data_dir + "SignedOutput.pdf"
    cert_file = data_dir + "certificate.pfx"
    cert_password = "your_cert_password"

    # Create PdfFileSignature object
    pdf_sign = PdfFileSignature()

    # Bind PDF document (input & output)
    pdf_sign.bind_pdf(input_pdf, output_pdf)

    # Define signature placement (page 1, rectangle coordinates)
    sig_rect = Rectangle(100, 500, 300, 650)

    # Create PKCS7Detached signature using certificate
    signature = PKCS7Detached(cert_file, cert_password)

    # Optionally set signature appearance
    pdf_sign.signature_appearance = data_dir + "signature_image.jpg"

    # Sign the PDF
    pdf_sign.sign(1, cert_file, cert_password, "Reason for signing", "Contact", "Location", sig_rect, signature)

    # Save the signed document
    pdf_sign.save()
