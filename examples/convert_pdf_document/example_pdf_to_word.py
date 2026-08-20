from os import path
import aspose.pdf as ap
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import initialize_data_dir, set_license


def convert_PDF_to_DOC(infile, outfile):
    """
    Convert PDF to Microsoft Word DOC format.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output DOC filename

    Returns:
        None

    Example:
        convert_PDF_to_DOC("sample.pdf", "sample_python.doc")
    """
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_PDF_to_DOCX(infile, outfile):
    """
    Convert PDF to Microsoft Word DOCX format.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output DOCX filename

    Returns:
        None

    Example:
        convert_PDF_to_DOCX("sample.pdf", "sample_python.docx")
    """
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    document.save(outfile, save_options)


def convert_PDF_to_DOCX_advanced(infile, outfile):
    """
    Convert PDF to Microsoft Word DOCX format.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output DOCX filename

    Returns:
        None

    Example:
        convert_PDF_to_DOCX("sample.pdf", "sample_python.docx")
    """
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    save_options.mode = ap.DocSaveOptions.RecognitionMode.ENHANCED_FLOW
    document.save(outfile, save_options)


def run_all_examples(data_dir=None, license_path=None):
    """Run PDF to Word examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("PDF to DOC", convert_PDF_to_DOC, "PDF_to_DOC.doc"),
        ("PDF to DOCX", convert_PDF_to_DOCX, "PDF_to_DOCX.docx"),
        ("PDF to DOCX adv", convert_PDF_to_DOCX_advanced, "PDF_to_DOCX_adv.docx"),
    ]

    for name, func, o in examples:
        infile = path.join(input_dir, "sample.pdf")
        outfile = path.join(output_dir, o)
        try:
            func(infile, outfile)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
