from os import path, remove
import aspose.pdf as ap
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import initialize_data_dir, set_license

def convert_OFD_to_PDF(infile, outfile):
    load_options = ap.OfdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)


def convert_TEX_to_PDF(infile, outfile):
    load_options = ap.LatexLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)


def convert_PS_to_PDF(infile, outfile):
    load_options = ap.PsLoadOptions()

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)


def convert_EPS_to_PDF(infile, outfile):
    load_options = ap.PsLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)


def convert_EPUB_to_PDF(infile, outfile):
    load_options = ap.EpubLoadOptions()
    document = ap.Document(infile, load_options)

    document.save(outfile)
    print(infile + " converted into " + outfile)


def convert_MD_to_PDF(infile, outfile):
    load_options = ap.MdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)


def convert_TXT_to_PDF_simple(infile, outfile):
    with open(infile, "r", encoding="utf-8") as f:
        text_content = f.read()

    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment(text_content)

    page.paragraphs.add(text_fragment)
    document.save(outfile)
    print(infile + " converted into " + outfile)


def convert_TXT_to_PDF(infile, outfile):
    with open(infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(outfile)

    print(infile + " converted into " + outfile)


def convert_PCL_to_PDF(infile, outfile):
    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)


# -------------- convert_XML_to_PDF


def transform_xml_to_html(xml_file, xslt_file, html_file):
    from lxml import etree

    """
    Transform XML to HTML using XSLT and return as a stream
    """
    # Parse XML document
    xml_doc = etree.parse(xml_file)

    # Parse XSLT stylesheet
    xslt_doc = etree.parse(xslt_file)
    transform = etree.XSLT(xslt_doc)

    # Apply transformation
    result = transform(xml_doc)

    # Save result to HTML file
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(str(result))


def convert_XML_to_PDF(template, infile, outfile):
    import tempfile
    path_temp_file = path.join(tempfile.gettempdir(), "temp.html")

    load_options = ap.HtmlLoadOptions()
    transform_xml_to_html(infile, template, path_temp_file)

    document = ap.Document(path_temp_file, load_options)
    document.save(outfile)

    if path.exists(path_temp_file):
        remove(path_temp_file)

    print(infile + " converted into " + outfile)


# // -------------- convert_XML_to_PDF


def convert_XPS_to_PDF(infile, outfile):
    load_options = ap.XpsLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)


def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run other file to PDF examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Convert EPS to PDF", convert_EPS_to_PDF, "sample.eps"),
        ("Convert EPUB to PDF", convert_EPUB_to_PDF, "sample.epub"),
        ("Convert MD to PDF", convert_MD_to_PDF, "sample.md"),
        ("Convert OFD to PDF", convert_OFD_to_PDF, "sample.ofd"),
        ("Convert PCL to PDF", convert_PCL_to_PDF, "sample_pcl.txt"),
        # ("Convert PS_to_PDF", convert_PS_to_PDF, "sample_1.ps"),
        ("Convert TXT to_PDF simple", convert_TXT_to_PDF_simple, "sample_simple.txt"),
        ("Convert XPS to PDF", convert_XPS_to_PDF, "sample.oxps"),
        ("Convert TXT to PDF", convert_TXT_to_PDF, "sample.txt"),
        ("Convert XML to PDF", convert_XML_to_PDF, ["sample.xslt", "sample.xml"]),
        ("Convert XSLFO to PDF", convert_XSLFO_to_PDF, ["demo.xslt", "demo.xml"]),
    ]

    for name, func, i in examples:
        output_path = path.join(output_dir, f"{func.__name__}.pdf")
        try:
            if isinstance(i, str):
                input_path = path.join(input_dir, i)
                func(input_path, output_path)
            else:
                input_paths = [path.join(input_dir, f) for f in i]
                func(input_paths[0],input_paths[1], output_path)
            print(f"✅ Success: {name} completed.")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")

    print(f"\nAll other file to pdf creation examples finished. Check output in {output_dir}")

if __name__ == "__main__":
    run_all_examples()
