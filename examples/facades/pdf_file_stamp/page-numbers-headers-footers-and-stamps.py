import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def _create_formatted_text(text: str, font_size: int = 12) -> pdf_facades.FormattedText:
    """Create a reusable formatted text object for PdfFileStamp examples."""
    return pdf_facades.FormattedText(
        text,
        drawing.Color.blue,
        drawing.Color.light_gray,
        pdf_facades.FontStyle.HELVETICA_BOLD,
        pdf_facades.EncodingType.WINANSI,
        True,
        font_size,
    )


def _resolve_existing_input(input_dir: str, filename: str, *fallback_parts: str) -> str:
    """Prefer local sample_data for this module and fall back to shared repo assets."""
    candidate = path.join(input_dir, filename)
    if path.exists(candidate):
        return candidate

    repo_root = path.abspath(path.join(CURRENT_DIR, "..", "..", ".."))
    return path.join(repo_root, *fallback_parts)


def add_page_numbers_with_default_placement(infile: str, outfile: str) -> None:
    """Add page numbers with the default bottom-centered placement."""
    file_stamp = pdf_facades.PdfFileStamp()
    try:
        file_stamp.bind_pdf(infile)
        file_stamp.starting_number = 1
        file_stamp.add_page_number(_create_formatted_text("Page #"))
        file_stamp.save(outfile)
    finally:
        file_stamp.close()


def add_page_numbers_at_custom_position(infile: str, outfile: str) -> None:
    """Add page numbers at a custom X/Y position."""
    file_stamp = pdf_facades.PdfFileStamp()
    try:
        file_stamp.bind_pdf(infile)
        file_stamp.starting_number = 1
        file_stamp.add_page_number(_create_formatted_text("Page #"), 120.0, 36.0)
        file_stamp.save(outfile)
    finally:
        file_stamp.close()


def add_page_numbers_with_margins_and_alignment(infile: str, outfile: str) -> None:
    """Add page numbers with explicit margins and upper-right alignment."""
    file_stamp = pdf_facades.PdfFileStamp()
    try:
        file_stamp.bind_pdf(infile)
        file_stamp.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE
        file_stamp.starting_number = 1
        file_stamp.add_page_number(
            _create_formatted_text("Page #"),
            pdf_facades.PdfFileStamp.POS_UPPER_RIGHT,
            24.0,
            24.0,
            18.0,
            18.0,
        )
        file_stamp.save(outfile)
    finally:
        file_stamp.close()


def add_text_header_to_pdf(infile: str, outfile: str) -> None:
    """Add a text header to every page in the PDF."""
    file_stamp = pdf_facades.PdfFileStamp()
    try:
        file_stamp.bind_pdf(infile)
        file_stamp.add_header(_create_formatted_text("Approved by signing workflow"), 24.0)
        file_stamp.save(outfile)
    finally:
        file_stamp.close()


def add_image_header_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image header to every page in the PDF."""
    file_stamp = pdf_facades.PdfFileStamp()
    try:
        file_stamp.bind_pdf(infile)
        with open(image_file, "rb") as image_stream:
            file_stamp.add_header(image_stream, 18.0)
        file_stamp.save(outfile)
    finally:
        file_stamp.close()


def add_header_with_custom_margins(infile: str, outfile: str) -> None:
    """Add a text header with custom top, left, and right margins."""
    file_stamp = pdf_facades.PdfFileStamp()
    try:
        file_stamp.bind_pdf(infile)
        file_stamp.add_header(
            _create_formatted_text("Quarterly Review Header"),
            18.0,
            36.0,
            36.0,
        )
        file_stamp.save(outfile)
    finally:
        file_stamp.close()


def add_text_footer_to_pdf(infile: str, outfile: str) -> None:
    """Add a text footer to every page in the PDF."""
    file_stamp = pdf_facades.PdfFileStamp()
    try:
        file_stamp.bind_pdf(infile)
        file_stamp.add_footer(_create_formatted_text("Confidential"), 24.0)
        file_stamp.save(outfile)
    finally:
        file_stamp.close()


def add_image_footer_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image footer to every page in the PDF."""
    file_stamp = pdf_facades.PdfFileStamp()
    try:
        file_stamp.bind_pdf(infile)
        with open(image_file, "rb") as image_stream:
            file_stamp.add_footer(image_stream, 18.0)
        file_stamp.save(outfile)
    finally:
        file_stamp.close()


def add_footer_with_custom_margins(infile: str, outfile: str) -> None:
    """Add a text footer with custom bottom, left, and right margins."""
    file_stamp = pdf_facades.PdfFileStamp()
    try:
        file_stamp.bind_pdf(infile)
        file_stamp.add_footer(
            _create_formatted_text("Footer with custom margins"),
            18.0,
            36.0,
            36.0,
        )
        file_stamp.save(outfile)
    finally:
        file_stamp.close()


def add_stamp_to_pdf(infile: str, outfile: str) -> None:
    """Add a text stamp to all pages in the PDF."""
    file_stamp = pdf_facades.PdfFileStamp()
    try:
        file_stamp.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_logo(_create_formatted_text("APPROVED", 18))
        stamp.set_origin(36.0, 320.0)
        stamp.rotation = 45.0
        stamp.opacity = 0.6
        stamp.is_background = False

        file_stamp.add_stamp(stamp)
        file_stamp.save(outfile)
    finally:
        file_stamp.close()


def run_all_examples(data_dir=None, license_path=None) -> None:
    """Run all PdfFileStamp examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    input_pdf = _resolve_existing_input(
        input_dir,
        "sample.pdf",
        "sample_data",
        "facades",
        "pdf_content_editor",
        "input",
        "sample.pdf",
    )
    image_file = _resolve_existing_input(
        input_dir,
        "logo.jpg",
        "sample_data",
        "working_with_text",
        "input",
        "logo.jpg",
    )

    examples = [
        ("Add Page Numbers with Default Placement", add_page_numbers_with_default_placement, False),
        ("Add Page Numbers at Custom Position", add_page_numbers_at_custom_position, False),
        ("Add Page Numbers with Margins and Alignment", add_page_numbers_with_margins_and_alignment, False),
        ("Add Text Header to PDF", add_text_header_to_pdf, False),
        ("Add Image Header to PDF", add_image_header_to_pdf, True),
        ("Add Header with Custom Margins", add_header_with_custom_margins, False),
        ("Add Text Footer to PDF", add_text_footer_to_pdf, False),
        ("Add Image Footer to PDF", add_image_footer_to_pdf, True),
        ("Add Footer with Custom Margins", add_footer_with_custom_margins, False),
        ("Add Stamp to PDF", add_stamp_to_pdf, False),
    ]

    for name, func, needs_image in examples:
        try:
            output_file = path.join(output_dir, f"{func.__name__}.pdf")
            if needs_image:
                func(input_pdf, image_file, output_file)
            else:
                func(input_pdf, output_file)
            print(f"вњ… Success: {name}")
        except Exception as e:
            print(f"вќЊ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()