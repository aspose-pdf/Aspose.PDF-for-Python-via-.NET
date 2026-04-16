import sys
from os import path

import aspose.pdf as ap
from aspose.pycore import cast, is_assignable

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def mark_text_redaction(infile, outfile, search_term):
    """Mark matching text fragments with redaction annotations."""
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

    text_search_options = ap.text.TextSearchOptions(True)
    text_fragment_absorber.text_search_options = text_search_options
    document.pages.accept(text_fragment_absorber)

    for text_fragment in text_fragment_absorber.text_fragments:
        page = text_fragment.page
        annotation_rectangle = text_fragment.rectangle
        redaction_annotation = ap.annotations.RedactionAnnotation(page, annotation_rectangle)
        redaction_annotation.fill_color = ap.Color.gray
        redaction_annotation.border_color = ap.Color.red
        redaction_annotation.color = ap.Color.white
        redaction_annotation.overlay_text = "REDACTED"
        redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
        redaction_annotation.repeat = True
        page.annotations.add(redaction_annotation, True)

    document.save(outfile)


def apply_redaction(infile, outfile):
    """Apply redaction annotations on page 1 permanently."""
    document = ap.Document(infile)
    redaction_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
    ]

    for redaction_annotation in redaction_annotations:
        if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
            cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()

    document.save(outfile)


def redact_area(infile, outfile):
    """Redact the third detected image placement on page 1."""
    document = ap.Document(infile)

    image_placement_absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(image_placement_absorber)

    target_rect = image_placement_absorber.image_placements[2].rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True

    page.annotations.add(redaction_annotation, True)
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run security annotation examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "mark_text_redaction",
            mark_text_redaction,
            ("sample.pdf", "sample_redaction.pdf", "PDF"),
        ),
        (
            "apply_redaction",
            apply_redaction,
            ("sample_redaction.pdf", "sample_redacted.pdf"),
        ),
        (
            "redact_area",
            redact_area,
            ("sample_redact_area.pdf", "sample_redact_area.pdf"),
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
