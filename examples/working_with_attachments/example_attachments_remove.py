from os import path
import aspose.pdf as ap
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_attachment(infile, attachment_name, outfile):
    """
    Remove a specific attachment from the PDF.

    Args:
        infile (str): The input PDF file name.
        attachment_name (str): The name of the attachment to remove from the PDF.
        outfile (str): The output PDF file name with the attachment removed.

    Returns:
        None

    Example:
        >>> remove_attachment("with_attachments.pdf", "file_example.txt", "removed_one.pdf")

    Note:
        This function removes the attachment specified by ``attachment_name`` if it exists in the document.
    """

    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete_by_key(attachment_name)
        document.save(outfile)


def remove_all_attachments(infile, outfile):
    """
    Remove all attachments from the specified PDF and save the result.

    Args:
        infile (str): The input PDF file name
        outfile (str): The output PDF file name with all attachments removed

    Returns:
        None

    Example:
        >>> remove_all_attachments("with_attachments.pdf", "clean.pdf")

    Note:
        This clears all embedded files from the PDF document.
    """
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete()
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
            "remove_attachment",
            remove_attachment,
            path.join(input_dir, "sample_attachment.pdf"),
            "file_example.txt",
            path.join(output_dir, "removed_attachment.pdf"),
        ),
        (
            "remove_all_attachments",
            remove_all_attachments,
            path.join(input_dir, "sample_attachment.pdf"),
            path.join(output_dir, "removed_all_attachments.pdf"),
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
