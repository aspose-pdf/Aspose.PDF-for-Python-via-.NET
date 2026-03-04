# Page Management
#─ Extract Pages from PDF
#─ Delete Pages from PDF
#─ Insert Pages into PDF
#─ Append Pages to PDF
#─ Concatenate or Merge PDF Files

from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Extract Pages from PDF
def extract_pages_from_pdf():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license for Aspose.PDF
    set_license()

    # Open the source PDF document
    with ap.Document(path.join(data_dir, "input.pdf")) as pdf_document:
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page numbers to be extracted (1-based index)
        pages_to_extract = [1, 3, 5]

        # Extract the specified pages into a new PDF document
        output_path = path.join(data_dir, "extracted_pages.pdf")
        pdf_editor.extract(
            path.join(data_dir, "input.pdf"),
            output_path,
            pages_to_extract,
        )
        print(f"Extracted pages saved to: {output_path}")

# Delete Pages from PDF
def delete_pages_from_pdf():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license for Aspose.PDF
    set_license()

    # Open the source PDF document
    with ap.Document(path.join(data_dir, "input.pdf")) as pdf_document:
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page numbers to be deleted (1-based index)
        pages_to_delete = [2, 4]

        # Delete the specified pages from the PDF document
        output_path = path.join(data_dir, "pdf_with_deleted_pages.pdf")
        pdf_editor.delete(
            path.join(data_dir, "input.pdf"),
            output_path,
            pages_to_delete,
        )
        print(f"PDF with deleted pages saved to: {output_path}")

# Insert Pages into PDF
def insert_pages_into_pdf():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license for Aspose.PDF
    set_license()

    # Open the source PDF document
    with ap.Document(path.join(data_dir, "input.pdf")) as pdf_document:
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page number where new pages will be inserted (1-based index)
        insert_page_number = 2

        # Define the path to the PDF document containing pages to be inserted
        pages_to_insert_path = path.join(data_dir, "pages_to_insert.pdf")

        # Insert pages from the specified PDF document into the source PDF document
        output_path = path.join(data_dir, "pdf_with_inserted_pages.pdf")
        pdf_editor.insert(
            path.join(data_dir, "input.pdf"),
            output_path,
            insert_page_number,
            pages_to_insert_path,
            [1, 2],  # Pages to insert from the second PDF (1-based index)
        )
        print(f"PDF with inserted pages saved to: {output_path}")

# Append Pages to PDF
def append_pages_to_pdf():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license for Aspose.PDF
    set_license()

    # Open the source PDF document
    with ap.Document(path.join(data_dir, "input.pdf")) as pdf_document:
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the path to the PDF document containing pages to be appended
        pages_to_append_path = path.join(data_dir, "pages_to_append.pdf")

        # Append pages from the specified PDF document to the end of the source PDF document
        output_path = path.join(data_dir, "pdf_with_appended_pages.pdf")
        pdf_editor.append(
            path.join(data_dir, "input.pdf"),
            output_path,
            pages_to_append_path,
            [1, 2],  # Pages to append from the second PDF (1-based index)
        )
        print(f"PDF with appended pages saved to: {output_path}")

# Concatenate or Merge PDF Files
def concatenate_or_merge_pdf_files():
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

        ("Insert Pages into PDF", insert_pages_into_pdf, "pdf_with_inserted_pages.pdf"),
        ("Append Pages to PDF", append_pages_to_pdf, "pdf_with_appended_pages.pdf"),
        ("Concatenate or Merge PDF Files", concatenate_or_merge_pdf_files, "merged_output.pdf"),
        ("Extract Pages from PDF", extract_pages_from_pdf, "extracted_pages.pdf"),
        ("Delete Pages from PDF", delete_pages_from_pdf, "pdf_with_deleted_pages.pdf")
    ]

    for name, func, data_file_name in examples:
        try:
            if (func.__name__ == "insert_pages_into_pdf" or func.__name__ == "append_pages_to_pdf"):
                input_file_name = path.join(input_dir, "input.pdf")
            else:
                input_file_name = path.join(input_dir, "f")
            output_file_name = path.join(output_dir, data_file_name)
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll page management examples finished.")


if __name__ == "__main__":
    run_all_examples()                               