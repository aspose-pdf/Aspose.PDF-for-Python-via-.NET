import aspose.pdf as ap
from os import path
from aspose.pycore import cast, is_assignable
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def extract_highlighted_text(infile):
    """
    Extract text from highlight annotations.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_highlight_text("sample.pdf")

    Note:
        Prints marked text from each highlight annotation on first page.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    for annotation in page.annotations:
        if is_assignable(annotation, ap.annotations.HighlightAnnotation):
            highlight_annotation = cast(ap.annotations.HighlightAnnotation, annotation)
            print(highlight_annotation.get_marked_text())


def extract_stamp_text(infile):
    """
    Extract text from stamp annotations.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_stamp_text("sample-doc.pdf")

    Note:
        Extracts text from stamp appearance using TextAbsorber.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    for annotation in page.annotations:
        if annotation.annotation_type == ap.annotations.AnnotationType.STAMP:
            absorber = ap.text.TextAbsorber()
            xforms = []
            if annotation.appearance.try_get_value("N", xforms):
                absorber.visit(xforms[0])
                print(absorber.text)


def extract_super_sub_text(infile, outfile, page_number=1):
    """
    Extract text (including superscript/subscript) from a specified page of a PDF and write to a text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based index of the page to extract.
    """
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber()
    # Accept only the specific page for extraction
    document.pages[page_number].accept(absorber)
    extracted_text = absorber.text
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(extracted_text)


def extract_super_sub_details(infile, outfile, page_number=1):
    """
    Extract details of each text fragment on a page, identifying superscript and subscript items.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based page index.
    """
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber()
    document.pages[page_number].accept(absorber)
    with open(outfile, "w", encoding="utf-8") as f:
        for fragment in absorber.text_fragments:
            text = fragment.text
            is_sup = fragment.text_state.superscript  # True if superscript
            is_sub = fragment.text_state.subscript  # True if subscript
            f.write(f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n")


def run_all_examples(data_dir=None, license_path=None):
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Extract Highlighted Text", extract_highlighted_text, "sample.pdf", None),
        ("Extract Stamp Text", extract_stamp_text, "sample-stamp.pdf", None),
        (
            "Extract Super/Sub Text",
            extract_super_sub_text,
            "sample-scripts.pdf",
            "superscript_subscript.txt",
        ),
        (
            "Extract Super/Sub Details",
            extract_super_sub_details,
            "sample-scripts.pdf",
            "superscript_subscript_details.txt",
        ),
    ]

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
