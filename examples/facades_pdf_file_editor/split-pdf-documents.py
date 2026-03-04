# Split PDF Documents
#─ Split PDF from Beginning
#─ Split PDF to End
#─ Split PDF into Multiple Documents
#─ Split PDF into Single Pages

from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Split PDF from Beginning
def split_pdf_from_beginning():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Create a new PDF document
    pdf_document = ap.Document()

    # Add a page to the PDF document
    pdf_document.pages.add()

    # Save the PDF document to the data directory
    input_pdf_path = path.join(data_dir, "input.pdf")
    pdf_document.save(input_pdf_path)

    # Create an instance of PdfFileEditor
    pdf_file_editor = pdf_facades.PdfFileEditor()

    # Split the PDF document from the beginning (starting from page 1)
    output_pdf_path = path.join(data_dir, "output_from_beginning.pdf")
    pdf_file_editor.split(input_pdf_path, output_pdf_path, 1)

# Split PDF to End
def split_pdf_to_end():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Create a new PDF document
    pdf_document = ap.Document()

    # Add a page to the PDF document
    pdf_document.pages.add()

    # Save the PDF document to the data directory
    input_pdf_path = path.join(data_dir, "input.pdf")
    pdf_document.save(input_pdf_path)

    # Create an instance of PdfFileEditor
    pdf_file_editor = pdf_facades.PdfFileEditor()

    # Split the PDF document to the end (starting from page 1)
    output_pdf_path = path.join(data_dir, "output_to_end.pdf")
    pdf_file_editor.split(input_pdf_path, output_pdf_path, 1, -1)

# Split PDF into Multiple Documents
def split_pdf_into_multiple_documents():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Create a new PDF document
    pdf_document = ap.Document()

    # Add multiple pages to the PDF document
    for i in range(1, 6):
        pdf_document.pages.add()

    # Save the PDF document to the data directory
    input_pdf_path = path.join(data_dir, "input.pdf")
    pdf_document.save(input_pdf_path)

    # Create an instance of PdfFileEditor
    pdf_file_editor = pdf_facades.PdfFileEditor()

    # Split the PDF document into multiple documents (2 pages each)
    output_pdf_path_pattern = path.join(data_dir, "output_split_%d.pdf")
    pdf_file_editor.split(input_pdf_path, output_pdf_path_pattern, 1, 2)

# Split PDF into Single Pages
def split_pdf_into_single_pages():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Create a new PDF document
    pdf_document = ap.Document()

    # Add multiple pages to the PDF document
    for i in range(1, 6):
        pdf_document.pages.add()

    # Save the PDF document to the data directory
    input_pdf_path = path.join(data_dir, "input.pdf")
    pdf_document.save(input_pdf_path)

    # Create an instance of PdfFileEditor
    pdf_file_editor = pdf_facades.PdfFileEditor()

    # Split the PDF document into single pages
    output_pdf_path_pattern = path.join(data_dir, "output_page_%d.pdf")
    pdf_file_editor.split(input_pdf_path, output_pdf_path_pattern, 1, 1)

def run_all_examples(data_dir=None, license_path=None):
    """Run all page splitting examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Split PDF from Beginning", split_pdf_from_beginning, "output_from_beginning.pdf"),
        ("Split PDF to End", split_pdf_to_end, "output_to_end.pdf"),
        ("Split PDF into Multiple Documents", split_pdf_into_multiple_documents, "output_split_1.pdf"),
        ("Split PDF into Single Pages", split_pdf_into_single_pages, "output_page_1.pdf")
    ]

    for name, func, data_file_name in examples:
        try:
            if (func.__name__ == "insert_pages_into_pdf" or func.__name__ == "append_pages_to_pdf"):
                input_file_name = path.join(input_dir, "")
            else:
                input_file_name = path.join(input_dir, "f")
            output_file_name = path.join(output_dir, data_file_name)
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll page splitting examples finished.")


if __name__ == "__main__":
    run_all_examples()                                   
