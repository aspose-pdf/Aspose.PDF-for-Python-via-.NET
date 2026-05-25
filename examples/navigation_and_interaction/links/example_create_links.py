import aspose.pdf as ap
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), "../.."))

from config import set_license, initialize_data_dir


def create_link_annotation_launch_action(infile, outfile):
    """
    Create link annotation with launch action.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        create_link_annotation_launch_action("sample.pdf", "sample_launch_action.pdf")

    Note:
        Creates green link with dashed border at position (10, 580, 120, 600).
        Launch actions may be disabled by admin for security.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")
    page.annotations.append(link)
    document.save(outfile)


def create_link_annotation_go_to_remote_action(infile, outfile):
    """
    Create link annotation with go-to-remote action.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        create_link_annotation_go_to_remote_action("sample.pdf", "sample_remote_action.pdf")

    Note:
        Creates green link that jumps to page 1 of sample.pdf.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)
    page.annotations.append(link)
    document.save(outfile)


def create_link_annotation_go_to_action(infile, outfile):
    """
    Create link annotation with go-to action.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        create_link_annotation_go_to_action("sample.pdf", "sample_goto_action.pdf")

    Note:
        Creates green link with dashed border that jumps to page 4 (or last page if fewer than 4).
    """
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    if document.pages.length >= 4:
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        link.action = ap.annotations.GoToAction(document.pages[document.pages.length])
    page.annotations.append(link)
    document.save(outfile)


def create_link_annotation_go_to_URI_action(infile, outfile):
    """
    Create link annotation with URI action.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        create_link_annotation_go_to_URI_action("sample.pdf", "sample_URI_action.pdf")

    Note:
        Creates green link that opens https://docs.aspose.com/pdf/python in browser.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")
    page.annotations.append(link)
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run create links examples and report status.
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
            "Launch action",
            create_link_annotation_launch_action,
            "sample.pdf",
            "sample_launch_action.pdf",
        ),
        (
            "Remote action",
            create_link_annotation_go_to_remote_action,
            "sample.pdf",
            "sample_remote_action.pdf",
        ),
        (
            "GoTo action",
            create_link_annotation_go_to_action,
            "sample.pdf",
            "sample_goto_action.pdf",
        ),
        (
            "URI action",
            create_link_annotation_go_to_URI_action,
            "sample.pdf",
            "sample_URI_action.pdf",
        ),
    ]

    for name, func, input_file, output_file in examples:
        try:
            input_file_name = path.join(input_dir, input_file)
            output_file_name = path.join(output_dir, output_file)
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
