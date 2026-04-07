import sys
from os import path

import aspose.pdf.facades as pdf_facades


CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def resolve_sample_image_path(input_dir: str) -> str:
    """Resolve an image for footer examples from local or shared sample data."""
    local_image = path.join(input_dir, "sample_form_image.jpg")
    if path.exists(local_image):
        return local_image

    return path.abspath(
        path.join(
            CURRENT_DIR,
            "..",
            "..",
            "..",
            "sample_data",
            "facades",
            "form",
            "input",
            "sample_form_image.jpg",
        )
    )


def add_text_footer(infile: str, outfile: str) -> None:
    """Add a text footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_footer("Sample Footer", 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()


def add_image_footer(infile: str, image_file: str, outfile: str) -> None:
    """Add an image footer with a bottom margin."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_footer(image_file, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()


def add_footer_with_margins(infile: str, outfile: str) -> None:
    """Add a text footer with bottom, left, and right margins."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_footer("Custom Footer", 20, 20, 20)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()


def run_all_examples(data_dir=None, license_path=None):
    """Run all footer examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)
    input_file = path.join(input_dir, "sample.pdf")
    image_file = resolve_sample_image_path(input_dir)

    examples = [
        ("Add Text Footer", add_text_footer, (input_file, path.join(output_dir, "add_text_footer.pdf"))),
        (
            "Add Image Footer",
            add_image_footer,
            (input_file, image_file, path.join(output_dir, "add_image_footer.pdf")),
        ),
        (
            "Add Footer with Margins",
            add_footer_with_margins,
            (input_file, path.join(output_dir, "add_footer_with_margins.pdf")),
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
