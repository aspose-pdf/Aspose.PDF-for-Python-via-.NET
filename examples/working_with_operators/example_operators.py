import sys
import aspose.pdf as ap
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_image_using_pdf_operators(infile, imagefile, outfile):
    """
    Add image to PDF using low-level operators.

    Args:
        infile (str): Input PDF filename
        imagefile (str): Image filename to add
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        add_image_using_pdf_operators("PDFOperators.pdf", "PDFOperators.jpg", "PDFOperators_out.pdf")

    Note:
        Uses GSave, ConcatenateMatrix, Do, GRestore operators.
        Image placed at rectangle (100, 100, 200, 200).
    """
    with ap.Document(infile) as document:
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        page = document.pages[1]

        with open(imagefile, "rb") as image_stream:
            page.resources.images.add(image_stream)

        page.contents.append(ap.operators.GSave())

        rectangle = ap.Rectangle(
            lower_left_x, lower_left_y, upper_right_x, upper_right_y, True
        )
        matrix = ap.Matrix(
            [
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            ]
        )

        page.contents.append(ap.operators.ConcatenateMatrix(matrix))

        x_image = page.resources.images[len(page.resources.images)]

        page.contents.append(ap.operators.Do(x_image.name))

        page.contents.append(ap.operators.GRestore())

        document.save(outfile)


def draw_xform_on_page(infile, imagefile, outfile):
    """
    Draw XForm with image at multiple positions.

    Args:
        infile (str): Input PDF filename
        imagefile (str): Image filename to add
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        draw_xform_on_page("DrawXFormOnPage.pdf", "aspose-logo.jpg", "DrawXFormOnPage_out.pdf")

    Note:
        Creates XForm with image, draws it at (100, 500) and (100, 300).
        Uses operators to wrap existing contents and place XForm.
    """
    with ap.Document(infile) as document:
        page_contents = document.pages[1].contents

        page_contents.insert(1, ap.operators.GSave())
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GSave())

        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.append(form)

        form.contents.append(ap.operators.GSave())
        form.contents.append(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        with open(imagefile, "rb") as image_stream:
            form.resources.images.add(image_stream)

        x_image = form.resources.images[len(form.resources.images)]
        form.contents.append(ap.operators.Do(x_image.name))
        form.contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 500)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 300)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GRestore())

        document.save(outfile)


def remove_graphics_objects(infile, outfile):
    """
    Remove graphics objects from PDF page.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        remove_graphics_objects("RemoveGraphicsObjects.pdf", "NoGraphics_out.pdf")

    Note:
        Removes Stroke, ClosePathStroke, and Fill operators from first page.        
    """
    with ap.Document(infile) as document:
        page = document.pages[1]
        # Collect operators to remove in single pass
        # Operator codes: S=Stroke, h=ClosePathStroke, f=Fill'
        graphics_operators = {"S", "h", "f"}
        operators_to_remove = [op for op in page.contents if str(op) in graphics_operators]

        page.contents.delete(operators_to_remove)
        document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run operators examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "Add image using operators",
            add_image_using_pdf_operators,
            "PDFOperators.jpg",
        ),
        (
            "Draw XForm on page",
            draw_xform_on_page,
            "sample-cover.jpg",
        ),
        ("Remove graphics objects", remove_graphics_objects, ""),
    ]

    for name, func, sample in examples:
        try:
            output_file_name = path.join(output_dir, f"{func.__name__}.pdf")
            if func.__name__ == "remove_graphics_objects":
                input_file_name = path.join(input_dir, "RemoveGraphicsObjects.pdf")
                func(input_file_name, output_file_name)
            else:
                input_file_name = path.join(input_dir, "sample.pdf")
                sample_file_name = path.join(input_dir, sample)
                func(input_file_name, sample_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()
