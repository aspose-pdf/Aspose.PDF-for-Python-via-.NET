import sys
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
from os import path


sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def mark_text_redaction(infile, outfile, searchTerm):
    """
    Mark text for redaction with redaction annotations.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename
        searchTerm (str): Text to search and mark for redaction

    Returns:
        None

    Example:
        mark_text_redaction("sample.pdf", "sample_redaction.pdf", "Markers")

    Note:
        Creates RedactionAnnotation with gray fill, red border, white text.
        Overlay text shows "REDACTED" centered and repeated.
    """
    document = ap.Document(infile)
    textFragmentAbsorber = ap.text.TextFragmentAbsorber(searchTerm)

    textSearchOptions = ap.text.TextSearchOptions(True)
    textFragmentAbsorber.text_search_options = textSearchOptions
    document.pages.accept(textFragmentAbsorber)

    textFragmentCollection = textFragmentAbsorber.text_fragments

    for textFragment in textFragmentCollection:
        page = textFragment.page
        annotationRectangle = textFragment.rectangle
        annot = ap.annotations.RedactionAnnotation(page, annotationRectangle)
        annot.fill_color = ap.Color.gray
        annot.border_color = ap.Color.red
        annot.color = ap.Color.white
        annot.overlay_text = "REDACTED"
        annot.text_alignment = ap.HorizontalAlignment.CENTER
        annot.repeat = True
        textFragment.page.annotations.add(annot, True)
    document.save(outfile)

def apply_redaction(infile, outfile):
    """
    Apply redaction annotations to permanently remove content.

    Args:
        infile (str): Input PDF filename with redaction annotations
        outfile (str): Output PDF filename with redactions applied

    Returns:
        None

    Example:
        apply_redaction("sample_redaction.pdf", "sample_redacted.pdf")

    Note:
        Finds all RedactionAnnotation on first page and applies them permanently.
    """
    document = ap.Document(infile)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for ra in redactionAnnotations:
        if is_assignable(ra, ap.annotations.RedactionAnnotation):
            annotation = cast(ap.annotations.RedactionAnnotation, ra)
            annotation.redact()

    document.save(outfile)


def redact_area(infile, outfile):
    """
    Redacts a specific area in a PDF document by applying a redaction annotation.

    This function identifies an image placement in the first page of a PDF document,
    extracts its rectangular bounds, and applies a redaction annotation over that area.
    The redacted area is filled with a gray color and displays "REDACTED" text overlay.

    Args:
        infile (str): Path to the input PDF file to be redacted.
        outfile (str): Path where the redacted PDF file will be saved.

    Returns:
        None

    Example:
        >>> redact_area("input.pdf", "output_redacted.pdf")

    Note:
        - The function targets the third image placement (index 2) on the first page
        - The redaction annotation includes a white text overlay with "REDACTED"
        - The annotation has a red border and gray fill color
        - The overlay text is repeated to fill the redacted area
    """
    document = ap.Document(infile)
    imagePlacementAbsorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(imagePlacementAbsorber)
    redact_area = imagePlacementAbsorber.image_placements[2].rectangle
    annot = ap.annotations.RedactionAnnotation(page, redact_area)
    annot.fill_color = ap.Color.gray
    annot.border_color = ap.Color.red
    annot.color = ap.Color.white
    annot.overlay_text = "REDACTED"
    annot.text_alignment = ap.HorizontalAlignment.CENTER
    annot.repeat = True
    page.annotations.add(annot, True)
    document.save(outfile)

def run_all_examples(data_dir=None, license_path=None):
    """Run adding extra annotations examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Mark text redaction", mark_text_redaction, ("sample.pdf", "sample_redaction.pdf", "PDF")),
        ("Apply redaction", apply_redaction, ("sample_redaction.pdf", "sample_redacted.pdf")),
        ("Redact area", redact_area, ("sample.pdf", "sample_redact_area.pdf")),

    ]

    for name, func, args in examples:
        input_file_name = path.join(input_dir, args[0])
        output_file_name = path.join(output_dir, args[1])
        try:
            if (len(args)>2):
                func(input_file_name, output_file_name, args[2])
            else:
                func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
