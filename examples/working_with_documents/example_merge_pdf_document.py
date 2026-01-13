import sys
import aspose.pdf as ap
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def merge_two_documents(infile1, infile2, outfile):
    """Merge two PDF documents into a single output document.

    This operation opens two input PDF files, appends all pages from the
    second document to the first, and saves the merged result to the
    specified output file.

    Args:
        infile1 (str): Path to the first input PDF document. Pages from
            this document will appear first in the merged output.
        infile2 (str): Path to the second input PDF document. All pages
            from this document are appended to ``infile1``.
        outfile (str): Path where the merged PDF document will be saved.

    Returns:
        None

    Examples:
        Merge two sample documents and save the result::

            from os import path
            from working_with_documents.example_merge_pdf_document import merge_two_documents

            input_dir = "sample_data/input"
            output_dir = "sample_data/output"

            infile1 = path.join(input_dir, "sample1.pdf")
            infile2 = path.join(input_dir, "sample3.pdf")
            outfile = path.join(output_dir, "sample_merge.pdf")

            merge_two_documents(infile1, infile2, outfile)
    """
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run Merge Document examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Merge two documents", merge_two_documents),
    ]

    for name, func in examples:
        try:
            input_file_name1 = path.join(input_dir, "sample1.pdf")
            input_file_name2 = path.join(input_dir, "sample3.pdf")
            output_file_name = path.join(output_dir, "sample_merge.pdf")
            func(input_file_name1, input_file_name2, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Merge Document examples finished.")


if __name__ == "__main__":
    run_all_examples()
