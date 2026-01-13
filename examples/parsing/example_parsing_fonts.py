import aspose.pdf as ap
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir



def extract_fonts(infile):
    """
    Extract and print font names from PDF.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_fonts("sample.pdf")

    Note:
        Prints font names to console using font_utilities.
    """

    document = ap.Document(infile)
    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)


def run_all_examples(data_dir=None, license_path=None):
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [("Extract fonts", extract_fonts, "sample.pdf", None)]

    for name, func, input_file, output_file in examples:
        try:
            args = [path.join(input_dir, input_file)]
            if output_file:
                args.append(path.join(output_dir, output_file))
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
