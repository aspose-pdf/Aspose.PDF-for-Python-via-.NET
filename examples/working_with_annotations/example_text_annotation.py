import sys
from os import path

import aspose.pdf as ap
from aspose.pycore import cast

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def free_text_annotation_add(infile, outfile):
    """Add a free-text annotation to page 1."""
    document = ap.Document(infile)

    free_text_annotation = ap.annotations.FreeTextAnnotation(
        document.pages[1],
        ap.Rectangle(299, 713, 308, 720, True),
        ap.annotations.DefaultAppearance(),
    )
    free_text_annotation.title = "Aspose User"
    free_text_annotation.color = ap.Color.light_green

    document.pages[1].annotations.append(free_text_annotation)
    document.save(outfile)


def free_text_annotation_get(infile, outfile):
    """Print free-text annotation rectangles on page 1."""
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        print(annotation.rect)


def free_text_annotation_delete(infile, outfile):
    """Delete free-text annotations from page 1."""
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)


def text_highlight_annotation_add(infile, outfile):
    """Add a highlight annotation to page 1."""
    document = ap.Document(infile)

    highlight_annotation = ap.annotations.HighlightAnnotation(
        document.pages[1],
        ap.Rectangle(300, 750, 320, 770, True),
    )

    document.pages[1].annotations.append(highlight_annotation)
    document.save(outfile)


def text_highlight_annotation_get(infile, outfile):
    """Print highlight annotation rectangles on page 1."""
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        print(annotation.rect)


def text_highlight_annotation_delete(infile, outfile):
    """Delete highlight annotations from page 1."""
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)


def text_strikeout_annotation_add(infile, outfile):
    """Add a strikeout annotation to page 1."""
    document = ap.Document(infile)

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    strikeout_annotation.title = "Aspose User"
    strikeout_annotation.subject = "Inserted text 1"
    strikeout_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeout_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeout_annotation)
    document.save(outfile)


def text_strikeout_annotation_get(infile, outfile):
    """Print strikeout annotation rectangles on page 1."""
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        print(annotation.rect)


def text_strikeout_annotation_delete(infile, outfile):
    """Delete strikeout annotations from page 1."""
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)


def text_squiggly_annotation_add(infile, outfile):
    """Add a squiggly annotation to page 1."""
    document = ap.Document(infile)
    page = document.pages[1]

    squiggly_annotation = ap.annotations.SquigglyAnnotation(
        page,
        ap.Rectangle(67, 317, 261, 459, True),
    )
    squiggly_annotation.title = "John Smith"
    squiggly_annotation.color = ap.Color.blue

    page.annotations.append(squiggly_annotation)
    document.save(outfile)


def text_squiggly_annotation_get(infile, outfile):
    """Print squiggly annotation rectangles on page 1."""
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        print(annotation.rect)


def text_squiggly_annotation_delete(infile, outfile):
    """Delete squiggly annotations from page 1."""
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)


def text_underline_annotation_add(infile, outfile):
    """Add an underline annotation to page 1."""
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline 1"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)


def text_underline_annotation_get(infile, outfile):
    """Print underline annotation rectangles on page 1."""
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        print(annotation.rect)


def text_underline_annotation_delete(infile, outfile):
    """Delete underline annotations from page 1."""
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)


def text_underline_with_quad_points_add(infile, outfile):
    """Add underline annotation with explicit quad points."""
    document = ap.Document(infile)
    rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

    underline_annotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline with Quad Points"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue
    underline_annotation.quad_points = [
        ap.Point(rect.llx, rect.lly),
        ap.Point(rect.urx, rect.lly),
        ap.Point(rect.urx, rect.ury),
        ap.Point(rect.llx, rect.ury),
    ]

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)


def text_underline_marked_text_get(infile, outfile):
    """Print marked text extracted from underline annotations."""
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)        
        print(f"Marked text: {ua.get_marked_text()}")


def text_underline_marked_fragments_get(infile, outfile):
    """Print marked text fragments extracted from underline annotations."""
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        for fragment in ua.get_marked_text_fragments():
            print(f"Fragment text: {fragment.text}")


def text_underline_by_title_delete(infile, outfile):
    """Delete underline annotations with title 'Aspose User'."""
    document = ap.Document(infile)

    underline_annotations = [
        cast(ap.annotations.UnderlineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE        
    ]

    for annotation in underline_annotations:
        if annotation.title.startswith("a"):
            document.pages[1].annotations.delete(annotation)

    document.save(outfile)


def text_underline_flatten_add(infile, outfile):
    """Add and flatten an underline annotation into page content."""
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline to Flatten"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    underline_annotation.flatten()

    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run text annotation examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add Free Text Annotation", free_text_annotation_add),
        ("Get Free Text Annotation", free_text_annotation_get),
        ("Delete Free Text Annotation", free_text_annotation_delete),
        ("Add Text Highlight Annotation", text_highlight_annotation_add),
        ("Get Text Highlight Annotation", text_highlight_annotation_get),
        ("Delete Text Highlight Annotation", text_highlight_annotation_delete),
        ("Add Text Strikeout Annotation", text_strikeout_annotation_add),
        ("Get Text Strikeout Annotation", text_strikeout_annotation_get),
        ("Delete Text Strikeout Annotation", text_strikeout_annotation_delete),
        ("Add Text Squiggly Annotation", text_squiggly_annotation_add),
        ("Get Text Squiggly Annotation", text_squiggly_annotation_get),
        ("Delete Text Squiggly Annotation", text_squiggly_annotation_delete),
        ("Add Text Underline Annotation", text_underline_annotation_add),
        ("Get Text Underline Annotation", text_underline_annotation_get),
        ("Delete Text Underline Annotation", text_underline_annotation_delete),
        ("Add Text Underline Annotation with Quad Points", text_underline_with_quad_points_add),
        ("Add Text Underline Annotation Flatten", text_underline_flatten_add),
        ("Get Text Underline Annotation Marked Text", text_underline_marked_text_get),
        ("Get Text Underline Annotation Marked Fragments", text_underline_marked_fragments_get),
        ("Delete Text Underline Annotation by Title", text_underline_by_title_delete),
    ]

    for name, func in examples:    
        output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
        try:
            input_file_name = path.join(input_dir, "Annotations.pdf")
            if "add" in func.__name__:
                    input_file_name = path.join(input_dir, "sample.pdf")
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
