import sys
from os import path

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license  # noqa: E402

from _pdf_file_signature_helpers import (  # noqa: E402
    DEFAULT_SIGNED_PDF,
    create_pdf_file_signature,
    require_signature_name,
    write_stream_data,
)


def extract_signature_image(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_image = pdf_signature.extract_image(sign_name)
        write_stream_data(signature_image, outfile)
    finally:
        pdf_signature.close()


def extract_signature_certificate(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_certificate = pdf_signature.extract_certificate(sign_name)
        write_stream_data(signature_certificate, outfile)
    finally:
        pdf_signature.close()


def run_all_examples(data_dir=None, license_path=None):
    """Run all signature extraction examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Extract Signature Image", extract_signature_image, "signature-image.bin"),
        (
            "Extract Signature Certificate",
            extract_signature_certificate,
            "signature-certificate.cer",
        ),
    ]

    for name, func, output_name in examples:
        try:
            func(
                path.join(input_dir, DEFAULT_SIGNED_PDF),
                path.join(output_dir, output_name),
            )
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
