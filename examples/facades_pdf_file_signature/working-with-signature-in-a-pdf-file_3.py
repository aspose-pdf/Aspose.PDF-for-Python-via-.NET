# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesignature\working-with-signature-in-a-pdf-file
# Code fence language: python


from aspose.pdf.facades import PdfFileSignature
from aspose.pdf.forms import PKCS1
from aspose.pdf import Rectangle

def suppress_location_and_reason():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_security_signatures()

    pdf_signature = PdfFileSignature()
    pdf_signature.bind_pdf(data_dir + "input.pdf")

    rect = Rectangle(10, 10, 300, 50)
    signature = PKCS1(data_dir + "rsa_cert.pfx", "12345")

    # Suppress reason and location by leaving empty strings
    pdf_signature.sign(
        1,
        "",  # empty reason
        "test01@aspose-pdf-demo.local",
        "",  # empty location
        True,
        rect,
        signature
    )
    pdf_signature.save(data_dir + "DigitallySign_out.pdf")
