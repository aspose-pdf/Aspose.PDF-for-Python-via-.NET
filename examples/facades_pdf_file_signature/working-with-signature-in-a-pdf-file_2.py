# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffilesignature\working-with-signature-in-a-pdf-file
# Code fence language: python


from aspose.pdf.facades import PdfFileSignature

def extract_signature_image():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_security_signatures()

    signature = PdfFileSignature()
    signature.bind_pdf(data_dir + "ExtractingImage.pdf")

    if signature.contains_signature():
        for sig_name in signature.get_signature_names():
            image_stream = signature.extract_image(sig_name)
            if image_stream:
                with open(data_dir + "ExtractedImage_out.jpg", "wb") as fs:
                    fs.write(image_stream.read())
