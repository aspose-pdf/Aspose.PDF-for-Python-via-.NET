import aspose.pdf as ap
import io
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def open_document_from_file(infile):

    # Open document
    document = ap.Document(infile)
    print("Pages: " + str(len(document.pages)))


def open_document_from_stream(infile):
    with io.FileIO(infile, "r") as stream:
        # Open document
        document = ap.Document(stream)
        print("Pages: " + str(len(document.pages)))


def open_document_encrypted(infile):
    password = "P@ssw0rd"
    # Open document
    document = ap.Document(infile, password)
    print("Pages: " + str(len(document.pages)))


def run_all_examples(data_dir=None, license_path=None):
    """Run Open Document examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("open_document_from_file", open_document_from_file),
        ("open_document_from_stream", open_document_from_stream),
        ("open_document_encrypted", open_document_encrypted),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}.pdf")
            func(input_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Open Document examples finished.")


if __name__ == "__main__":
    run_all_examples()
