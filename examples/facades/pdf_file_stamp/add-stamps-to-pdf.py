import sys
from os import path

import aspose.pdf.facades as pdf_facades


CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def add_stamp_to_pdf(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to a PDF file."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()


def run_all_examples(data_dir=None, license_path=None):
    """Run all stamp examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)
    input_file = path.join(input_dir, "sample.pdf")
    image_file = path.join(input_dir, "sample_image.png")

    examples = [
        (
            "Add Stamp to PDF",
            add_stamp_to_pdf,
            (input_file, image_file, path.join(output_dir, "add_stamp_to_pdf.pdf")),
        ),
    ]

    for name, func, args in examples:
        try:
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as error:
            print(f"❌ Failed: {name} - {error}")


if __name__ == "__main__":
    run_all_examples()
