import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir

# Concatenate or Merge PDF Files
def concatenate_pdf_files():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license for Aspose.PDF
    set_license()

    # Define the paths to the PDF documents to be merged
    pdf_files_to_merge = [
        path.join(data_dir, "input.pdf"),
        path.join(data_dir, "additional.pdf"),
    ]

    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Merge the specified PDF documents into a single PDF document
    output_path = path.join(data_dir, "merged_output.pdf")
    pdf_editor.merge(pdf_files_to_merge, output_path)
    print(f"Merged PDF saved to: {output_path}")


def run_all_examples(data_dir=None, license_path=None):
    """Run all page management examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Concatenate PDF Files", concatenate_pdf_files),
    ]

    for name, func in examples:
        input_file_name = path.join(input_dir, func.__name__ + ".pdf")
        output_file_name = path.join(output_dir, func.__name__ + ".pdf")
        try:
            if (
                func.__name__ == "insert_pages_into_pdf"
                or func.__name__ == "append_pages_to_pdf"
            ):
                func(
                    input_file_name,
                    path.join(input_dir, "sample_data.pdf"),
                    output_file_name,
                )
            else:
                func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll page management examples finished.")


if __name__ == "__main__":
    run_all_examples()
