import sys
import aspose.pdf as ap
from os import path

sys.path.append(path.join(path.dirname(__file__), '../..'))

from config import set_license, initialize_data_dir


def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)


def run_all_examples(data_dir=None, license_path=None):
    """Run page stamps examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("add_page_stamp", add_page_stamp),
    ]

    input_file_name = path.join(input_dir, "sample.pdf")
    page_stamp_file = path.join(input_dir, "page_stamp.pdf")

    for name, func in examples:
        output_file_name = path.join(output_dir, f"{name}_out.pdf")
        try:
            func(input_file_name, page_stamp_file, output_file_name)
            print(f"✅ {name} completed. Output: {output_file_name}")
        except Exception as e:
            print(f"❌ {name} failed: {e}")

    print(f"\nAll page stamps examples finished. Check output in {output_dir}")


# Main execution
if __name__ == "__main__":
    run_all_examples()