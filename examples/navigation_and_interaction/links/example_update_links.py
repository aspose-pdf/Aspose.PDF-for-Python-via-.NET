import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

sys.path.append(path.join(path.dirname(__file__), '../..'))

from config import set_license, initialize_data_dir


def link_annotation_update_text_color(infile, outfile):
    """
    Update text color of link annotations.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        link_annotation_update_text_color("sample.pdf", "sample_text_color.pdf")

    Note:
        Changes text color to red for all link annotations on first page.
        Expands search rectangle by 2 points in all directions.
    """

    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        ta = ap.text.TextFragmentAbsorber()
        rect = la.rect
        rect.llx -= 2
        rect.lly -= 2
        rect.urx += 2
        rect.ury += 2
        ta.text_search_options = ap.text.TextSearchOptions(rect)
        ta.visit(document.pages[1])
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    document.save(outfile)


def link_annotation_update_border(infile, outfile):
    """
    Update border color of link annotations.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        link_annotation_update_border("sample.pdf", "sample_border.pdf")

    Note:
        Changes link annotation color to red for all links on first page.
    """
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red

    document.save(outfile)


def link_annotation_update_web_destination(infile, outfile):
    """
    Update web destination of URI link annotations.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        link_annotation_update_web_destination("sample.pdf", "sample_web_dest.pdf")

    Note:
        Changes all GoToURIAction links to point to https://www.google.com
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
                action.uri = "https://www.google.com"
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run update links examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Update text color", link_annotation_update_text_color),
        ("Update border", link_annotation_update_border),
        ("Update web destination", link_annotation_update_web_destination),
    ]

    input_file_name = path.join(input_dir, "sample.pdf")
    for name, func in examples:
        try:
            output_file_name = path.join(output_dir, f"{func.__name__}.pdf")
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
