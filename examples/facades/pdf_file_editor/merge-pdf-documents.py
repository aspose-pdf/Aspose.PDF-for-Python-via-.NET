import sys
from os import path
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), '..', '..'))
from config import set_license, initialize_data_dir


def merge_pdf_documents(first_input_file, second_input_file, output_file):
    """Merge two PDF documents into a single output PDF.

    Args:
        first_input_file (str): Path to the first source PDF file.
        second_input_file (str): Path to the second source PDF file.
        output_file (str): Path where the merged PDF will be saved.
    """
    pdf_editor = ap.facades.PdfFileEditor()
    pdf_editor.concatenate([first_input_file, second_input_file], output_file)


def run_all_examples(data_dir=None, license_path=None):
    """Run all merge PDF document examples with status reporting."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Merge PDF Documents", merge_pdf_documents),
    ]

    for name, func in examples:
        try:
            first_input_file = path.join(input_dir, "sample1.pdf")
            second_input_file = path.join(input_dir, "sample2.pdf")
            output_file = path.join(output_dir, "merge_pdf_documents_out.pdf")
            func(first_input_file, second_input_file, output_file)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()