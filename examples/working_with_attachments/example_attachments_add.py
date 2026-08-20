from os import path
import aspose.pdf as ap
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_attachments(infile, attachment_path, outfile):
    """
    Add a file as an attachment to a PDF document.

    This function opens a PDF document, attaches a specified file to it as an embedded file,
    and saves the modified PDF to a new output file.

    Args:
        infile (str): Path to the input PDF file to which the attachment will be added.
        attachment_path (str): Path to the file that will be attached to the PDF.
        outfile (str): Path where the modified PDF with the attachment will be saved.

    Returns:
        None

    Example:
        >>> add_attachments("input.pdf", "data.txt", "output.pdf")

    Notes:
        - The function uses the basename of the attachment_path as the key for the embedded file
        - A FileSpecification is created with a description "Sample text file"
        - The original PDF file is not modified; changes are saved to the outfile
    """
    with ap.Document(infile) as document:
        file_spec = ap.FileSpecification(attachment_path, "Sample text file")
        document.embedded_files.add(path.basename(attachment_path), file_spec)
        document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run attachments examples and report status.
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
            "add_attachments",
            add_attachments,
            path.join(input_dir, "sample.pdf"),
            path.join(input_dir, "file_example.txt"),
            path.join(output_dir, "sample_with_attachment.pdf"),
        ),
    ]

    for example in examples:
        name, func, *args = example
        try:
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()
