import aspose.pdf as ap
import aspose.pdf.vector as apv
from os import path, makedirs
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def extract_graphics_elements(infile, outfile):
    """
    Extract vector graphic elements from a specified page of a PDF and log basic element properties.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file for logging element info.
    """
    document = ap.Document(infile)

    gr_absorber = apv.GraphicsAbsorber()
    # Visit page 2 (pages collection is 1-indexed; document.pages[1] is the second page)
    gr_absorber.visit(document.pages[1])

    elements = gr_absorber.elements
    with open(outfile, "w", encoding="utf-8") as f:
        for idx, elem in enumerate(elements, start=1):
            # Basic properties
            rect = elem.rectangle
            pos = elem.position
            ops_count = len(elem.operators)
            f.write(
                f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n"
            )


def save_vector_graphics_to_svg(infile, svg_outfile):
    """
    Save vector graphics from a specified page of a PDF document into an SVG file.
    Args:
        infile (str): Path to input PDF file.
        svg_outfile (str): Path to output SVG file.
    """
    document = ap.Document(infile)

    page = document.pages[1]
    # Try to save vector graphics into SVG
    page.try_save_vector_graphics(svg_outfile)


def extract_subpaths_to_svgs(infile, output_dir):
    """
    Extract each vector sub-path on a PDF page into separate SVG files using extraction options.
    Args:
        infile (str): Input PDF file path.
        output_dir (str): Directory path where SVG files will be saved.
    """
    document = ap.Document(infile)
    options = apv.SvgExtractionOptions()
    options.extract_every_sub_path_to_svg = True

    page = document.pages[1]
    extractor = apv.SvgExtractor(options)
    subpaths_dir = path.join(output_dir, "subpaths")
    makedirs(subpaths_dir, exist_ok=True)
    extractor.extract(page, subpaths_dir)


def extract_list_of_elements_to_single_image(infile, outfile):
    """
    Extracts multiple vector graphic elements from a PDF page and saves them as a single SVG image.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    page = document.pages[1]
    extractor = apv.SvgExtractor()
    elements = []  # Fill this list with specific graphic elements as needed
    extractor.extract(elements, page, outfile)


def extract_single_vector_element(infile, outfile):
    """
    Extracts a specific vector graphic element (e.g., an XFormPlacement) from a PDF page and saves it as an SVG file.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    graphics_absorber = apv.GraphicsAbsorber()
    page = document.pages[1]
    graphics_absorber.visit(page)
    xform_placement = graphics_absorber.elements[1]
    if isinstance(xform_placement, apv.XFormPlacement):
        xform_placement.elements[2].save_to_svg(outfile)


def run_all_examples(data_dir=None, license_path=None):
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "Extract graphics elements",
            extract_graphics_elements,
            "sample.pdf",
            "graphics_elements.txt",
        ),
        (
            "Save vector graphics to SVG",
            save_vector_graphics_to_svg,
            "sample.pdf",
            "vector_graphics.svg",
        ),
        (
            "Extract subpaths to SVGs",
            extract_subpaths_to_svgs,
            "sample.pdf",
            "subpaths",
        ),
        (
            "Extract list of elements to single image",
            extract_list_of_elements_to_single_image,
            "sample.pdf",
            "elements_image.svg",
        ),
        (
            "Extract single vector element",
            extract_single_vector_element,
            "sample.pdf",
            "single_element.svg",
        ),
    ]

    for name, func, input_file, output_file in examples:
        try:
            args = [path.join(input_dir, input_file)]
            if output_file:
                args.append(path.join(output_dir, output_file))
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
