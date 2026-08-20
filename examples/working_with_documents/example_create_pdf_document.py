import io
import sys
from os import path
from pathlib import Path

import aspose.pdf as ap
import pytesseract

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir  # noqa: E402


def create_new_document(output_pdf):
    """Create a simple PDF with a single “Hello World!” page."""
    document = ap.Document()
    page = document.pages.add()
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    document.save(output_pdf)

def create_searchable_pdf(input_pdf, output_pdf):
    """Convert a PDF page to an image and use OCR to produce a searchable PDF."""
    temp_image_path = "temp_image.png"
    page_number = 1
    image_stream = io.FileIO(temp_image_path, "w")
    try:
        document = ap.Document(input_pdf)
        resolution = ap.devices.Resolution(300)
        png_device = ap.devices.PngDevice(resolution)
        png_device.process(document.pages[page_number], image_stream)
        image_stream.close()
        pdf = pytesseract.image_to_pdf_or_hocr(temp_image_path, extension="pdf")
        document = ap.Document(io.BytesIO(pdf))
        document.save(output_pdf)
    finally:
        image_file = Path(temp_image_path)
        image_file.unlink(missing_ok=True)


def create_searchable_document(infile, outfile, image_file_path, page_number=1):
    """Use optical character recognition (OCR) to create a searchable PDF document.

    Args:
        infile (str): The path to the input PDF file.
        outfile (str): The path to the output searchable PDF file.
        image_file_path (str): The path to the intermediate image file.
        page_number (int): The page number to process.

    Returns:
        None
    """

    # Requires: pip install pytesseract
    # Also ensure the Tesseract OCR engine is installed and available on your system PATH.
    import pytesseract

    try:
        image_stream = io.FileIO(image_file_path, 'x')
        document = ap.Document(infile)
        resolution = ap.devices.Resolution(300)
        png_device = ap.devices.PngDevice(resolution)
        png_device.process(document.pages[page_number], image_stream)
        image_stream.close()
        pdf = pytesseract.image_to_pdf_or_hocr(image_file_path, extension='pdf')
        document = ap.Document(io.BytesIO(pdf))
        document.save(outfile)
    finally:
        image_file = Path(image_file_path)
        image_file.unlink(missing_ok=True)


def run_all_examples(data_dir=None, license_path=None):
    """Run PDF creation examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Create new document", create_new_document),
        ("Create searchable PDF", create_searchable_pdf),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}.pdf")
            if func.__name__ == "create_new_document":
                func(output_file_name)
            else:
                func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll PDF creation examples finished.")


if __name__ == "__main__":
    run_all_examples()
