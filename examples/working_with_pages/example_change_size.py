import sys
import aspose.pdf as ap
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_page_size(input_file_name, output_file_name):
    """
    Set the size of the first page in the PDF document to A4 and save the updated document.

    Parameters:
    - input_file_name (str): Path to the input PDF file.
    - output_file_name (str): Path to save the output PDF file.
    """
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in) and in Aspose.Pdf, 1 inch = 72 points
    # So A4 dimensions in points will be (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)


def get_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Get particular page
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")


def get_page_size_rotation(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")


def run_all_examples(data_dir=None, license_path=None):
    """
    Run all page size manipulation examples.
    This function executes a series of examples demonstrating how to work with PDF page sizes
    using the Aspose.PDF library. It processes each example function sequentially and reports
    the success or failure of each operation.
    Args:
        data_dir (str, optional): The directory path containing input files and where output
            files will be saved. If None, a default directory will be used.
        license_path (str, optional): The file path to the Aspose.PDF license file.
            If None, the library will run in evaluation mode.
    Examples:
        The function runs the following examples:
        - set_page_size: Demonstrates setting custom page dimensions
        - get_page_size: Shows how to retrieve page size information
        - get_page_size_rotation: Illustrates getting page size with rotation info
    Returns:
        None: This function prints status messages to console but does not return a value.
    Side Effects:
        - Sets the Aspose.PDF license if license_path is provided
        - Creates output PDF files in the output directory
        - Prints success/failure messages for each example to console
    Note:
        Requires 'sample.pdf' to be present in the input directory.
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("set_page_size", set_page_size),
        ("get_page_size", get_page_size),
        ("get_page_size_rotation", get_page_size_rotation),
    ]

    for name, func in examples:
        input_file_name = path.join(input_dir, "sample.pdf")
        output_file_name = path.join(output_dir, f"{name}_out.pdf")
        try:
            func(input_file_name, output_file_name)
            print(f"✅ {name} completed. Output: {output_file_name}")
        except Exception as e:
            print(f"❌ {name} failed: {e}")

    print(f"\nAll page extraction examples finished. Check output in {output_dir}")


# Main execution
if __name__ == "__main__":
    run_all_examples()
