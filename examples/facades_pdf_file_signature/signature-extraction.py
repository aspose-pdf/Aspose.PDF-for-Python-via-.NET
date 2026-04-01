from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def extract_signature_image(input_file_name, output_file_name):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(input_file_name)

    # Extract signature image
    signature_image = pdf_signature.extract_signature_image(1)
    with FileIO(output_file_name, "wb") as output_file:
        output_file.write(signature_image)
    print(f"Signature image extracted to: {output_file_name}")

def extract_signature_certificate(input_file_name, output_file_name):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(input_file_name)

    # Extract signature certificate
    signature_certificate = pdf_signature.extract_signature_certificate(1)
    with FileIO(output_file_name, "wb") as output_file:
        output_file.write(signature_certificate)
    print(f"Signature certificate extracted to: {output_file_name}")

def run_all_examples(data_dir=None, license_path=None):
    """Run all signature extraction examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Extract Signature Image", extract_signature_image),
        ("Extract Signature Certificate", extract_signature_certificate),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "input.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll signature extraction examples finished.")


if __name__ == "__main__":
    run_all_examples() 



