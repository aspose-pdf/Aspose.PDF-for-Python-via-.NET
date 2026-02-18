# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesignature\add-signature-in-pdf-file
# Code fence language: python


from aspose.pdf.facades import PdfFileSignature
from aspose.pdf.forms import PKCS1, SignatureCustomAppearance

def add_pdf_file_signature_field():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "input.pdf"
    output_pdf = data_dir + "DigitallySign_out.pdf"
    cert_file = data_dir + "rsa_cert.pfx"
    cert_password = "12345"

    pdf_signature = PdfFileSignature()

    # Bind PDF document
    pdf_signature.bind_pdf(input_pdf)

    # Create PKCS#1 signature with custom appearance
    signature = PKCS1(cert_file, cert_password)
    signature.reason = "Sign as Author"

    appearance = SignatureCustomAppearance()
    appearance.font_size = 6
    appearance.font_family_name = "Calibri"
    signature.custom_appearance = appearance

    # Sign PDF using a named signature field
    pdf_signature.sign("Signature1", signature)

    # Save signed PDF
    pdf_signature.save(output_pdf)
