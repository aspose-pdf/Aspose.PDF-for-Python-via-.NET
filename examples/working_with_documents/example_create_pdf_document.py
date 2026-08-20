import aspose.pdf as ap
import io
import sys
from os import path
from pathlib import Path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir  # noqa: E402


def create_new_document(input_pdf, output_pdf):
    """Create a simple PDF with a single “Hello World!” page."""
    document = ap.Document()
    page = document.pages.add()
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    document.save(output_pdf)


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
        ("Create a Searchable PDF document", create_searchable_document),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}.pdf")
            if func == create_searchable_document:
                image_path = path.join(output_dir, "create_searchable_document.png")
                func(input_file_name, output_file_name, image_path)
            else:
                func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll PDF creation examples finished.")


if __name__ == "__main__":
    run_all_examples()
