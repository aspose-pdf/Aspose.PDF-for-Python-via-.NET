import sys
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def extract_image_params(infile):
    """
    Extract and print image parameters from PDF.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_params("sample.pdf")

    Note:
        Prints width, height, position (LLX, LLY), and resolution for each image.
    """
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))


def extract_image_types_from_pdf(infile):
    """
    Extract and count image types (grayscale/RGB) with resolution analysis.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_types_from_pdf("sample_extr.pdf")

    Note:
        Prints total images count, color type for each image, and resolution info.
        Uses operators analysis (GSave/GRestore/ConcatenateMatrix/Do) to calculate scaling.
    """
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()

    grayscaled = 0
    rgb = 0

    document.pages[1].accept(absorber)

    print("--------------------------------")
    print("Total Images = " + str(len(absorber.image_placements)))

    image_counter = 1

    for image_placement in absorber.image_placements:
        colorType = image_placement.image.get_color_type()
        if colorType == ap.ColorType.GRAYSCALE:
            grayscaled += 1
            print(f"Image {image_counter} is Grayscale...")
        elif colorType == ap.ColorType.RGB:
            rgb += 1
            print(f"Image {image_counter} is RGB...")
        image_counter += 1

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(
        drawing.drawing2d.Matrix(
            float(1), float(0), float(0), float(1), float(0), float(0)
        )
    )

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

                print(
                    f"image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )


def extract_image_alt_text(infile):
    """
    Extract alternative text from images in PDF.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_alt_text("sample_extr.pdf")

    Note:
        Prints name in collection and alternative text for each image on first page.
    """
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: " + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])


def extract_image_information_from_pdf(infile):
    """
    Extract detailed image information using operators analysis.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_information_from_pdf("sample_alt.pdf")

    Note:
        Analyzes page contents operators to calculate scaled dimensions and resolution.
        Uses graphics state stack to track transformations.
    """

    document = ap.Document(infile)

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(
        drawing.drawing2d.Matrix(
            float(1), float(0), float(0), float(1), float(0), float(0)
        )
    )

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

                print(
                    f"image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )


def run_all_examples(data_dir=None, license_path=None):
    """Run get search image examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    examples = [
        ("Extract image params", extract_image_params, "sample_extr.pdf"),
        ("Extract image types", extract_image_types_from_pdf, "sample_extr.pdf"),
        (
            "Extract image information",
            extract_image_information_from_pdf,
            "sample_alt.pdf",
        ),
        ("Extract alt text", extract_image_alt_text, "sample_extr.pdf"),
    ]

    for name, func, sample in examples:
        try:
            input_file_name = path.join(input_dir, sample)
            func(input_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
