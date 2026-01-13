import aspose.pdf as ap
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import initialize_data_dir, set_license

def convert_PDF_to_PPTX(infile, outfile):
    """
    Convert PDF to PowerPoint PPTX format.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PPTX filename

    Returns:
        None

    Example:
        convert_PDF_to_PPTX("sample.pdf", "sample_python.pptx")
    """
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)

def convert_PDF_to_PPTX_slides_as_images(infile, outfile):
    """
    Convert PDF to PPTX with slides as images.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PPTX filename

    Returns:
        None

    Example:
        convert_PDF_to_PPTX_slides_as_images("sample.pdf", "sample_python.pptx")

    Note:
        Each PDF page is converted to an image slide.
    """
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(outfile, save_options)


def convert_PDF_to_PPTX_image_resolution(infile, outfile):
    """
    Convert PDF to PPTX with custom image resolution.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PPTX filename

    Returns:
        None

    Example:
        convert_PDF_to_PPTX_image_resolution("sample.pdf", "sample_python.pptx")

    Note:
        Sets image resolution to 300 DPI.
    """
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(outfile, save_options)


def run_all_examples(data_dir=None, license_path=None):
    """Run PDF to PowerPoint examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("PDF to PPTX", convert_PDF_to_PPTX, "PDF_to_PPTX_basic.pptx"),
        (
            "PDF to PPTX as images",
            convert_PDF_to_PPTX_slides_as_images,
            "PDF_to_PPTX_images.pptx",
        ),
        (
            "PDF to PPTX with resolution",
            convert_PDF_to_PPTX_image_resolution,
            "PDF_to_PPTX_image_res.pptx",
        ),
    ]

    for name, func, o in examples:
        input_file_name = path.join(input_dir, "sample.pdf")
        output_file_name = path.join(output_dir, o)
        try:
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
