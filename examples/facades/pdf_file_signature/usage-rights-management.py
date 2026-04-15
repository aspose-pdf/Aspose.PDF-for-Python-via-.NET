import sys
from os import path

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license

from _pdf_file_signature_helpers import (
    DEFAULT_SIGNED_PDF,
    create_pdf_file_signature,
)


def remove_usage_rights(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
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
        ("Remove Usage Rights", remove_usage_rights),
    ]

    for name, func in examples:
        try:
            func(
                path.join(input_dir, DEFAULT_SIGNED_PDF),
                path.join(output_dir, f"{func.__name__}.pdf"),
            )
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
