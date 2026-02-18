# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesecurity\decrypt-pdf
# Code fence language: python


from aspose.pdf.facades import PdfFileInfo, PdfFileSecurity

def decrypt_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "sample_encrypted.pdf"
    output_pdf = data_dir + "SampleDecrtypted_out.pdf"

    # Check whether the PDF is encrypted
    pdf_info = PdfFileInfo(input_pdf)
    if pdf_info.is_encrypted:
        file_security = PdfFileSecurity()

        # Bind PDF document
        file_security.bind_pdf(input_pdf)

        # Decrypt PDF document using password
        file_security.decrypt_file("P@ssw0rd")

        # Save decrypted PDF
        file_security.save(output_pdf)
