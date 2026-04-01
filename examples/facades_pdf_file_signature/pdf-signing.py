from io import FileIO
import sys  
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

from examples.config import initialize_data_dir, set_license   

sys.path.append(path.join(path.dirname(__file__), ".."))

from certificate_configuration import set_certificate_for_signing

def sign_pdf_with_basic_parameters(input_file_name, output_file_name):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(input_file_name)

    # Set certificate for signing
    set_certificate_for_signing(input_file_name)

    # Sign PDF with basic parameters
    signature_reason = "Document approval"
    signature_location = "New York, USA"
    pdf_signature.sign(output_file_name, signature_reason, signature_location)
    print(f"PDF signed successfully: {output_file_name}")

def sign_pdf_with_certificate_object(input_file_name, output_file_name):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(input_file_name)

    # Set certificate for signing
    set_certificate_for_signing(input_file_name)

    # Sign PDF with certificate object
    signature_reason = "Document approval"
    signature_location = "New York, USA"
    pdf_signature.sign(output_file_name, signature_reason, signature_location)
    print(f"PDF signed successfully: {output_file_name}")

def sign_pdf_with_named_signature(input_file_name, output_file_name):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(input_file_name)

    # Set certificate for signing
    set_certificate_for_signing(input_file_name)

    # Sign PDF with named signature
    signature_reason = "Document approval"
    signature_location = "New York, USA"
    signature_name = "MySignature"
    pdf_signature.sign(output_file_name, signature_reason, signature_location, signature_name)
    print(f"PDF signed successfully with named signature: {output_file_name}")

def apply_visible_signature(input_file_name, output_file_name):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(input_file_name)

    # Set certificate for signing
    set_certificate_for_signing(input_file_name)

    # Apply visible signature
    signature_reason = "Document approval"
    signature_location = "New York, USA"
    signature_name = "VisibleSignature"
    page_number = 1
    rectangle = ap.Rectangle(100, 100, 200, 150)
    pdf_signature.sign(output_file_name, signature_reason, signature_location, signature_name, page_number, rectangle)
    print(f"PDF signed successfully with visible signature: {output_file_name}")

def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF signing examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Sign PDF with Basic Parameters", sign_pdf_with_basic_parameters),
        ("Sign PDF with Certificate Object", sign_pdf_with_certificate_object),
        ("Sign PDF with Named Signature", sign_pdf_with_named_signature),
        ("Apply Visible Signature", apply_visible_signature),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "input.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll PDF signing examples finished.")


if __name__ == "__main__":
    run_all_examples() 



