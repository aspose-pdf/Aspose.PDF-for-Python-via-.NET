import sys
import aspose.pdf as ap
from os import path
from io import FileIO

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_image(image_file, outfile):
    """
    Add an image to PDF document at specified position.

    Args:
        infile (str): Input PDF filename
        image_file (str): Image filename to add
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        add_image("sample.pdf", "sample.png", "sample_add_image.pdf")

    Note:
        Adds image to first page at rectangle (20, 730, 120, 830).
    """
    document = ap.Document()
    page = document.pages.add()
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)


def add_image_using_operators(image_file, outfile):
    """
    Add image to PDF using low-level operators.

    Args:
        image_file (str): Image filename to add
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        add_image_using_operators("sample.jpg", "sample_add_image_op.pdf")

    Note:
        Creates new PDF with image using GSave/ConcatenateMatrix/Do/GRestore operators.
        Image is scaled to fit page width maintaining aspect ratio.
    """

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(image_file, "rb")
    image_id = resources_images.add(image_stream)

    x_image = list(resources_images)[-1]

    rectangle = ap.Rectangle(
        0,
        0,
        page.media_box.width,
        (page.media_box.width * x_image.height) / x_image.width,
        True,
    )

    # Create operator sequence for adding image
    operators = []

    # Save graphics state
    operators.append(ap.operators.GSave())

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.llx + (page.media_box.height - rectangle.height) / 2,
    )
    operators.append(ap.operators.ConcatenateMatrix(matrix))

    # Draw the image
    operators.append(ap.operators.Do(image_id))

    # Restore graphics state
    operators.append(ap.operators.GRestore())

    # Add operators to page contents
    page.contents.add(operators)

    document.save(outfile)


def add_image_set_alternative_text_for_image(image_file, outfile):
    """
    Add image with alternative text to PDF.

    Args:
        image_file (str): Image filename to add
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        add_image_set_alternative_text_for_image("sample.jpg", "sample_add_image_alt.pdf")

    Note:
        Creates new PDF with image at full page size (842x595).
        Sets alternative text for accessibility using try_set_alternative_text.
    """

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))

    resources_images = page.resources.images
    alt_text = "Alternative text for image"
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text(alt_text, page)

    # If set is successful, then get the alternative text for the image
    if result:
        print("Text has been added successfuly")
    document.save(outfile)


def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(image_file, "rb")
    image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    # Save the current graphics state
    page.contents.add(ap.operators.GSave())

    # Set coordinates for the image placement
    lowerLeftX = 0
    lowerLeftY = 0
    upperRightX = 600
    upperRightY = 600

    rectangle = ap.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY, True)

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    # Use ConcatenateMatrix operator to define how the image must be placed
    page.contents.add(ap.operators.ConcatenateMatrix(matrix))
    page.contents.add(ap.operators.Do(image_id))

    # Restore the graphics state
    page.contents.add(ap.operators.GRestore())

    # Save the document
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run add image examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add image", add_image),
        (
            "Add image using operators",
            add_image_using_operators,
        ),
        (
            "Add image with alt text",
            add_image_set_alternative_text_for_image,
        ),
        (
            "Add image to PDF with Flate Compression",
            add_image_to_pdf_with_flate_compression,
        ),
    ]

    for name, func in examples:
        input_file_name = path.join(input_dir, "sample.jpg")
        output_file_name = path.join(output_dir, f"{name}_out.pdf")
        try:
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
