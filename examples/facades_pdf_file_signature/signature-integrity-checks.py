from io import FileIO
import sys
from os import path
import aspose.pdf as ap 
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def check_signature_coverage(input_file_name, output_file_name):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(input_file_name)

    # Check signature coverage
    coverage = pdf_signature.check_signature_coverage()
    print(f"Signature Coverage: {coverage}%")

def validate_document_integrity(input_file_name, output_file_name):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(input_file_name)

    # Validate document integrity
    is_valid = pdf_signature.validate_document_integrity()
    print(f"Document Integrity Valid: {is_valid}")

def run_all_examples(data_dir=None, license_path=None):
    """Run all signature integrity check examples and report status.

    Args: 
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.  
    
    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Check Signature Coverage", check_signature_coverage),
        ("Validate Document Integrity", validate_document_integrity),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "signed_input.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll signature integrity check examples finished.")


if __name__ == "__main__":
    run_all_examples() 


