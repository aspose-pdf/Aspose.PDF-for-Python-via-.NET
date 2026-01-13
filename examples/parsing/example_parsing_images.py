import aspose.pdf as ap
from io import FileIO
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def extract_image(infile, outfile):
    """
    Extract image from PDF document.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output image filename

    Returns:
        None

    Example:
        extract_image("sample-image.pdf", "extracted-image.jpg")

    Note:
        Extracts first image from first page.
    """
    document = ap.Document(infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(outfile, "wb") as output_image:
        xImage.save(output_image)

def run_all_examples(data_dir=None, license_path=None):
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Extract Image", extract_image, "sample-image.pdf", "extracted-image.jpg", None),
    ]

    for name, func, input_file, output_file, page_num in examples:
        try:
            args = [
                path.join(input_dir, input_file),
                path.join(output_dir, output_file),
            ]
            if page_num:
                args.append(page_num)
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()