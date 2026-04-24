import sys
import aspose.pdf as ap
from io import FileIO
from os import path

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
        extract_image("sample_extr.pdf", "extracted_image.jpg")

    Note:
        Extracts first image from first page.
    """
    document = ap.Document(infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(outfile, "w") as output_image:
        xImage.save(output_image)


def extract_image_from_specific_region(infile, outfile):
    """
    Extract images from specific region of PDF page.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output image filename pattern (use 'index' for numbering)

    Returns:
        None

    Example:
        extract_image_from_specific_region("sample_extr.pdf", "extracted_image_index.jpg")

    Note:
        Extracts images within rectangle (0, 0, 590, 590).
        Output files numbered as index 1, 2, 3, etc.
    """
    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.urx)
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1


def run_all_examples(data_dir=None, license_path=None):
    """Run extract image examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Extract image", extract_image, "extracted_image.jpg"),
        (
            "Extract from region",
            extract_image_from_specific_region,
            "extracted_image_index.jpg",
        ),
    ]

    input_file_name = path.join(input_dir, "sample_extr.pdf")
    for name, func, o in examples:
        try:
            output_file_name = path.join(output_dir, o)
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
