import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def decode_all_pages(infile: str, output_dir: str) -> None:
    """Decode all pages of a PDF document into image files."""
    viewer = pdf_facades.PdfViewer()
    try:
        viewer.bind_pdf(infile)
        decoded_pages = viewer.decode_all_pages()

        for index, page_image in enumerate(decoded_pages, start=1):
            image_path = path.join(output_dir, f"decode_all_pages_{index}.png")
            page_image.save(image_path)
    finally:
        viewer.close()


def decode_specific_page(infile: str, outfile: str, page_number: int = 1) -> None:
    """Decode a specific PDF page into an image file."""
    viewer = pdf_facades.PdfViewer()
    try:
        viewer.bind_pdf(infile)
        page_image = viewer.decode_page(page_number)
        page_image.save(outfile)
    finally:
        viewer.close()


def run_all_examples(data_dir=None, license_path=None) -> None:
    """Run all decode examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    infile = path.join(input_dir, "sample.pdf")
    examples = [
        ("Decode All Pages", lambda: decode_all_pages(infile, output_dir)),
        ("Decode Specific Page", lambda: decode_specific_page(infile, path.join(output_dir, "decode_specific_page.png"))),
    ]

    for name, func in examples:
        try:
            func()
            print(f"вњ… Success: {name}")
        except Exception as e:
            print(f"вќЊ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()