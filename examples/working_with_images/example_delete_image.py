import sys
import aspose.pdf as ap
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def delete_image(infile, outfile):
    """
    Delete image from PDF document.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        delete_image("sample.pdf", "deleted_image.pdf")

    Note:
        Deletes first image from first page.
    """

    document = ap.Document(infile)
    document.pages[1].resources.images.delete(1)
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run delete image examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Delete image", delete_image),
    ]

    input_file_name = path.join(input_dir, "sample_delete.pdf")
    for name, func in examples:
        try:
            output_file_name = path.join(output_dir, f"{name}_out.pdf")
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
