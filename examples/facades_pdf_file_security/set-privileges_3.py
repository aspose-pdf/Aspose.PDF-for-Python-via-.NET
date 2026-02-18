# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesecurity\set-privileges
# Code fence language: python


from aspose.pdf.facades import PdfFileSignature

def remove_extended_rights():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_security_signatures()

    input_pdf = data_dir + "DigitallySign.pdf"
    output_pdf = data_dir + "RemoveRights_out.pdf"

    pdf_sign = PdfFileSignature()

    # Bind PDF document
    pdf_sign.bind_pdf(input_pdf)

    # Check and remove usage rights if present
    if pdf_sign.contains_usage_rights():
        pdf_sign.remove_usage_rights()

    # Save updated PDF document
    pdf_sign.document.save(output_pdf)
