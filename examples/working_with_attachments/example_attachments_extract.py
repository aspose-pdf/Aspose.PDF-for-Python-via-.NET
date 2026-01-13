from os import path
from io import FileIO
import aspose.pdf as ap
import sys
from aspose.pycore import cast, is_assignable

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def extract_single_attachment(infile, attachment_name, outfile):
    """
    Extract a specific embedded file (attachment) from a PDF document by name.

    This function searches for an attachment with the specified name in the PDF document
    and saves it to the output file path if found.

    Args:
        infile (str): Path to the input PDF file containing attachments.
        attachment_name (str): Name of the specific attachment to extract.
        outfile (str): Path where the extracted attachment will be saved.

    Returns:
        None

    Example:
        >>> extract_single_attachment("document_with_attachments.pdf", "report.txt", "./output/report.txt")
        Extracting attachment: report.txt
        Attachment extracted successfully

    Raises:
        ValueError: If the specified attachment is not found in the PDF.

    Note:
        - The attachment name must match exactly (case-sensitive).
        - The function will overwrite the output file if it already exists.
    """

    with ap.Document(infile) as document:
        print(f"Extracting attachment: {attachment_name}")

        attachment_found = False
        for file_spec in document.embedded_files:
            if file_spec.name == attachment_name:
                with open(outfile, "wb") as f:
                    f.write(file_spec.contents.read())
                print("Attachment extracted successfully")
                attachment_found = True
                break

        if not attachment_found:
            raise ValueError(f"Attachment '{attachment_name}' not found in PDF")


def _print_file_params(params):
    """Helper to print file specification parameters."""
    if params:
        print(f"CheckSum: {params.check_sum}")
        print(f"Creation Date: {params.creation_date}")
        print(f"Modification Date: {params.mod_date}")
        print(f"Size: {params.size}")


def extract_attachments(infile, output_dir):
    """
    Extract all embedded files (attachments) from a PDF document.
    This function iterates through all embedded files in the PDF document, prints their
    metadata (name, description, MIME type, and parameters), and saves each attachment
    to the specified output directory.
    Args:
        infile (str): Path to the input PDF file containing attachments.
        output_dir (str): Directory path where extracted attachments will be saved.
    Returns:
        None
    Example:
        >>> extract_attachments("document_with_attachments.pdf", "./output")
        Total files: 2
        Name: attachment1.txt
        Description: Sample text file
        Mime Type: text/plain
        ...
    Note:
        - The function will overwrite existing files with the same name in the output directory.
        - Requires the aspose.pdf module (imported as ap) to be available.
        - Uses the helper function _print_file_params to display file parameters.
    """

    with ap.Document(infile) as document:
        print(f"Total files: {len(document.embedded_files)}")

        for file_spec in document.embedded_files:
            print(f"Name: {file_spec.name}")
            print(f"Description: {file_spec.description}")
            print(f"Mime Type: {file_spec.mime_type}")
            _print_file_params(file_spec.params)

            output_path = path.join(output_dir, file_spec.name)
            with open(output_path, "wb") as f:
                f.write(file_spec.contents.read())


def extract_file_attachment_annotation(infile, output_dir):
    """
    Extract an embedded file from a FileAttachment annotation in a PDF document.
    This function locates the first FileAttachment annotation on the first page of a PDF,
    retrieves its embedded file, and saves it to the specified output directory.
    Args:
        infile (str): Path to the input PDF file containing file attachment annotations.
        output_dir (str): Directory path where the extracted file will be saved.
    Returns:
        None
    Raises:
        StopIteration: If no FileAttachment annotation is found on the first page.
        IOError: If there are issues reading the PDF or writing the extracted file.
    Example:
        >>> extract_file_attachment_annotation("document.pdf", "./output")
        File name: attachment.txt
        Extracted to: ./output/extracted-attachment.txt
    Note:
        - Only the first FileAttachment annotation on the first page is processed.
        - The extracted file is prefixed with "extracted-" in the output directory.
        - The embedded file contents are read entirely into memory before writing.
    """
    # Open PDF document
    document = ap.Document(infile)

    # Get first page
    page = document.pages[1]

    # Find first FileAttachment annotation
    file_attachment = next(
        annot
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.FILE_ATTACHMENT
    )

    # Cast to FileAttachmentAnnotation
    faa = cast(ap.annotations.FileAttachmentAnnotation, file_attachment)

    # Access embedded file
    file_spec = faa.file
    print(f"File name: {file_spec.name}")

    # Save embedded file to disk
    output_path = path.join(output_dir, f"extracted-{file_spec.name}")
    with open(output_path, "wb") as f:
        f.write(file_spec.contents.read())

    print(f"Extracted to: {output_path}")


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
            "Extract single attachment",
            extract_single_attachment,
            path.join(input_dir, "sample_attachment.pdf"),
            "rfc822.txt",
            path.join(output_dir, "extracted_attachment.txt"),
        ),
        (
            "Extract all attachments",
            extract_attachments,
            path.join(input_dir, "sample_attachment.pdf"),
            output_dir,
        ),
        (
            "Extract file attachment annotation",
            extract_file_attachment_annotation,
            path.join(input_dir, "sample_with_attachment.pdf"),
            output_dir,
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
