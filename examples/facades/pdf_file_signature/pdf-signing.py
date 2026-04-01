import aspose.pdf.facades as pdf_facades
import sys
from os import path

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license

from _pdf_file_signature_helpers import (
    DEFAULT_INPUT_PDF,
    DEFAULT_SIGNATURE_NAME,
    configure_signature_certificate,
    create_custom_signature_appearance,
    create_pdf_file_signature,
    create_pkcs7_signature,
    create_signature_rectangle,
)


def sign_pdf_with_basic_parameters(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        configure_signature_certificate(pdf_signature)
        pdf_signature.sign(
            1,
            "Document approval",
            "qa@example.com",
            "New York, USA",
            False,
            create_signature_rectangle(),
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()


def sign_pdf_with_certificate_object(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature()
        pdf_signature.sign(1, False, create_signature_rectangle(), signature)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()


def sign_pdf_with_named_signature(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(reason="Approved by signing workflow")
        pdf_signature.sign(
            1,
            DEFAULT_SIGNATURE_NAME,
            "Approved by signing workflow",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()


def apply_visible_signature(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(reason="Visible approval signature")
        signature.custom_appearance = create_custom_signature_appearance()
        pdf_signature.sign(
            1,
            "Visible approval signature",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()


def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF signing examples and report status."""
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
            if (func.__name__ == "sign_pdf_with_named_signature"):
                func(
                    path.join(input_dir, "sample_field.pdf"),
                    path.join(output_dir, f"{func.__name__}.pdf"),
                )            
            else:
                func(
                    path.join(input_dir, DEFAULT_INPUT_PDF),
                    path.join(output_dir, f"{func.__name__}.pdf"),
                )
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
