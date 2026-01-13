import sys
from os import path

import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir  # noqa: E402


def create_new_document(input_pdf, output_pdf):
    """Create a simple PDF with a single “Hello World!” page."""
    document = ap.Document()
    page = document.pages.add()
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    document.save(output_pdf)


def run_all_examples(data_dir=None, license_path=None):
    """Run PDF creation examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Create new document", create_new_document),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}.pdf")
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll PDF creation examples finished.")


if __name__ == "__main__":
    run_all_examples()
