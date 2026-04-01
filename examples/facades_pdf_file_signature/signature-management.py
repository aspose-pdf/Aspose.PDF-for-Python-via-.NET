import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import initialize_data_dir, set_license

from _pdf_file_signature_helpers import (
    DEFAULT_SIGNED_PDF,
    create_pdf_file_signature,
    require_signature_name,
)


def remove_signature_from_pdf(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()


def remove_signature_with_field_cleanup(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name, True)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()


def run_all_examples(data_dir=None, license_path=None):
    """Run all signature management examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Remove Signature from PDF", remove_signature_from_pdf),
        ("Remove Signature with Field Cleanup", remove_signature_with_field_cleanup),
    ]

    for name, func in examples:
        try:
            func(
                path.join(input_dir, DEFAULT_SIGNED_PDF),
                path.join(output_dir, f"{func.__name__}.pdf"),
            )
            print(f"Success: {name}")
        except Exception as e:
            print(f"Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
