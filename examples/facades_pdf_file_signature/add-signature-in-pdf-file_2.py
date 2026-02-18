# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesignature\add-signature-in-pdf-file
# Code fence language: python


from aspose.pdf.facades import PdfFileSignature
from aspose.pdf.forms import PKCS1
from aspose.pdf import Rectangle

def add_two_signatures():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "input.pdf"
    cert_file = data_dir + "rsa_cert.pfx"
    cert_password = "12345"

    # Create PdfFileSignature object
    pdf_signature = PdfFileSignature()

    # =========================
    # First signature
    # =========================
    pdf_signature.bind_pdf(input_pdf)

    rect1 = Rectangle(10, 10, 300, 50)
    signature1 = PKCS1(cert_file, cert_password)

    pdf_signature.sign(
        1,
        "I'm document author",
        "test@aspose-pdf-demo.local",
        "Aspose Pdf Demo, Australia",
        True,
        rect1,
        signature1
    )

    first_signed_pdf = data_dir + "DigitallySign_out.pdf"
    pdf_signature.save(first_signed_pdf)

    # =========================
    # Second signature
    # =========================
    pdf_signature.bind_pdf(first_signed_pdf)

    rect2 = Rectangle(10, 10, 300, 50)
    signature2 = PKCS1(cert_file, cert_password)

    pdf_signature.sign(
        2,
        "I'm document reviewer",
        "test02@aspose-pdf-demo.local",
        "Aspose Pdf Demo, Australia",
        True,
        rect2,
        signature2
    )

    pdf_signature.save(data_dir + "DigitallySign2_out.pdf")
