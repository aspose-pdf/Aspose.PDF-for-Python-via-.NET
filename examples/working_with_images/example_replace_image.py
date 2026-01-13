import sys
import aspose.pdf as ap
from io import FileIO
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    """
    Replace image in PDF document.

    Args:
        infile (str): Input PDF filename
        image_file (str): New image filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        replace_image("sample_replace.pdf", "sample_new.jpg", "sample_replace_1.pdf")

    Note:
        Replaces first image on first page.
    """
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)


def replace_image_with_absorber(infile, image_file, outfile):
    """
    Replace image using ImagePlacementAbsorber.

    Args:
        infile (str): Input PDF filename
        image_file (str): New image filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        replace_image_with_absorber("sample_replace.pdf", "sample_new.jpg", "sample_replace_2.pdf")

    Note:
        Uses ImagePlacementAbsorber to find and replace first image placement.
    """
    document = ap.Document(infile)

    # Create ImagePlacementAbsorber to find image placements
    absorber = ap.ImagePlacementAbsorber()

    # Accept the absorber for the first page
    document.pages[1].accept(absorber)

    # Replace the first image placement found
    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run replace image examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)
    examples = [
        ("Replace image", replace_image),
        ("Replace with absorber", replace_image_with_absorber),
    ]

    input_file_name = path.join(input_dir, "sample_replace.pdf")
    image_file_name = path.join(input_dir, "sample_new.jpg")
    for name, func in examples:
        try:
            output_file_name = path.join(output_dir, f"{func.__name__}.pdf")
            func(input_file_name, image_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
