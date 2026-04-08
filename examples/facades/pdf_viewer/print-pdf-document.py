import sys
from os import path

import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def _create_bound_viewer(infile: str) -> pdf_facades.PdfViewer:
    viewer = pdf_facades.PdfViewer()
    viewer.bind_pdf(infile)
    viewer.auto_resize = True
    viewer.auto_rotate = True
    viewer.print_page_dialog = False
    return viewer


def print_document_with_default_settings(infile: str) -> None:
    """Print a PDF document with default settings."""
    viewer = _create_bound_viewer(infile)
    try:
        viewer.print_document()
    finally:
        viewer.close()


def print_document_with_printer_setup(infile: str) -> None:
    """Print a PDF document with the printer setup dialog."""
    viewer = _create_bound_viewer(infile)
    try:
        viewer.print_document_with_setup()
    finally:
        viewer.close()


def print_document_with_printer_settings(infile: str) -> None:
    """Print a PDF document with explicit printer settings."""
    viewer = _create_bound_viewer(infile)
    try:
        printer_settings = viewer.get_default_printer_settings()
        viewer.print_document_with_settings(printer_settings)
    finally:
        viewer.close()


def print_document_with_page_and_printer_settings(infile: str) -> None:
    """Print a PDF document with explicit page and printer settings."""
    viewer = _create_bound_viewer(infile)
    try:
        page_settings = viewer.get_default_page_settings()
        printer_settings = viewer.get_default_printer_settings()
        page_settings.landscape = True
        viewer.print_document_with_settings(page_settings, printer_settings)
    finally:
        viewer.close()


def run_all_examples(data_dir=None, license_path=None) -> None:
    """Define all document-print examples and report status when executed."""
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    infile = path.join(input_dir, "sample.pdf")
    examples = [
        ("Print Document with Default Settings", print_document_with_default_settings),
        ("Print Document with Printer Setup", print_document_with_printer_setup),
        ("Print Document with Printer Settings", print_document_with_printer_settings),
        ("Print Document with Page and Printer Settings", print_document_with_page_and_printer_settings),
    ]

    for name, func in examples:
        try:
            func(infile)
            print(f"вњ… Success: {name}")
        except Exception as e:
            print(f"вќЊ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()