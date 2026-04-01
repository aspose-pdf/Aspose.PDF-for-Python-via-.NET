from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def set_certificate_for_signing(input_file_name):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(input_file_name)

    # Set certificate for signing
    certificate_path = path.join(path.dirname(__file__), "certificate.pfx")
    certificate_password = "password"
    pdf_signature.set_certificate(certificate_path, certificate_password)
    print(f"Certificate set for signing: {certificate_path}")

def run_all_examples(data_dir=None, license_path=None):
    """Run all certificate configuration examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Set Certificate for Signing", set_certificate_for_signing),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "input.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll certificate configuration examples finished.")


if __name__ == "__main__":
    run_all_examples() 

