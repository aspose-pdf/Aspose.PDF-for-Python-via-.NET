# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesignature\remove-signature-from-pdf-file
# Code fence language: python


from aspose.pdf.facades import PdfFileSignature

def remove_signature():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "signed_rsa.pdf"
    output_pdf = data_dir + "RemoveSignature_out.pdf"

    pdf_signature = PdfFileSignature()

    # Bind PDF document
    pdf_signature.bind_pdf(input_pdf)

    # Get list of signature names
    signature_names = pdf_signature.get_sign_names()

    # Remove all signatures
    for name in signature_names:
        print(f"Removed {name}")
        pdf_signature.remove_signature(name)

    # Save PDF without signatures
    pdf_signature.save(output_pdf)
