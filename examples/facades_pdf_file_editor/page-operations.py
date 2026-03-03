# Page Operations
# ├─ Extract Pages
# ├─ Insert Pages
# ├─ Delete Pages
# ├─ Replace Pages
# └─ Clone Pages

from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Extract Pages
def extract_pages():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license
    set_license()

    # Create a PdfExtractor object
    extractor = pdf_facades.PdfExtractor()

    # Bind the source PDF file
    extractor.bind_pdf(path.join(data_dir, "input.pdf"))

    # Extract pages 1 to 3 and save them to a new PDF file
    with FileIO(path.join(data_dir, "extracted_pages.pdf"), "w") as output_file:
        extractor.extract_pages(output_file, 1, 3)

# Insert Pages
def insert_pages():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license
    set_license()

    # Create a PdfFileEditor object
    editor = pdf_facades.PdfFileEditor()

    # Bind the source PDF file
    editor.bind_pdf(path.join(data_dir, "input.pdf"))

    # Insert pages from another PDF file at page 2
    editor.insert(path.join(data_dir, "pages_to_insert.pdf"), 2)

    # Save the modified PDF file
    editor.save(path.join(data_dir, "after_inserting_pages.pdf"))

# Delete Pages            
def delete_pages():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license
    set_license()

    # Create a PdfFileEditor object
    editor = pdf_facades.PdfFileEditor()

    # Bind the source PDF file
    editor.bind_pdf(path.join(data_dir, "input.pdf"))

    # Delete pages 2 to 4
    editor.delete(2, 4)

    # Save the modified PDF file
    editor.save(path.join(data_dir, "after_deleting_pages.pdf"))

# Replace Pages
def replace_pages():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license
    set_license()

    # Create a PdfFileEditor object
    editor = pdf_facades.PdfFileEditor()

    # Bind the source PDF file
    editor.bind_pdf(path.join(data_dir, "input.pdf"))

    # Replace pages 2 to 4 with pages from another PDF file
    editor.replace(path.join(data_dir, "replacement_pages.pdf"), 2, 4)

    # Save the modified PDF file
    editor.save(path.join(data_dir, "after_replacing_pages.pdf"))

# Clone Pages
def clone_pages():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license
    set_license()

    # Create a PdfFileEditor object
    editor = pdf_facades.PdfFileEditor()

    # Bind the source PDF file
    editor.bind_pdf(path.join(data_dir, "input.pdf"))

    # Clone pages 2 to 4 and insert them at page 5
    editor.clone(2, 4, 5)

    # Save the modified PDF file
    editor.save(path.join(data_dir, "after_cloning_pages.pdf"))        

def run_all_examples(data_dir=None, license_path=None):
    """Run all page operations examples and report status .

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    examples = [
        ("Extract Pages", extract_pages),
        ("Insert Pages", insert_pages),
        ("Delete Pages", delete_pages),
        ("Replace Pages", replace_pages),
        ("Clone Pages", clone_pages)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}_in.pdf")
            func(input_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll managing PDF page operations examples finished.")


if __name__ == "__main__":
    run_all_examples()