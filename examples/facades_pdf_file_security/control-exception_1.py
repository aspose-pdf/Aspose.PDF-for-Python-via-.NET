# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesecurity\control-exception
# Code fence language: python


from aspose.pdf.facades import PdfFileSecurity

def control_exception_pdf_file():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    pdf_path = data_dir + "sample_encrypted.pdf"
    output_path = data_dir + "SampleDecrtypted_out.pdf"

    file_security = PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(pdf_path)

    # Disallow exceptions (handle errors manually)
    file_security.allow_exceptions = False

    # Attempt to decrypt with an incorrect password
    if not file_security.decrypt_file("IncorrectPassword"):
        print("Something wrong...")
        print(f"Last exception: {file_security.last_exception.message}")

    # Save PDF document (will save only if decryption succeeds)
    file_security.save(output_path)
