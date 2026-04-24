import aspose.pdf as ap
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import initialize_data_dir, set_license


def using_graphics_absorber(infile: str):
    """
    Demonstrate using GraphicsAbsorber to read vector graphics from PDF.

    Args:
        infile (str): Input PDF filename containing vector graphics

    Returns:
        None

    Example:
        using_graphics_absorber("DocumentWithVectorGraphics.pdf")

    Note:
        Prints information about each vector graphic element found on the first page.
    """
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")


def move_graphics(infile: str, outfile: str):
    """
    Move all vector graphics on a page by adjusting their positions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        move_graphics("input.pdf", "output.pdf")

    Note:
        Moves all vector graphics 150 units right and 10 units down.
    """
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                position = element.position
                element.position = ap.Point(position.x + 150, position.y - 10)
            graphics_absorber.resume_update()
        document.save(outfile)


def remove_graphics_method_1(infile: str, outfile: str):
    """
    Remove vector graphics within a specified rectangle (Method 1).

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        remove_graphics_method_1("input.pdf", "output.pdf")

    Note:
        Removes graphics by calling element.remove() on each element within the rectangle.
    """
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    element.remove()
            graphics_absorber.resume_update()
        document.save(outfile)


def remove_graphics_method_2(infile: str, outfile: str):
    """
    Remove vector graphics within a specified rectangle (Method 2).

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        remove_graphics_method_2("input.pdf", "output.pdf")

    Note:
        Removes graphics by collecting elements and calling page.delete_graphics().
    """
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.visit(page)
            removed_elements_collection = ap.vector.GraphicElementCollection()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    removed_elements_collection.add(element)
            page.contents.suppress_update()
            page.delete_graphics(removed_elements_collection)
            page.contents.resume_update()
        document.save(outfile)


def add_to_another_page_method_1(infile: str, outfile: str):
    """
    Copy vector graphics to another page (Method 1).

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        add_to_another_page_method_1("input.pdf", "output.pdf")

    Note:
        Copies graphics by calling element.add_on_page() for each element.
    """
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            for element in graphics_absorber.elements:
                element.add_on_page(page_2)
            page_2.contents.resume_update()
        document.save(outfile)


def add_to_another_page_method_2(infile: str, outfile: str):
    """
    Copy vector graphics to another page (Method 2).

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        add_to_another_page_method_2("input.pdf", "output.pdf")

    Note:
        Copies graphics by calling page.add_graphics() with the entire collection.
    """
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            page_2.add_graphics(graphics_absorber.elements, None)
            page_2.contents.resume_update()
        document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run Vector Graphics examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("using_graphics_absorber", using_graphics_absorber),
        ("move_graphics", move_graphics),
        ("remove_graphics_method_1", remove_graphics_method_1),
        ("remove_graphics_method_2", remove_graphics_method_2),
        ("add_to_another_page_method_1", add_to_another_page_method_1),
        ("add_to_another_page_method_2", add_to_another_page_method_2),
    ]

    for name, func in examples:
        try:
            input_file = path.join(input_dir, "DocumentWithVectorGraphics.pdf")
            if func.__name__ == "using_graphics_absorber":
                func(input_file)
            else:
                output_file = path.join(output_dir, f"{name}_out.pdf")
                func(input_file, output_file)
            print(f"✅ Success: {name} completed.")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")

    print(f"\nAll Vector Graphics examples finished. Check output in {output_dir}")


if __name__ == "__main__":
    run_all_examples()
