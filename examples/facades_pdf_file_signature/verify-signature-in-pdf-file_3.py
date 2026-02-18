# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesignature\verify-signature-in-pdf-file
# Code fence language: python


from aspose.pdf.facades import PdfFileSignature

def is_pdf_signature_valid():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "signed_rsa.pdf"

    pdf_signature = PdfFileSignature()

    # Bind PDF document
    pdf_signature.bind_pdf(input_pdf)

    # Verify the specified signature
    if pdf_signature.verify_signature("Signature1"):
        print("Signature Verified")
