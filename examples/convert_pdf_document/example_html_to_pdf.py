import aspose.pdf as ap
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import initialize_data_dir, set_license


def convert_HTML_to_PDF(infile, outfile):
    """
    Converts an HTML file to PDF format.

    Args:
        infile (str): Input HTML file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_HTML_to_PDF("sample.html", "sample_python.pdf")

    Note:
        Uses SCALE_TO_PAGE_WIDTH layout option for better fit.
    """
    load_options = ap.HtmlLoadOptions()
    load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)


def convert_HTML_to_PDF_media_type(infile, outfile):
    """
    Converts an HTML file to PDF format with screen media type.

    Args:
        infile (str): Input HTML file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_HTML_to_PDF_media_type("sample_media.html", "sample_media.pdf")

    Note:
        Sets HTML media type to SCREEN for CSS media queries.
    """
    load_options = ap.HtmlLoadOptions()
    load_options.html_media_type = ap.HtmlMediaType.SCREEN
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)


def convert_HTML_to_PDF_priority_css_page_rule(infile, outfile):
    """
    Converts an HTML file to PDF format with priority CSS page rule.

    Args:
        infile (str): Input HTML file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_HTML_to_PDF_priority_css_page_rule("sample.html", "sample_css.pdf")

    Note:
        CSS page rules do not take priority over default PDF page settings (is_priority_css_page_rule=False).
    """
    load_options = ap.HtmlLoadOptions()
    load_options.is_priority_css_page_rule = False
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)


def convert_HTML_to_PDF_embed_fonts(infile, outfile):
    """
    Converts an HTML file to PDF format with embedded fonts.

    Args:
        infile (str): Input HTML file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_HTML_to_PDF_embed_fonts("sample.html", "sample_fonts.pdf")

    Note:
        Embeds all fonts used in HTML for better portability.
    """
    load_options = ap.HtmlLoadOptions()
    load_options.is_embed_fonts = True
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)


def convert_HTML_to_PDF_render_content_to_same_page(infile, outfile):
    """
    Converts an HTML file to PDF format rendering all content to a single page.

    Args:
        infile (str): Input HTML file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_HTML_to_PDF_render_content_to_same_page("sample.html", "sample_single.pdf")

    Note:
        All HTML content is rendered to a single PDF page regardless of length.
    """
    options = ap.HtmlLoadOptions()
    options.is_render_to_single_page = True

    doc = ap.Document(infile, options)
    doc.save(outfile)


def convert_HTML_to_PDF_render_html_with_svg_data(infile, outfile):
    """
    Converts an HTML file with SVG data to PDF format.

    Args:
        infile (str): Input HTML file name with SVG.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_HTML_to_PDF_render_html_with_svg_data("sample_svg2.html", "sample_svg.pdf")

    Note:
        This feature is not implemented yet.
    """
    raise NotImplementedError("HTML with SVG to PDF conversion is not implemented yet")


def convert_WebPage_to_PDF(infile, outfile):
    """
    Converts a web page URL to PDF format.

    Args:
        infile (str): URL of the web page.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_WebPage_to_PDF("https://docs.aspose.com/pdf/python-net/", "sample_page.pdf")

    Note:
        This feature is not implemented yet. Requires requests library and temp file handling.
    """
    raise NotImplementedError("Web page to PDF conversion is not implemented yet")


def convert_MHTML_to_PDF(infile, outfile):
    """
    Converts an MHTML file to PDF format.

    Args:
        infile (str): Input MHTML file name.
        outfile (str): Output PDF file name.

    Returns:
        None

    Example:
        convert_MHTML_to_PDF("sample.mhtml", "sample_mhtml.pdf")

    Note:
        MHTML is a web page archive format containing HTML and embedded resources.
        Page size is set to A4 (842x1191 points).
    """
    load_options = ap.MhtLoadOptions()
    load_options.page_info.width = 842
    load_options.page_info.height = 1191
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run HTML to PDF examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("HTML to PDF",
         convert_HTML_to_PDF,
         "sample.html",
         "sample_HTML_to_PDF.pdf"),
        (
            "HTML to PDF media type",
            convert_HTML_to_PDF_media_type,
            "sample_media.html",
            "sample_media.pdf",
        ),
        (
            "HTML to PDF CSS priority",
            convert_HTML_to_PDF_priority_css_page_rule,
            "sample.html",
            "sample_css.pdf",
        ),
        (
            "HTML to PDF embed fonts",
            convert_HTML_to_PDF_embed_fonts,
            "sample.html",
            "sample_fonts.pdf",
        ),
        (
            "HTML to PDF single page",
            convert_HTML_to_PDF_render_content_to_same_page,
            "sample.html",
            "sample_single.pdf",
        ),
        ("MHTML to PDF", convert_MHTML_to_PDF, "sample.mhtml", "sample_mhtml.pdf"),
    ]

    for title, func, i, o in examples:
        infile_file_name = path.join(input_dir, i)
        outfile_file_name = path.join(output_dir, o)
        try:
            func(infile_file_name, outfile_file_name)
            print(f"✅ Success: {title}")
        except Exception as e:
            print(f"❌ Failed: {title} - {e}")


if __name__ == "__main__":
    run_all_examples()
