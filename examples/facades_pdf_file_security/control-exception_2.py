# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesecurity\control-exception
# Code fence language: python


from aspose.pdf.facades import PdfFileSecurity

def control_exception_pdf_file2():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    pdf_path = data_dir + "sample_encrypted.pdf"
    output_path = data_dir + "SampleDecrtypted_out.pdf"

    file_security = PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(pdf_path)

    # Allow exceptions (raise errors automatically)
    file_security.allow_exceptions = True

    try:
        # Attempt to decrypt PDF document
        file_security.decrypt_file("IncorrectPassword")
    except Exception as ex:
        print("Something wrong...")
        print(f"Exception: {ex}")

    # Save PDF document
    file_security.save(output_path)
