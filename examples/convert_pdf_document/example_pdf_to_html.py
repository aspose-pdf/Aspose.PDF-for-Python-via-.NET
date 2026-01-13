import aspose.pdf as ap
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import initialize_data_dir, set_license

"""
Conversion examples demonstrating how to convert PDF files to HTML with various options.
"""


def convert_PDF_to_HTML(infile, outfile):
    """
    Converts a PDF file to basic HTML format.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output HTML file name.

    Returns:
        None

    Example:
        convert_PDF_to_HTML("sample.pdf", "sample.html")

    Note:
        Uses default HTML save options.
    """
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_HTML_storing_images(infile, outfile):
    """
    Converts a PDF file to HTML format and stores images in a separate folder.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output HTML file name.

    Returns:
        None

    Example:
        convert_PDF_to_HTML_storing_images("sample.pdf", "sample_images.html")

    Note:
        Images are stored in the data directory.
    """
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "images")
    save_options.special_folder_for_all_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_HTML_multi_page(infile, outfile):
    """
    Converts a PDF file to HTML format with multiple pages.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output HTML file name.

    Returns:
        None

    Example:
        convert_PDF_to_HTML_multi_page("sample.pdf", "sample_multipage.html")

    Note:
        Each PDF page is saved as a separate HTML file.
    """
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_HTML_storing_svg(infile, outfile):
    """
    Converts a PDF file to HTML format and stores SVG images in a separate folder.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output HTML file name.

    Returns:
        None

    Example:
        convert_PDF_to_HTML_storing_svg("sample.pdf", "sample_svg.html")

    Note:
        SVG images are stored in the data directory.
    """
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_HTML_compress_svg(infile, outfile):
    """
    Converts a PDF file to HTML format and compresses SVG images.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output HTML file name.

    Returns:
        None

    Example:
        convert_PDF_to_HTML_compress_svg("sample.pdf", "sample_compress.html")

    Note:
        SVG compression reduces file size while maintaining quality.
    """
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    save_options.compress_svg_graphics_if_any = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_HTML_PNG_background(infile, outfile):
    """
    Converts a PDF file to HTML format with PNG background mode.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output HTML file name.

    Returns:
        None

    Example:
        convert_PDF_to_HTML_PNG_background("sample.pdf", "sample_png.html")

    Note:
        Raster images are saved as embedded parts of PNG page backgrounds.
    """

    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.raster_images_saving_mode = (
        ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    )
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_HTML_body_content(infile, outfile):
    """
    Converts a PDF file to HTML format with body content only.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output HTML file name.

    Returns:
        None

    Example:
        convert_PDF_to_HTML_body_content("sample.pdf", "sample_body.html")

    Note:
        Generates only the HTML body content without <html> and <head> tags.
    """
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.html_markup_generation_mode = (
        ap.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    )
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_HTML_transparent_text_rendering(infile, outfile):
    """
    Converts a PDF file to HTML format with transparent text rendering.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output HTML file name.

    Returns:
        None

    Example:
        convert_PDF_to_HTML_transparent_text_rendering("sample.pdf", "sample_transparent.html")

    Note:
        Transparent and shadowed texts are rendered transparently in the HTML output.
    """
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_HTML_document_layers_rendering(infile, outfile):
    """
    Converts a PDF file to HTML format with document layers rendering.

    Args:
        infile (str): Input PDF file name.
        outfile (str): Output HTML file name.

    Returns:
        None

    Example:
        convert_PDF_to_HTML_document_layers_rendering("sample.pdf", "sample_layers.html")

    Note:
        PDF marked content is converted to HTML layers for better structure preservation.
    """
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run PDF to HTML examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("PDF to HTML", convert_PDF_to_HTML, "sample.html"),
        (
            "PDF to HTML storing images",
            convert_PDF_to_HTML_storing_images,
            "sample_images.html",
        ),
        (
            "PDF to HTML multi-page",
            convert_PDF_to_HTML_multi_page,
            "sample_multipage.html",
        ),
        ("PDF to HTML storing SVG",
         convert_PDF_to_HTML_storing_svg,
         "sample_svg.html"),
        (
            "PDF to HTML compress SVG",
            convert_PDF_to_HTML_compress_svg,
            "sample_compress.html",
        ),
        (
            "PDF to HTML PNG background",
            convert_PDF_to_HTML_PNG_background,
            "sample_png.html",
        ),
        (
            "PDF to HTML body content",
            convert_PDF_to_HTML_body_content,
            "sample_body.html",
        ),
        (
            "PDF to HTML transparent text",
            convert_PDF_to_HTML_transparent_text_rendering,
            "sample_transparent.html",
        ),
        (
            "PDF to HTML document layers",
            convert_PDF_to_HTML_document_layers_rendering,
            "sample_layers.html",
        ),
    ]

    input_file = path.join(input_dir, "sample.pdf")
    for name, func, o in examples:
        output_file = path.join(output_dir, o)
        try:
            func(input_file, output_file)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")

if __name__ == "__main__":
    
    run_all_examples()
