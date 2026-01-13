import aspose.pdf as ap
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def extract_text_from_region(infile, outfile, page_number, rect_coords):
    """
    Extract text from a specified rectangular region on a given page.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based index of the page.
        rect_coords (tuple): (llx, lly, urx, ury) coordinates of the rectangle.
        outfile (str): Output text file path.
    """
    document = ap.Document(infile)
    absorber = ap.text.TextAbsorber()
    # Set options to restrict search to the rectangle
    absorber.text_search_options.limit_to_page_bounds = True
    llx, lly, urx, ury = rect_coords
    absorber.text_search_options.rectangle = ap.Rectangle(llx, lly, urx, ury, True)
    # Accept on the specific page
    document.pages[page_number].accept(absorber)
    extracted_text = absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)


def extract_paragraphs_with_geometry(infile, outfile):
    """
    Extract paragraphs and record geometry info (rectangle / polygon) for each paragraph in a PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    absorber = ap.text.ParagraphAbsorber()
    absorber.visit(document.pages[1])

    page_markup = absorber.page_markups[0]
    with open(outfile, "w", encoding="utf-8") as tw:
        for sec_idx, section in enumerate(page_markup.sections, start=1):
            tw.write(f"Section {sec_idx}: rectangle = {str(section.rectangle)}\n")
            for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                tw.write(
                    f"  Paragraph {para_idx}: polygon = {list(paragraph.points)}\n"
                )
                # Concatenate paragraph text
                parts = []
                for line in paragraph.lines:
                    for fragment in line:
                        parts.append(fragment.text)
                    parts.append("\r\n")
                tw.write("    Text: " + "".join(parts) + "\n\n")


def run_all_examples(data_dir=None, license_path=None):
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "extract_text_from_region",
            extract_text_from_region,
            "sample.pdf",
            "sample.txt",
            1,
            (20, 450, 570, 750),
        ),
        (
            "extract_paragraphs_with_geometry",
            extract_paragraphs_with_geometry,
            "sample.pdf",
            "extract_paragraphs_with_geometry.txt",
            None,
            None,
        ),
    ]

    for name, func, input_file, output_file, page_num, coords in examples:
        try:
            args = [
                path.join(input_dir, input_file),
                path.join(output_dir, output_file),
            ]
            if page_num:
                args.append(page_num)
                args.append(coords)
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
