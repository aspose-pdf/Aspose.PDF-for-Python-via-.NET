import aspose.pdf as ap
from io import FileIO
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import initialize_data_dir, set_license

"""
Conversion examples demonstrating how to convert PDF files to various image formats.
"""

def convert_PDF_to_BMP(infile, outfile):
    """
    Converts a PDF file to BMP image format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output BMP file name prefix.

    Returns:
        None

    Example:
        convert_PDF_to_BMP("sample.pdf", "sample")

    Note:
        Each page is saved as a separate BMP file with 300 DPI resolution.
    """

    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)

def convert_PDF_to_EMF(infile, outfile):
    """
    Converts a PDF file to EMF (Enhanced Metafile) format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output EMF file name prefix.

    Returns:
        None

    Example:
        convert_PDF_to_EMF("sample.pdf", "sample")

    Note:
        Each page is saved as a separate EMF file with 300 DPI resolution.
    """
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)

def convert_PDF_to_GIF(infile, outfile):
    """
    Converts a PDF file to GIF image format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output GIF file name prefix.

    Returns:
        None

    Example:
        convert_PDF_to_GIF("sample.pdf", "sample")

    Note:
        Each page is saved as a separate GIF file with 300 DPI resolution.
    """
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)

def convert_PDF_to_JPEG(infile, outfile):
    """
    Converts a PDF file to JPEG image format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output JPEG file name prefix.

    Returns:
        None

    Example:
        convert_PDF_to_JPEG("sample.pdf", "sample")

    Note:
        Each page is saved as a separate JPEG file with 300 DPI resolution.
    """
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)

def convert_PDF_to_PNG(infile, outfile):
    """
    Converts a PDF file to PNG image format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output PNG file name prefix.

    Returns:
        None

    Example:
        convert_PDF_to_PNG("sample.pdf", "sample")

    Note:
        Each page is saved as a separate PNG file with 300 DPI resolution.
    """
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    device = ap.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1


def convert_PDF_to_PNG_with_default_font(infile, outfile):
    """
    Converts a PDF file to PNG image format with default font substitution.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output PNG file name prefix.

    Returns:
        None

    Example:
        convert_PDF_to_PNG_with_default_font("sample.pdf", "sample")

    Note:
        Each page is saved as a separate PNG file with 300 DPI resolution.
        Arial is used as default font when fonts are missing.
    """
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

def convert_PDF_to_SVG(infile, outfile):
    """
    Converts a PDF file to SVG (Scalable Vector Graphics) format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output SVG directory name.

    Returns:
        None

    Example:
        convert_PDF_to_SVG("sample.pdf", "sample_svg")

    Note:
        Output is not compressed to ZIP and treated as directory for multiple pages.
    """
    document = ap.Document(infile)

    save_options = ap.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(f"{outfile}.svg", save_options)

def convert_PDF_to_TIFF(infile, outfile):
    """
    Converts a PDF file to TIFF image format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output TIFF file name.

    Returns:
        None

    Example:
        convert_PDF_to_TIFF("sample.pdf", "sample.tiff")

    Note:
        Uses LZW compression, default color depth, and includes blank pages.
    """
    document = ap.Document(infile)

    resolution = ap.devices.Resolution(300)
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, f"{outfile}.tiff")

    print(infile + " converted into " + outfile)

def run_all_examples(data_dir=None, license_path=None):
    """Run PDF to Images examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("PDF to BMP", convert_PDF_to_BMP),
        ("PDF to EMF", convert_PDF_to_EMF),
        ("PDF to GIF", convert_PDF_to_GIF),
        ("PDF to JPEG", convert_PDF_to_JPEG),
        ("PDF to PNG", convert_PDF_to_PNG),
        ("PDF to PNG with default font", convert_PDF_to_PNG_with_default_font),
        ("PDF to SVG", convert_PDF_to_SVG),
        ("PDF to TIFF", convert_PDF_to_TIFF),
    ]

    input_file = path.join(input_dir, "sample.pdf")
    output_file = path.join(output_dir, "sample")
    for name, func in examples:
        try:
            func(input_file, output_file)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")

if __name__ == "__main__":
    run_all_examples()
