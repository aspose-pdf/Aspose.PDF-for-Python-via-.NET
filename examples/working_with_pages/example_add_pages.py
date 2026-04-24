import sys
import aspose.pdf as ap
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def insert_empty_page(input_file_name, output_file_name):
    """Insert a new empty page at a specific position.

    Args:
        input_file_name (str): Path to the source PDF.
        output_file_name (str): Path where the modified PDF is saved.
    Returns:
        None
    Example:
        >>> insert_empty_page("sample.pdf", "insert_empty_page_out.pdf")
    Note:
        Uses 1-based indexing; here inserts a page at position 2.
    """
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)


def add_empty_page_to_end(input_file_name, output_file_name):
    """Append an empty page at the end of a PDF.

    Args:
        input_file_name (str): Path to the source PDF.
        output_file_name (str): Path where the modified PDF is saved.
    Returns:
        None
    Example:
        >>> add_empty_page_to_end("sample.pdf", "add_empty_page_to_end_out.pdf")
    Note:
        The new page is added as the last page of the document.
    """
    document = ap.Document(input_file_name)
    document.pages.add()
    document.save(output_file_name)


def add_page_from_another_document(input_file_name, output_file_name):
    """Add a page from another PDF into the current document.

    Creates a new document with a first page, then imports the first page
    of another document and appends it.

    Args:
        input_file_name (str): Path to the second PDF whose first page is imported.
        output_file_name (str): Path where the combined PDF is saved.
    Returns:
        None
    Example:
        >>> add_page_from_another_document("sample.pdf", "add_page_from_another_document_out.pdf")
    Note:
        Imported pages retain their original content and properties.
    """
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    document.save(output_file_name)


def run_all_examples(data_dir=None, license_path=None):
    """Run page adding examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("insert_empty_page", insert_empty_page),
        ("add_empty_page_to_end", add_empty_page_to_end),
        ("add_page_from_another_document", add_page_from_another_document),
    ]

    for name, func in examples:
        input_file_name = path.join(input_dir, "sample.pdf")
        output_file_name = path.join(output_dir, f"{name}_out.pdf")
        try:
            func(input_file_name, output_file_name)
            print(f"✅ {name} completed. Output: {output_file_name}")
        except Exception as e:
            print(f"❌ {name} failed: {e}")

    print(f"\nAll page adding examples finished. Check output in {output_dir}")


# Main execution
if __name__ == "__main__":
    run_all_examples()
