import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def _create_viewer() -> pdf_facades.PdfViewer:
    viewer = pdf_facades.PdfViewer()
    viewer.auto_resize = True
    viewer.auto_rotate = True
    viewer.print_page_dialog = False
    return viewer


def print_large_pdf_with_default_settings(infile: str) -> None:
    """Print a large PDF file with default viewer settings."""
    viewer = _create_viewer()
    try:
        viewer.print_large_pdf(infile)
    finally:
        viewer.close()


def print_large_pdf_with_page_settings(infile: str) -> None:
    """Print a large PDF file with explicit page settings."""
    viewer = _create_viewer()
    try:
        viewer.bind_pdf(infile)
        page_settings = viewer.get_default_page_settings()
        printer_settings = viewer.get_default_printer_settings()
        page_settings.landscape = True
        viewer.print_large_pdf(infile, page_settings, printer_settings)
    finally:
        viewer.close()


def print_large_pdf_with_printer_settings(infile: str) -> None:
    """Print a large PDF file with explicit printer settings."""
    viewer = _create_viewer()
    try:
        viewer.bind_pdf(infile)
        printer_settings = viewer.get_default_printer_settings()
        viewer.print_large_pdf(infile, printer_settings)
    finally:
        viewer.close()


def print_large_pdf_from_stream(infile: str) -> None:
    """Print a large PDF file from a stream."""
    viewer = _create_viewer()
    try:
        with open(infile, "rb") as input_stream:
            page_settings = viewer.get_default_page_settings()
            printer_settings = viewer.get_default_printer_settings()
            viewer.print_large_pdf(input_stream, page_settings, printer_settings)
    finally:
        viewer.close()


def run_all_examples(data_dir=None, license_path=None) -> None:
    """Define all large-print examples and report status when executed."""
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    infile = path.join(input_dir, "sample.pdf")
    examples = [
        ("Print Large PDF with Default Settings", print_large_pdf_with_default_settings),
        ("Print Large PDF with Page Settings", print_large_pdf_with_page_settings),
        ("Print Large PDF with Printer Settings", print_large_pdf_with_printer_settings),
        ("Print Large PDF from Stream", print_large_pdf_from_stream),
    ]

    for name, func in examples:
        try:
            func(infile)
            print(f"вњ… Success: {name}")
        except Exception as e:
            print(f"вќЊ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()