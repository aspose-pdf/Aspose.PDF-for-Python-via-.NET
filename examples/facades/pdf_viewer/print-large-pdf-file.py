import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license


def _create_viewer(infile: str) -> pdf_facades.PdfViewer:
    """Create a PdfViewer configured and bound to a PDF file.
    
    Args:
        infile (str): Path to the PDF file to bind.
    
    Returns:
        pdf_facades.PdfViewer: Configured and bound viewer with optimal settings for large files.
    """
    viewer = pdf_facades.PdfViewer()
    viewer.auto_resize = True
    viewer.auto_rotate = True
    viewer.auto_rotate_mode = pdf_facades.AutoRotateMode.NONE
    viewer.print_page_dialog = False
    viewer.print_as_image = False
    viewer.print_as_grayscale = False
    viewer.use_intermidiate_image = True
    viewer.printer_job_name = "Aspose.PDF Large File Print"
    viewer.coordinate_type = ap.PageCoordinateType.CROP_BOX
    viewer.bind_pdf(infile)
    return viewer


def print_large_pdf_with_default_settings(infile: str) -> None:
    """Print a large PDF file with default viewer settings.
    
    Args:
        infile (str): Path to the PDF file to print.
    """
    viewer = _create_viewer(infile)
    try:
        viewer.print_large_pdf(infile)
        print(f"Print status: {viewer.print_status}")
    finally:
        viewer.close()


def print_large_pdf_with_printer_settings(infile: str) -> None:
    """Print a large PDF file with explicit printer settings.
    
    Args:
        infile (str): Path to the PDF file to print.
    """
    viewer = _create_viewer(infile)
    try:
        printer_settings = viewer.get_default_printer_settings()
        viewer.print_large_pdf(infile, printer_settings)
        print(f"Print status: {viewer.print_status}")
    finally:
        viewer.close()


def print_large_pdf_with_page_and_printer_settings(infile: str) -> None:
    """Print a large PDF file with explicit page and printer settings.
    
    Args:
        infile (str): Path to the PDF file to print.
    """
    viewer = _create_viewer(infile)
    try:
        page_settings = viewer.get_default_page_settings()
        printer_settings = viewer.get_default_printer_settings()
        page_settings.landscape = True
        viewer.print_large_pdf(infile, page_settings, printer_settings)
        print(f"Print status: {viewer.print_status}")
    finally:
        viewer.close()


def print_large_pdf_from_stream(infile: str) -> None:
    """Print a large PDF file from a stream with explicit settings.
    
    Args:
        infile (str): Path to the PDF file to print.
    """
    viewer = _create_viewer(infile)
    try:
        with open(infile, "rb") as input_stream:
            page_settings = viewer.get_default_page_settings()
            printer_settings = viewer.get_default_printer_settings()
            viewer.print_large_pdf(input_stream, page_settings, printer_settings)
            print(f"Print status: {viewer.print_status}")
    finally:
        viewer.close()


def run_all_examples(data_dir=None, license_path=None) -> None:
    """Execute all large-print examples and report status.
    
    Args:
        data_dir (str, optional): Custom data directory path. Defaults to None.
        license_path (str, optional): Path to Aspose license file. Defaults to None.
    """
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    infile = path.join(input_dir, "sample.pdf")
    examples = [
        ("Print Large PDF with Default Settings", print_large_pdf_with_default_settings),
        ("Print Large PDF with Printer Settings", print_large_pdf_with_printer_settings),
        ("Print Large PDF with Page and Printer Settings", print_large_pdf_with_page_and_printer_settings),
        ("Print Large PDF from Stream", print_large_pdf_from_stream),
    ]

    for name, func in examples:
        try:
            func(infile)
            print(f"✅ Success: {name}")
        except Exception as error:
            print(f"❌ Failed: {name} - {error}")


if __name__ == "__main__":
    run_all_examples()
