import sys
from os import path

import aspose.pdf.facades as pdf_facades

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license  # noqa: E402


def check_usage_rights(infile, outfile):
    """Check whether the input PDF contains usage rights."""
    pdf_signature = pdf_facades.PdfFileSignature()
    try:
        pdf_signature.bind_pdf(infile)
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights: {had_usage_rights}")
    finally:
        pdf_signature.close()


def remove_usage_rights(infile, outfile):
    """Remove usage rights from the input PDF and save the result."""
    pdf_signature = pdf_facades.PdfFileSignature()
    try:
        pdf_signature.bind_pdf(infile)
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights before removal: {had_usage_rights}")
        pdf_signature.remove_usage_rights()
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()


def run_all_examples(data_dir=None, license_path=None):
    """Run all usage rights management examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Check Usage Rights", check_usage_rights),
        ("Remove Usage Rights", remove_usage_rights),
    ]

    for name, func in examples:
        try:
            func(
                path.join(input_dir, "signed.pdf"),
                path.join(output_dir, f"{func.__name__}.pdf"),
            )
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
