import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import initialize_data_dir, set_license

from _pdf_file_signature_helpers import (
    DEFAULT_INPUT_PDF,
    DEFAULT_CERTIFICATE_PASSWORD,
    configure_signature_certificate,
    create_pdf_file_signature,
)


def set_certificate_for_signing(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        certificate_path = configure_signature_certificate(
            pdf_signature,
            certificate_password=DEFAULT_CERTIFICATE_PASSWORD,
        )
        print(f"Certificate configured for signing: {certificate_path}")
    finally:
        pdf_signature.close()


def run_all_examples(data_dir=None, license_path=None):
    """Run all certificate configuration examples and report status."""
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    examples = [
        ("Set Certificate for Signing", set_certificate_for_signing),
    ]

    for name, func in examples:
        try:
            func(path.join(input_dir, DEFAULT_INPUT_PDF))
            print(f"Success: {name}")
        except Exception as e:
            print(f"Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
