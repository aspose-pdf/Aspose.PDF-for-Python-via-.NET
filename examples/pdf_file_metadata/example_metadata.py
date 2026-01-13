import aspose.pdf as ap
import datetime
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def get_pdf_file_information(infile):
    """
    Get and display PDF document information (metadata).

    Args:
        infile (str): The input PDF file name

    Returns:
        None

    Example:
        >>> get_pdf_file_information("sample.pdf")

    Note:
        Prints author, creation date, keywords, modification date, subject, and title.
    """
    # Open PDF document
    document = ap.Document(infile)

    # Get document information
    doc_info = document.info

    # Display document information
    print(f"Author: {doc_info.author}")
    print(f"Creation Date: {doc_info.creation_date}")
    print(f"Keywords: {doc_info.keywords}")
    print(f"Modify Date: {doc_info.mod_date}")
    print(f"Subject: {doc_info.subject}")
    print(f"Title: {doc_info.title}")


def set_prefix_metadata(infile, outfile):
    """
    Set metadata property using a registered namespace prefix.

    Args:
        infile (str): The input PDF file name
        outfile (str): The output PDF file name

    Returns:
        None

    Example:
        >>> set_prefix_metadata("input.pdf", "output.pdf")

    Note:
        Registers 'xmp' namespace URI and sets ModifyDate.
    """
    # Open PDF document
    document = ap.Document(infile)

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata.add("xmp:ModifyDate", datetime.datetime.now().isoformat())  # ISO 8601 format

    # Save the updated PDF document
    document.save(outfile)


def set_file_information(infile, outfile):
    """
    Set comprehensive PDF document information (metadata).

    Args:
        infile (str): The input PDF file name
        outfile (str): The output PDF file name

    Returns:
        None

    Example:
        >>> set_file_information("input.pdf", "output.pdf")

    Note:
        Sets author, creation date, keywords, modification date, subject,
        title, producer, and creator fields.
    """
    # Open PDF document
    document = ap.Document(infile)

    # Specify document information
    doc_info = ap.DocumentInfo(document)
    doc_info.author = "Aspose"
    doc_info.creation_date = datetime.datetime.now()
    doc_info.keywords = "Aspose.Pdf, DOM, API"
    doc_info.mod_date = datetime.datetime.now()
    doc_info.subject = "PDF Information"
    doc_info.title = "Setting PDF Document Information"
    doc_info.producer = "Custom producer"
    doc_info.creator = "Custom creator"

    # Save PDF document
    document.save(outfile)


def set_xmp_metadata(infile, outfile):
    """
    Set XMP metadata properties in a PDF document.

    Args:
        infile (str): The input PDF file name
        outfile (str): The output PDF file name

    Returns:
        None

    Example:
        >>> set_xmp_metadata("input.pdf", "output.pdf")

    Note:
        Sets CreateDate, Nickname, and CustomProperty XMP fields.
    """
    # Open PDF document
    document = ap.Document(infile)

    # Set XMP metadata properties
    document.metadata.add("xmp:CreateDate",datetime.datetime.now().isoformat())
    document.metadata.add("xmp:Nickname", "Nickname")
    document.metadata.add("xmp:CustomProperty", "Custom Value")

    # Save the updated PDF document
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run metadata examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("get_pdf_file_information", get_pdf_file_information),
        ("set_prefix_metadata", set_prefix_metadata),
        ("set_file_information", set_file_information),
        ("set_xmp_metadata", set_xmp_metadata),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "sample.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}.pdf")
            if func.__name__ == "get_pdf_file_information":
                func(input_file_name)
            else:
                func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()
