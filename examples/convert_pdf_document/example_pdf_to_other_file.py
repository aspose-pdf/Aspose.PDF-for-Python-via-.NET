import aspose.pdf as ap
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import initialize_data_dir, set_license

"""
Conversion examples demonstrating how to convert PDF files to other formats.
"""


def convert_PDF_to_EPUB(infile, outfile):
    """
    Converts a PDF file to EPUB format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output EPUB file name.

    Returns:
        None

    Example:
        convert_PDF_to_EPUB("sample.pdf", "sample.epub")

    Note:
        Uses FLOW content recognition mode for better text reflow.
    """
    document = ap.Document(infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_TeX(infile, outfile):
    """
    Converts a PDF file to TeX/LaTeX format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output TeX file name.

    Returns:
        None

    Example:
        convert_PDF_to_TeX("sample.pdf", "sample.tex")

    Note:
        Generates LaTeX markup from PDF content.
    """
    document = ap.Document(infile)
    save_options = ap.LaTeXSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_TXT(infile, outfile):
    """
    Converts a PDF file to plain text format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output TXT file name.

    Returns:
        None

    Example:
        convert_PDF_to_TXT("sample.pdf", "sample.txt")

    Note:
        Extracts text from the first page only using TextDevice.
    """
    document = ap.Document(infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], outfile)

    print(infile + " converted into " + outfile)


def convert_PDF_to_XPS(infile, outfile):
    """
    Converts a PDF file to XPS format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output XPS file name.

    Returns:
        None

    Example:
        convert_PDF_to_XPS("sample.pdf", "sample.xps")

    Note:
        Uses new imaging engine for improved quality.
    """
    document = ap.Document(infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_MD(infile, outfile):
    """
    Converts a PDF file to Markdown format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output Markdown file name.

    Returns:
        None

    Example:
        convert_PDF_to_MD("sample.pdf", "sample.md")

    Note:
        Stores extracted images in 'images' subdirectory with HTML tags.
    """
    document = ap.Document(infile)
    save_options = ap.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_MobiXML(infile, outfile):
    """
    Converts a PDF file to MobiXML format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output MobiXML file name.

    Returns:
        None

    Example:
        convert_PDF_to_MobiXML("sample.pdf", "sample.mobi")

    Note:
        MobiXML is used for Kindle e-book format.
    """
    document = ap.Document(infile)
    document.save(outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run PDF to other file examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("PDF to EPUB", convert_PDF_to_EPUB, "sample.epub"),
        ("PDF to MD", convert_PDF_to_MD, "sample.md"),
        ("PDF to TeX", convert_PDF_to_TeX, "sample.tex"),
        ("PDF to TXT", convert_PDF_to_TXT, "sample.txt"),
        ("PDF to XPS", convert_PDF_to_XPS, "sample.xps"),
        ("PDF to MobiXML", convert_PDF_to_MobiXML, "sample.mobi"),
    ]

    input_file = path.join(input_dir, "sample.pdf")
    for name, func, o in examples:
        output_file = path.join(output_dir, f"{o}")
        try:
            func(input_file, output_file)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":

    run_all_examples()
