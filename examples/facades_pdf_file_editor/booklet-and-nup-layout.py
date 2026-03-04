# Booklet & N-Up Layout
#─ Create PDF Booklet
# ─ Create N-Up PDF Document

from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Create PDF Booklet
def create_pdf_booklet():
    # Initialize data directory path
    data_dir = initialize_data_dir()
    # Create BookletMaker object
    booklet_maker = pdf_facades.BookletMaker()
    # Set input PDF file
    booklet_maker.bind_pdf(data_dir + "input.pdf")
    # Set output PDF file
    booklet_maker.save(data_dir + "booklet_output.pdf")

# Create N-Up PDF Document
def create_nup_pdf_document():
    # Initialize data directory path
    data_dir = initialize_data_dir()
    # Create NUpMaker object
    nup_maker = pdf_facades.NUpMaker()
    # Set input PDF file
    nup_maker.bind_pdf(data_dir + "input.pdf")
    # Set output PDF file
    nup_maker.save(data_dir + "nup_output.pdf")

def run_all_examples(data_dir=None, license_path=None):
    """Run all booklet and N-Up layout examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [

        ("Create PDF Booklet", create_pdf_booklet, "booklet_output.pdf"),
        ("Create N-Up PDF Document", create_nup_pdf_document, "nup_output.pdf")
    ]

    for name, func, data_file_name in examples:
        try:
            if (func.__name__ == "create_pdf_booklet") or (func.__name__ == "create_nup_pdf_document"):
                input_file_name = path.join(input_dir, "input.pdf")
            else:
                input_file_name = path.join(input_dir, "f")
            output_file_name = path.join(output_dir, data_file_name)
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll booklet and N-Up layout examples finished.")


if __name__ == "__main__":
    run_all_examples()          