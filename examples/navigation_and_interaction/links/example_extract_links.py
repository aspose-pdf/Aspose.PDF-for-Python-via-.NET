import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

sys.path.append(path.join(path.dirname(__file__), '../..'))

from config import set_license, initialize_data_dir


def extract_link_annotation(infile):
    """
    Extract link annotations from PDF.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_link_annotation("sample_goto_action.pdf")

    Note:
        Prints page index and rectangle location for each link annotation on first page.
    """
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")


def extract_hyperlinks(infile):
    """
    Extract hyperlinks (URI actions) from PDF.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_hyperlinks("sample.pdf")

    Note:
        Prints page index and URI for each GoToURIAction link on first page.
        Moved from: Get PDF Hyperlink Destination (https://docs.aspose.com/pdf/python-net/actions/#get-pdf-hyperlink-destination-url)
    """

    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"Page {annotation.page_index}, URI:{action.uri}")


def run_all_examples(data_dir=None, license_path=None):
    """Run extract links examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Extract link annotations", extract_link_annotation, "sample_goto_action.pdf"),
        (
            "Extract hyperlinks",
            extract_hyperlinks,
            "sample.pdf",
        ),
    ]

    for name, func, input_file in examples:
        try:
            input_file_name = path.join(input_dir, input_file)
            func(input_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
