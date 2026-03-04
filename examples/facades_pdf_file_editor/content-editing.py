# Content Editing
#└─ Replace Text

from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Replace Text
def replace_text():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license for Aspose.PDF
    set_license()

    # Open the PDF document
    with ap.Document(path.join(data_dir, "input.pdf")) as doc:
        # Create a TextFragmentAbsorber object to find text fragments
        absorber = ap.TextFragmentAbsorber("old text")

        # Accept the absorber for the document
        doc.pages.accept(absorber)

        # Get the collection of text fragments
        text_fragments = absorber.text_fragments

        # Loop through the text fragments and replace the text
        for text_fragment in text_fragments:
            text_fragment.text = "new text"

        # Save the modified document
        doc.save(path.join(data_dir, "output.pdf"))

def run_all_examples(data_dir=None, license_path=None):
    """Run all content editing examples and report status .

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    examples = [
        ("Replace Text", replace_text)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}_in.pdf")
            func(input_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll content editing examples finished.")


if __name__ == "__main__":
    run_all_examples()          