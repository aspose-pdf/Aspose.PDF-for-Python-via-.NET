# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesignature\add-signature-in-pdf-file
# Code fence language: python


from aspose.pdf.facades import PdfFileSignature
from aspose.pdf.forms import PKCS1, SignatureCustomAppearance

def add_pdf_file_signature_field2():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "input.pdf"
    cert_file = data_dir + "rsa_cert.pfx"
    cert_password = "12345"

    pdf_signature = PdfFileSignature()

    # =========================
    # First signature field
    # =========================
    pdf_signature.bind_pdf(input_pdf)

    signature1 = PKCS1(cert_file, cert_password)
    signature1.reason = "Sign as Author"

    appearance1 = SignatureCustomAppearance()
    appearance1.font_size = 6
    signature1.custom_appearance = appearance1

    pdf_signature.sign("Signature1", signature1)
    first_signed_pdf = data_dir + "DigitallySign_out.pdf"
    pdf_signature.save(first_signed_pdf)

    # =========================
    # Second signature field
    # =========================
    pdf_signature.bind_pdf(first_signed_pdf)

    signature2 = PKCS1(cert_file, cert_password)
    signature2.reason = "Sign as Reviewer"

    appearance2 = SignatureCustomAppearance()
    appearance2.font_size = 6
    signature2.custom_appearance = appearance2

    pdf_signature.sign("Signature2", signature2)
    pdf_signature.save(data_dir + "DigitallySign2_out.pdf")
