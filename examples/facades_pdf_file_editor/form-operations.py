# Form Operations
# ─ Flatten Form Fields

from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Flatten Form Fields
def flatten_form_fields():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license
    set_license()

    # Open the PDF document
    with ap.Document(path.join(data_dir, "input.pdf")) as doc:
        # Create a FormEditor object
        form_editor = pdf_facades.FormEditor(doc)

        # Flatten the form fields
        form_editor.flatten()

        # Save the updated document
        form_editor.save(path.join(data_dir, "output.pdf"))

def run_all_examples(data_dir=None, license_path=None):
    """Run all form operations examples and report status .

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    examples = [
        ("Flatten Form Fields", flatten_form_fields)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}_in.pdf")
            func(input_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll form operations examples finished.")


if __name__ == "__main__":
    run_all_examples()            