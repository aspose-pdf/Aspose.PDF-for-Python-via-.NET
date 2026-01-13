import sys
import aspose.pdf as ap
from os import path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def import_export(infile, outfile):
    """
    Import annotations from one PDF document and export them to a new PDF document.

    Args:
        infile (str): The name of the input PDF file containing annotations.
        outfile (str): The name of the output PDF file where annotations will be exported.

    Returns:
        None

    Example:
        >>> import_export("sample_annotations.pdf", "sample_impex.pdf")

    Note:
        This function copies all annotations from the first page of the source document
        to a new page in the destination document.
    """
    source_document = ap.Document(infile)
    destination_document = ap.Document()

    page = destination_document.pages.add()

    for annot in source_document.pages[1].annotations:
        page.annotations.add(annot, True)

    destination_document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """
    Run annotation import/export examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "Import Export",
            import_export,
            ("sample_annotations.pdf", "sample_impex.pdf"),
        ),
    ]

    for name, func, args in examples:
        input_file_name = path.join(input_dir, args[0])
        output_file_name = path.join(output_dir, args[1])
        try:
            if len(args) > 2:
                func(input_file_name, output_file_name, args[2])
            else:
                func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
