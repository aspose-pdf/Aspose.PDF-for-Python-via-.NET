import aspose.pdf as ap
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def compare_pdf_with_get_difference_method(infile1, infile2, outfile1, outfile2):
    """
    Compare two PDF pages using GraphicalPdfComparer and save difference images.

    Args:
        infile1 (str): First input PDF file name
        infile2 (str): Second input PDF file name
        outfile1 (str): Output PNG file showing differences in red over white
        outfile2 (str): Output PNG file showing the destination page

    Returns:
        None

    Example:
        >>> compare_pdf_with_get_difference_method("doc1.pdf", "doc2.pdf", "diff.png", "dest.png")

    Note:
        Compares the first page of each document and generates two PNG images.
    """
    # Open PDF documents
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)

    # Create comparer
    comparer = ap.comparison.GraphicalPdfComparer()

    # Compare specific pages
    images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

    # Get image showing differences in red over a white background
    diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
    diff_img.save(outfile1)

    # Get the second image representing the destination page
    dest_img = images_difference.get_destination_image()
    dest_img.save(outfile2)


def comparing_specific_pages(infile1, infile2, outfile):
    """
    Compare specific pages from two PDF documents side by side.

    Args:
        infile1 (str): First input PDF file name
        infile2 (str): Second input PDF file name
        outfile (str): Output PDF file name

    Returns:
        None

    Example:
        >>> comparing_specific_pages("doc1.pdf", "doc2.pdf", "comparison.pdf")

    Note:
        Compares the first page of each document with additional change marks,
        ignoring spaces in the comparison.
    """

    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1.pages[1], document_2.pages[1], outfile, options
    )


def compare_pdf_with_compare_documents_to_pdf_method(infile1, infile2, outfile):
    """
    Compare two PDF documents graphically and save the result to a PDF file.

    Args:
        infile1 (str): First input PDF file name
        infile2 (str): Second input PDF file name
        outfile (str): Output PDF file name

    Returns:
        None

    Example:
        >>> compare_pdf_with_compare_documents_to_pdf_method("doc1.pdf", "doc2.pdf", "result.pdf")

    Note:
        Uses GraphicalPdfComparer with threshold=3.0, blue color for differences,
        and 300 DPI resolution.
    """

    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Create comparer and set options
    pdf_comparer = ap.comparison.GraphicalPdfComparer()
    pdf_comparer.threshold = 3.0
    pdf_comparer.color = ap.Color.blue
    pdf_comparer.resolution = ap.devices.Resolution(300)

    # Compare and output to a PDF file
    pdf_comparer.compare_documents_to_pdf(document_1, document_2, outfile)


def comparing_entire_documents(infile1, infile2, outfile):
    """
    Compare entire PDF documents side by side.

    Args:
        infile1 (str): First input PDF file name
        infile2 (str): Second input PDF file name
        outfile (str): Output PDF file name

    Returns:
        None

    Example:
        >>> comparing_entire_documents("doc1.pdf", "doc2.pdf", "full_comparison.pdf")

    Note:
        Compares all pages with additional change marks, ignoring spaces.
    """

    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1, document_2, outfile, options
    )


def run_all_examples(data_dir=None, license_path=None):
    """Run compare examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    # Initialize data directory
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "compare_pdf_with_get_difference_method",
            compare_pdf_with_get_difference_method,
        ),
        ("comparing_specific_pages", comparing_specific_pages),
        (
            "compare_pdf_with_compare_documents_to_pdf_method",
            compare_pdf_with_compare_documents_to_pdf_method,
        ),
        ("comparing_entire_documents", comparing_entire_documents),
    ]

    for name, func in examples:
        infile1 = path.join(input_dir, "sample_1.pdf")
        infile2 = path.join(input_dir, "sample_2.pdf")
        outfile = path.join(output_dir, f"{func.__name__}_out.pdf")
        try:
            if func.__name__ == "compare_pdf_with_get_difference_method":
                func(
                    infile1,
                    infile2,
                    path.join(
                        output_dir, "compare_pdf_with_get_difference_method_diff.png"
                    ),
                    path.join(
                        output_dir, "compare_pdf_with_get_difference_method_dest.png"
                    ),
                )
            else:
                func(infile1, infile2, outfile)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print(f"\nAll compare examples finished. Check output in {output_dir}")


if __name__ == "__main__":
    run_all_examples()
