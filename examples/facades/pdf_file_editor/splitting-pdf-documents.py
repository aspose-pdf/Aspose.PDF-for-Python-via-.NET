import sys
from os import path
import aspose.pdf.facades as pdf_facades

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import set_license, initialize_data_dir  # noqa: E402


# Split PDF from Beginning
def split_pdf_from_beginning(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_from_first(input_pdf_path, 3, output_pdf_path)


# Split PDF to End
def split_pdf_to_end(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_end(input_pdf_path, 2, output_pdf_path)


# Split PDF into Single Pages
def split_pdf_into_single_pages(input_pdf_path, output_pdf_path):
    pdf_file_editor = pdf_facades.PdfFileEditor()
    pdf_file_editor.split_to_pages(input_pdf_path, output_pdf_path)


def run_all_examples(data_dir=None, license_path=None):
    """Run all page splitting examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Split PDF from Beginning", split_pdf_from_beginning),
        ("Split PDF to End", split_pdf_to_end),
        ("Split PDF into Single Pages", split_pdf_into_single_pages),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, func.__name__ + ".pdf")
            if func.__name__ == "split_pdf_into_single_pages":
                output_file_name = path.join(output_dir, func.__name__ + "_%NUM%.pdf")
            else:
                output_file_name = path.join(output_dir, func.__name__ + ".pdf")
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll page splitting examples finished.")


if __name__ == "__main__":
    run_all_examples()
