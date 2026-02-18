# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesignature\working-with-signature-in-a-pdf-file
# Code fence language: python


from aspose.pdf.facades import PdfFileSignature

def extract_signature_info():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_security_signatures()

    pdf_signature = PdfFileSignature()
    pdf_signature.bind_pdf(data_dir + "signed_rsa.pdf")

    signature_names = pdf_signature.get_signature_names()
    if signature_names:
        sig_name = signature_names[0]

        # Extract certificate as a stream
        cer_stream = pdf_signature.extract_certificate(sig_name)
        if cer_stream is not None:
            with open(data_dir + "extracted_cert.pfx", "wb") as fs:
                fs.write(cer_stream.read())
