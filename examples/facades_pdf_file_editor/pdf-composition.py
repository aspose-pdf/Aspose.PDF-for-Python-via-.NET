# PDF Composition
# └─ Append PDFs

from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Append PDF
def append_pdf():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license
    set_license()

    # Create PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Append PDF file
    pdf_editor.append(
        path.join(data_dir, "input1.pdf"),
        path.join(data_dir, "input2.pdf"),
        path.join(data_dir, "output.pdf"),
    )

def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF composition examples and report status .

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    examples = [
        ("Append PDF", append_pdf)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}_in.pdf")
            func(input_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll PDF composition examples finished.")


if __name__ == "__main__":
    run_all_examples()    