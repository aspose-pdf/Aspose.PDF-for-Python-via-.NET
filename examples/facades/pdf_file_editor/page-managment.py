import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)
from config import set_license, initialize_data_dir


# Extract Pages from PDF
def extract_pages_from_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page numbers to be extracted (1-based index)
    pages_to_extract = [1, 4, 3]

    # Extract the specified pages from the PDF document and save to a new PDF document
    pdf_editor.extract(infile, pages_to_extract, outfile)


# Delete Pages from PDF
def delete_pages_from_pdf(infile, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page numbers to be deleted (1-based index)
    pages_to_delete = [2, 4]

    # Delete the specified pages from the PDF document
    pdf_editor.delete(infile, pages_to_delete, outfile)


# Insert Pages into PDF
def insert_pages_into_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()

    # Define the page number where new pages will be inserted (1-based index)
    insert_page_number = 2

    pdf_editor.insert(infile, insert_page_number, sample_file, [1, 2], outfile)


# Append Pages to PDF
def append_pages_to_pdf(infile, sample_file, outfile):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    # Append pages from the specified PDF document to the end of the source PDF document
    pdf_editor.append(infile, [sample_file], 1, 2, outfile)    

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
        ("Insert Pages into PDF", insert_pages_into_pdf),
        ("Append Pages to PDF", append_pages_to_pdf),
        ("Extract Pages from PDF", extract_pages_from_pdf),
        ("Delete Pages from PDF", delete_pages_from_pdf),
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
