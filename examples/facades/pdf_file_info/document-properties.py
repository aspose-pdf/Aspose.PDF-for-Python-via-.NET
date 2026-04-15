import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import set_license, initialize_data_dir

def get_pdf_version(input_file_name):
    
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)
    version = pdf_metadata.get_pdf_version()
    print(f"\nPDF Version: {version}")

def get_document_privileges(input_file_name):
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)

    privileges = pdf_metadata.get_document_privilege()

    print("Document Privileges:")
    print(f"  Can Print: {privileges.allow_print}")
    print(f"  Can Degraded Print: {privileges.allow_degraded_printing}")
    print(f"  Can Copy: {privileges.allow_copy}")
    print(f"  Can Modify Contents: {privileges.allow_modify_contents}")
    print(f"  Can Modify Annotations: {privileges.allow_modify_annotations}")
    print(f"  Can Fill In: {privileges.allow_fill_in}")
    print(f"  Can Screen Readers: {privileges.allow_screen_readers}")
    print(f"  Can Assembly: {privileges.allow_assembly}")


def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF metadata examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Get PDF Version", get_pdf_version),
        ("Get Document Privileges", get_document_privileges)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "sample.pdf")            
            func(input_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll PDF metadata examples finished.\n")

if __name__ == "__main__":
    run_all_examples()  