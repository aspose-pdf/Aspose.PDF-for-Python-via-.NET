import aspose.pdf as ap
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import initialize_data_dir, set_license

"""
Conversion examples demonstrating how to convert various image formats to PDF.
Note: DICOM conversion requires pydicom library (pip install pydicom).
"""


def convert_BMP_to_PDF(infile, outfile):
    """
    Converts a BMP image file to PDF format.

    Args:
        infile (str): Input BMP file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_BMP_to_PDF("sample.bmp", "sample_python.pdf")

    Note:
        Image is fitted to A4 page size (595x842 points).
    """
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)


def convert_CGM_to_PDF(infile, outfile):
    """
    Converts a CGM (Computer Graphics Metafile) file to PDF format.

    Args:
        infile (str): Input CGM file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_CGM_to_PDF("sample.cgm", "sample_python.pdf")

    Note:
        Uses CgmLoadOptions for proper file interpretation.
    """
    options = ap.CgmLoadOptions()
    document = ap.Document(infile, options)
    document.save(outfile)

    print(infile + " converted into " + outfile)


def convert_DICOM_to_PDF(infile, outfile):
    """
    Converts a DICOM medical imaging file to PDF format.

    Args:
        infile (str): Input DICOM file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_DICOM_to_PDF("sample.dicom", "sample_python.pdf")

    Note:
        Requires pydicom library. Page size is set to match image dimensions.
    """
    # Load the DICOM file
    import pydicom

    dicom_file = pydicom.dcmread(infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = ap.Document()
    page = document.pages.add()
    image = ap.Image()
    image.file_type = ap.ImageFileType.DICOM
    image.file = infile

    # Set page dimensions
    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(outfile)
    print(infile + " converted into " + outfile)


def convert_EMF_to_PDF(infile, outfile):
    """
    Converts an EMF (Enhanced Metafile) file to PDF format.

    Args:
        infile (str): Input EMF file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_EMF_to_PDF("sample.emf", "sample_python.pdf")

    Note:
        Image is fitted to A4 page size (595x842 points).
    """
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(infile, rectangle)

    # Save the file into PDF format
    document.save(outfile)
    print(infile + " converted into " + outfile)


def convert_GIF_to_PDF(infile, outfile):
    """
    Converts a GIF image file to PDF format.

    Args:
        infile (str): Input GIF file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_GIF_to_PDF("sample.gif", "sample_python.pdf")

    Note:
        Image is fitted to A4 page size (595x842 points).
    """
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)


def convert_JPEG_to_PDF(infile, outfile):
    """
    Converts a JPEG image file to PDF format.

    Args:
        infile (str): Input JPEG file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_JPEG_to_PDF("sample.jpg", "sample_python.pdf")

    Note:
        Image is fitted to A4 page size (595x842 points).
    """
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)


def convert_PNG_to_PDF(infile, outfile):
    """
    Converts a PNG image file to PDF format.

    Args:
        infile (str): Input PNG file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_PNG_to_PDF("sample.png", "sample_python.pdf")

    Note:
        Image is fitted to A4 page size (595x842 points).
    """
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)


def convert_SVG_to_PDF(infile, outfile):
    """
    Converts an SVG (Scalable Vector Graphics) file to PDF format.

    Args:
        infile (str): Input SVG file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_SVG_to_PDF("sample.svg", "sample_python.pdf")

    Note:
        Uses SvgLoadOptions for proper file interpretation.
    """
    load_options = ap.SvgLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)


def convert_TIFF_to_PDF(infile, outfile):
    """
    Converts a TIFF image file to PDF format.

    Args:
        infile (str): Input TIFF file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_TIFF_to_PDF("sample.tiff", "sample_python.pdf")

    Note:
        Image is fitted to A4 page size (595x842 points).
    """
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)


def convert_CDR_to_PDF(infile, outfile):
    """
    Converts a CDR (CorelDRAW) file to PDF format.

    Args:
        infile (str): Input CDR file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_CDR_to_PDF("sample.cdr", "sample_python.pdf")

    Note:
        Uses CdrLoadOptions for proper file interpretation.
    """
    load_options = ap.CdrLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run Images to PDF examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("BMP to PDF", convert_BMP_to_PDF, "sample.bmp"),
        ("CGM to PDF", convert_CGM_to_PDF, "sample.cgm"),
        ("EMF to PDF", convert_EMF_to_PDF, "sample.emf"),
        ("GIF to PDF", convert_GIF_to_PDF, "sample.gif"),
        ("JPEG to PDF", convert_JPEG_to_PDF, "sample.jpg"),
        ("PNG to PDF", convert_PNG_to_PDF, "sample.png"),
        ("SVG to PDF", convert_SVG_to_PDF, "sample.svg"),
        ("TIFF to PDF", convert_TIFF_to_PDF, "sample.tiff"),
        ("CDR to PDF", convert_CDR_to_PDF, "sample.cdr"),
    ]

    for name, func, i in examples:
        input_file_name = path.join(input_dir, i)
        output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
        try:
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
    # Note: DICOM conversion intentionally excluded from run_all_examples due to pydicom dependency
