import sys
import aspose.pdf as ap
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def split_documents(infile, outdir):
    """Split a multi-page PDF document into separate single-page documents.

    Each page from the input PDF is saved as an individual PDF file in the
    specified output directory using the naming pattern ``Page_{n}.pdf``,
    where ``n`` is the 1-based page index.

    Args:
        infile (str): Path to the source multi-page PDF file to split.
        outdir (str): Directory where the single-page PDF files will be created.

    Returns:
        None

    Examples:
        Split ``sample_split.pdf`` into individual page files in the output directory:

        >>> from os import path
        >>> from examples.working_with_documents.example_split_pdf_document import split_documents
        >>> input_file = path.join("sample_data", "input", "sample_split.pdf")
        >>> output_dir = path.join("sample_data", "output")
        >>> split_documents(input_file, output_dir)
    """
    document = ap.Document(infile)
    page_count = 1
    for page in document.pages:
        with ap.Document(infile) as new_document:
            new_document.pages.add(page)
            new_document.save(path.join(outdir, f"Page_{page_count}.pdf"))
            page_count += 1


def run_all_examples(data_dir=None, license_path=None):
    """Run Split Document examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Split documents into single pages", split_documents),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "sample_split.pdf")
            func(input_file_name, output_dir)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Split Document examples finished.")


if __name__ == "__main__":
    run_all_examples()
