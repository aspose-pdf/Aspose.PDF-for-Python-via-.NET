from facades import PDFDocument, PDFSignature
from config import set_license, initialize_data_dir
from os import name, name, path

def verify_pdf_signature(input_file_name, output_file_name):
    # Load PDF document
    pdf_document = PDFDocument(input_file_name)

    # Create PDF signature object
    pdf_signature = PDFSignature()

    # Verify PDF signature
    is_valid = pdf_signature.verify_signature(pdf_document)
    print(f"Is the PDF signature valid? {is_valid}")

def check_pdf_contains_signatures(input_file_name, output_file_name):
    # Load PDF document
    pdf_document = PDFDocument(input_file_name)

    # Create PDF signature object
    pdf_signature = PDFSignature()

    # Check if PDF contains signatures
    contains_signatures = pdf_signature.contains_signatures(pdf_document)
    print(f"Does the PDF contain signatures? {contains_signatures}")

def run_all_examples(data_dir=None, license_path=None):
    """Run all signature verification examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Verify PDF Signature", verify_pdf_signature),
        ("Check if PDF Contains Signatures", check_pdf_contains_signatures)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "input.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll signature verification examples finished.")


if __name__ == "__main__":
    run_all_examples()     
