import aspose.pdf as ap
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import initialize_data_dir, set_license

def convert_PDFA_to_PDF(infile, outfile):
    """
    Convert PDF/A to standard PDF.

    Args:
        infile (str): Input PDF/A filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        convert_PDFA_to_PDF("convert_PDF_to_PDFA.pdf", "convert_PDFA_to_PDF.pdf")

    Note:
        Removes PDF/A compliance using remove_pdfa_compliance().
    """
    document = ap.Document(infile)
    document.remove_pdfa_compliance()
    document.save(outfile)

def convert_PDFUA_to_PDF(infile, outfile):
    """
    Convert PDF/UA to standard PDF.

    Args:
        infile (str): Input PDF/UA filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        convert_PDFUA_to_PDF("sample_ua.pdf", "convert_PDFUA_to_PDF.pdf")

    Note:
        Removes PDF/UA compliance using remove_pdf_ua_compliance().
    """
    document = ap.Document(infile)
    document.remove_pdf_ua_compliance()
    document.save(outfile)

def run_all_examples(data_dir=None, license_path=None):
    """Run PDF/X to PDF examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("PDFA to PDF", convert_PDFA_to_PDF, "sample_a.pdf", "convert_PDFA_to_PDF.pdf"),
        ("PDFUA to PDF", convert_PDFUA_to_PDF, "sample_ua.pdf", "convert_PDFUA_to_PDF.pdf"),
    ]

    for name, func, i, o in examples:
        try:
            input_file_name = path.join(input_dir, i)
            output_file_name = path.join(output_dir, o)
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()

