import math
import sys

import aspose.pdf as ap
import aspose.pydrawing as drawing

from aspose.pycore import cast, is_assignable
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


def extract_image_information(infile, outfile):

    document = ap.Document(infile)

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(
        drawing.drawing2d.Matrix(
            float(1), float(0), float(0), float(1), float(0), float(0)
        )
    )

    with FileIO(outfile, "w") as output_file:
        for op in document.pages[1].contents:
            if is_assignable(op, ap.operators.GSave):
                graphics_state.append(
                    cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone()
                )

            elif is_assignable(op, ap.operators.GRestore):
                graphics_state.pop()

            elif is_assignable(op, ap.operators.ConcatenateMatrix):
                opCM = cast(ap.operators.ConcatenateMatrix, op)
                cm = drawing.drawing2d.Matrix(
                    float(opCM.matrix.a),
                    float(opCM.matrix.b),
                    float(opCM.matrix.c),
                    float(opCM.matrix.d),
                    float(opCM.matrix.e),
                    float(opCM.matrix.f),
                )

                graphics_state[-1].multiply(cm)
                continue

            elif is_assignable(op, ap.operators.Do):
                opDo = cast(ap.operators.Do, op)
                if opDo.name in image_names:
                    last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                    index = image_names.index(opDo.name) + 1
                    image = document.pages[1].resources.images[index]

                    scaled_width = math.sqrt(
                        last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2
                    )
                    scaled_height = math.sqrt(
                        last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2
                    )

                    original_width = image.width
                    original_height = image.height

                    res_horizontal = original_width * default_resolution / scaled_width
                    res_vertical = original_height * default_resolution / scaled_height

                    info = (
                        f"{infile} image {opDo.name} "
                        f"({scaled_width:.2f}:{scaled_height:.2f}): "
                        f"res {res_horizontal:.2f} x {res_vertical:.2f}\n"
                    )
                    print(info.rstrip())
                    output_file.write(info.encode())


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
        (
            "Extract image information",
            extract_image_information,
            "extracted_image_information.txt",
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
