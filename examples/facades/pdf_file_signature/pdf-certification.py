import aspose.pdf as ap
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
    create_pdf_file_signature,    
    create_doc_mdp_signature,
    create_pdf_file_signature,
    create_signature_rectangle,
)

def certify_pdf_with_mdp_signature(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            ap.forms.DocMDPAccessPermissions.FILLING_IN_FORMS,
            reason="Certified for form filling and signing",
        )
        pdf_signature.certify(
            1,
            "Certified for form filling and signing",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()


def apply_document_level_certification(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            ap.forms.DocMDPAccessPermissions.NO_CHANGES,
            reason="Certified with no further changes allowed",
        )
        pdf_signature.certify(
            1,
            "Certified with no further changes allowed",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()


def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF certification examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Set Certificate for Signing", set_certificate_for_signing),
        ("Certify PDF with MDP Signature", certify_pdf_with_mdp_signature),
        ("Apply Document-Level Certification", apply_document_level_certification),
    ]

    for name, func in examples:
        try:
            func(
                path.join(input_dir, DEFAULT_INPUT_PDF),
                path.join(output_dir, f"{func.__name__}.pdf"),
            )
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
