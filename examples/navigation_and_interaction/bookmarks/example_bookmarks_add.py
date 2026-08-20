import aspose.pdf as ap
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_bookmark(infile, outfile):
    """
    Add a bookmark (outline) to a PDF document.

    Args:
        infile (str): The input PDF file name
        outfile (str): The output PDF file name

    Returns:
        None

    Example:
        >>> add_bookmark("input.pdf", "output.pdf")

    Note:
        Creates a bookmark titled "Test Outline" pointing to the first page,
        with italic and bold text styling.
    """
    # Open PDF document
    document = ap.Document(infile)

    # Create a bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Test Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Set the destination page number
    pdf_outline.action = ap.annotations.GoToAction(document.pages[1])

    # Add bookmark to the document's outline collection
    outlines = document.outlines
    outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)


def add_child_bookmark(infile, outfile):
    """
    Add a parent bookmark with a child bookmark to a PDF document.

    Args:
        infile (str): The input PDF file name
        outfile (str): The output PDF file name

    Returns:
        None

    Example:
        >>> add_child_bookmark("input.pdf", "output.pdf")

    Note:
        Creates a "Parent Outline" with a nested "Child Outline",
        both with italic and bold text styling.
    """

    # Open PDF document
    document = ap.Document(infile)

    # Create a parent bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Parent Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Create a child bookmark object
    pdf_child_outline = ap.OutlineItemCollection(document.outlines)
    pdf_child_outline.title = "Child Outline"
    pdf_child_outline.italic = True
    pdf_child_outline.bold = True

    # Add child bookmark to parent bookmark's collection
    pdf_outline.append(pdf_child_outline)

    # Add parent bookmark to the document's outline collection
    document.outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)


def delete_bookmarks(infile, outfile):
    """
    Delete all bookmarks from a PDF document.

    Args:
        infile (str): The input PDF file name
        outfile (str): The output PDF file name

    Returns:
        None

    Example:
        >>> delete_bookmarks("input.pdf", "output.pdf")

    Note:
        This removes all outline entries from the document.
    """
    # Open PDF document
    document = ap.Document(infile)

    # Delete all bookmarks in the PDF document
    document.outlines.delete()

    # Save PDF document
    document.save(outfile)


def delete_bookmark(infile, outfile):
    """
    Delete a specific bookmark by title from a PDF document.

    Args:
        infile (str): The input PDF file name
        outfile (str): The output PDF file name

    Returns:
        None

    Example:
        >>> delete_bookmark("input.pdf", "output.pdf")

    Note:
        Deletes the bookmark titled "Child Outline". If multiple bookmarks
        have the same title, only the first matching bookmark will be deleted.
    """
    # Open PDF document
    document = ap.Document(infile)

    # Delete a specific bookmark by title.
    # Note: If multiple bookmarks have the same title, only the first matching bookmark will be deleted.
    document.outlines.delete("Child Outline")

    # Save PDF document
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run Bookmarks examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("add_bookmark", add_bookmark),
        ("add_child_bookmark", add_child_bookmark),
        ("delete_bookmarks", delete_bookmarks),
        ("delete_bookmark", delete_bookmark),
    ]

    for name, func in examples:
        try:
            if "delete" in name:
                input_file_name = path.join(input_dir, "delete_bookmark_in.pdf")
            else:
                input_file_name = path.join(input_dir, "bookmark.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print(f"\nAll Bookmarks creation examples finished. Check output in {output_dir}")


if __name__ == "__main__":
    run_all_examples()
