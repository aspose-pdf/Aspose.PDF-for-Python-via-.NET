import sys
from os import path

import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def _create_text_logo(text: str) -> pdf_facades.FormattedText:
    """Create formatted text for text stamp examples."""
    return pdf_facades.FormattedText(
        text,
        drawing.Color.blue,
        drawing.Color.light_gray,
        pdf_facades.FontStyle.HELVETICA_BOLD,
        pdf_facades.EncodingType.WINANSI,
        True,
        14,
    )


def _resolve_image_file(input_dir: str) -> str:
    """Resolve an image asset for stamp examples."""
    local_image = path.join(input_dir, "logo.jpg")
    if path.exists(local_image):
        return local_image

    repo_root = path.abspath(path.join(CURRENT_DIR, "..", "..", ".."))
    return path.join(repo_root, "sample_data", "working_with_text", "input", "logo.jpg")


def add_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()


def add_pdf_page_as_stamp(infile: str, stamp_pdf: str, outfile: str) -> None:
    """Add the first page of another PDF as a stamp."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_pdf(stamp_pdf, 1)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()


def add_text_stamp(infile: str, outfile: str) -> None:
    """Add a text stamp to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_logo(_create_text_logo("Approved by signing workflow"))

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()


def position_stamp_on_page(infile: str, image_file: str, outfile: str) -> None:
    """Place an image stamp at a custom position on the page."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.set_origin(36, 300)
        stamp.rotation = 30.0

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()


def resize_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Resize an image stamp before adding it to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.set_image_size(120, 60)
        stamp.set_origin(36, 220)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()


def run_all_examples(data_dir=None, license_path=None) -> None:
    """Run all stamp examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    input_pdf = path.join(input_dir, "sample.pdf")
    image_file = _resolve_image_file(input_dir)

    examples = [
        ("Add Image Stamp", add_image_stamp),
        ("Add PDF Page as Stamp", add_pdf_page_as_stamp),
        ("Add Text Stamp", add_text_stamp),
        ("Position Stamp on Page", position_stamp_on_page),
        ("Resize Image Stamp", resize_image_stamp),
    ]

    for name, func in examples:
        try:
            output_file = path.join(output_dir, f"{func.__name__}.pdf")
            if func.__name__ in ("add_image_stamp", "position_stamp_on_page", "resize_image_stamp"):
                func(input_pdf, image_file, output_file)
            elif func.__name__ == "add_pdf_page_as_stamp":
                func(input_pdf, input_pdf, output_file)
            else:
                func(input_pdf, output_file)
            print(f"вњ… Success: {name}")
        except Exception as e:
            print(f"вќЊ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()