from facades import PDFDocument, PDFSignature, PDFCertificationLevel
from config import set_license, initialize_data_dir 
from os import path

def certify_pdf_with_mdp_signature(input_file_name, output_file_name):
    # Load PDF document
    pdf_document = PDFDocument(input_file_name)

    # Create PDF signature object
    pdf_signature = PDFSignature()

    # Set certificate for signing
    certificate_path = path.join(path.dirname(__file__), "certificate.pfx")
    certificate_password = "password"
    pdf_signature.set_certificate(certificate_path, certificate_password)
    print(f"Certificate set for signing: {certificate_path}")

    # Set MDP signature level to allow form filling and signing
    pdf_signature.set_certification_level(PDFCertificationLevel.FORM_FILLING_AND_SIGNING)

    # Sign the PDF document with MDP signature
    pdf_signature.sign(pdf_document)

    # Save the signed PDF document
    pdf_document.save(output_file_name)
    print(f"PDF certified and saved as: {output_file_name}")    

def apply_document_level_certification(input_file_name, output_file_name):
    # Load PDF document
    pdf_document = PDFDocument(input_file_name)

    # Create PDF signature object
    pdf_signature = PDFSignature()

    # Set certificate for signing
    certificate_path = path.join(path.dirname(__file__), "certificate.pfx")
    certificate_password = "password"
    pdf_signature.set_certificate(certificate_path, certificate_password)
    print(f"Certificate set for signing: {certificate_path}")

    # Set document-level certification with no changes allowed
    pdf_signature.set_certification_level(PDFCertificationLevel.NO_CHANGES_ALLOWED)

    # Sign the PDF document with document-level certification
    pdf_signature.sign(pdf_document)

    # Save the certified PDF document
    pdf_document.save(output_file_name)
    print(f"PDF certified with document-level certification and saved as: {output_file_name}")

def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF certification examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Certify PDF with MDP Signature", certify_pdf_with_mdp_signature),
        ("Apply Document-Level Certification", apply_document_level_certification)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "input.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll PDF certification examples finished.")


if __name__ == "__main__":
    run_all_examples()    



