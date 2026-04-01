import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import initialize_data_dir, set_license

from _pdf_file_signature_helpers import (
    DEFAULT_CERTIFIED_PDF,
    DEFAULT_SIGNED_PDF,
    create_pdf_file_signature,
    require_signature_name,
)


def get_signature_revision(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_revision = pdf_signature.get_revision(sign_name)
        print(f"Signature Revision for '{sign_name}': {signature_revision}")
    finally:
        pdf_signature.close()


def get_total_document_revisions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        total_revisions = pdf_signature.get_total_revision()
        print(f"Total Document Revisions: {total_revisions}")
    finally:
        pdf_signature.close()


def get_access_permissions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        access_permissions = pdf_signature.get_access_permissions()
        print(f"Access Permissions: {access_permissions}")
    finally:
        pdf_signature.close()


def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF revision and permissions examples and report status."""
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    examples = [
        ("Get Signature Revision", get_signature_revision, DEFAULT_SIGNED_PDF),
        ("Get Total Document Revisions", get_total_document_revisions, DEFAULT_SIGNED_PDF),
        ("Get Access Permissions", get_access_permissions, DEFAULT_CERTIFIED_PDF),
    ]

    for name, func, input_name in examples:
        try:
            func(path.join(input_dir, input_name))
            print(f"Success: {name}")
        except Exception as e:
            print(f"Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
