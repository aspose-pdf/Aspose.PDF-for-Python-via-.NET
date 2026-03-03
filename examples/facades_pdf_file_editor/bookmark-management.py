# Bookmark Management
# ├─ Delete Bookmark
# └─ Flatten Bookmarks

from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Delete Bookmark
def delete_bookmark():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Create a new PDF document
    pdf_document = ap.Document()

    # Add a page to the document
    page = pdf_document.pages.add()

    # Add a bookmark to the page
    bookmark = pdf_document.outlines.add("Bookmark 1", page)

    # Save the document to the data directory
    output_path = path.join(data_dir, "delete_bookmark.pdf")
    pdf_document.save(output_path)

    # Load the PDF document using Facades API
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.bind_pdf(output_path)

    # Delete the bookmark
    pdf_editor.delete_bookmark("Bookmark 1")

    # Save the updated document
    updated_output_path = path.join(data_dir, "delete_bookmark_updated.pdf")
    pdf_editor.save(updated_output_path)

# Flatten Bookmarks    
def flatten_bookmarks():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Create a new PDF document
    pdf_document = ap.Document()

    # Add a page to the document
    page = pdf_document.pages.add()

    # Add a bookmark to the page
    bookmark = pdf_document.outlines.add("Bookmark 1", page)

    # Save the document to the data directory
    output_path = path.join(data_dir, "flatten_bookmarks.pdf")
    pdf_document.save(output_path)

    # Load the PDF document using Facades API
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.bind_pdf(output_path)

    # Flatten the bookmarks
    pdf_editor.flatten_bookmarks()

    # Save the updated document
    updated_output_path = path.join(data_dir, "flatten_bookmarks_updated.pdf")
    pdf_editor.save(updated_output_path)

def run_all_examples(data_dir=None, license_path=None):
    """Run all bookmark management examples and report status .

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    examples = [
        ("Delete Bookmark", delete_bookmark),
        ("Flatten Bookmarks", flatten_bookmarks)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}_in.pdf")
            func(input_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll bookmark management examples finished.")


if __name__ == "__main__":
    run_all_examples()    