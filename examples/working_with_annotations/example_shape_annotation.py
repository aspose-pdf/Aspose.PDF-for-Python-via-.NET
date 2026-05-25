import sys
from os import path

import aspose.pdf as ap
from aspose.pycore import cast

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def square_annotation_add(infile, outfile):
    """Add a square annotation to page 1."""
    document = ap.Document(infile)

    square_annotation = ap.annotations.SquareAnnotation(
        document.pages[1],
        ap.Rectangle(60, 600, 250, 450, True),
    )
    square_annotation.title = "John Smith"
    square_annotation.color = ap.Color.blue
    square_annotation.interior_color = ap.Color.blue_violet
    square_annotation.opacity = 0.25

    document.pages[1].annotations.append(square_annotation)
    document.save(outfile)


def circle_annotation_add(infile, outfile):
    """Add a circle annotation to page 1."""
    document = ap.Document(infile)

    circle_annotation = ap.annotations.CircleAnnotation(
        document.pages[1],
        ap.Rectangle(270, 160, 483, 383, True),
    )
    circle_annotation.title = "John Smith"
    circle_annotation.color = ap.Color.red
    circle_annotation.interior_color = ap.Color.misty_rose
    circle_annotation.opacity = 0.5
    circle_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 316, 1021, 459, True),
    )

    document.pages[1].annotations.append(circle_annotation)
    document.save(outfile)


def polygon_annotation_add(infile, outfile):
    """Add a polygon annotation to page 1."""
    document = ap.Document(infile)

    polygon_annotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygon_annotation.title = "John Smith"
    polygon_annotation.color = ap.Color.blue
    polygon_annotation.interior_color = ap.Color.blue_violet
    polygon_annotation.opacity = 0.25

    document.pages[1].annotations.append(polygon_annotation)
    document.save(outfile)


def polyline_annotation_add(infile, outfile):
    """Add a polyline annotation to page 1."""
    document = ap.Document(infile)

    polyline_annotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polyline_annotation.title = "John Smith"
    polyline_annotation.color = ap.Color.red
    polyline_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 196, 1021, 338, True),
    )

    document.pages[1].annotations.append(polyline_annotation)
    document.save(outfile)


def square_annotation_get(infile, outfile):
    """Print square annotation rectangles on page 1."""
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        print(annotation.rect)


def circle_annotation_get(infile, outfile):
    """Print circle annotation rectangles on page 1."""
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        print(annotation.rect)


def polygon_annotation_get(infile, outfile):
    """Print polygon annotation rectangles on page 1."""
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        print(annotation.rect)


def polyline_annotation_get(infile, outfile):
    """Print polyline annotation rectangles on page 1."""
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        print(annotation.rect)


def square_annotation_delete(infile, outfile):
    """Delete square annotations from page 1."""
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)


def circle_annotation_delete(infile, outfile):
    """Delete circle annotations from page 1."""
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)


def polygon_annotation_delete(infile, outfile):
    """Delete polygon annotations from page 1."""
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)


def polyline_annotation_delete(infile, outfile):
    """Delete polyline annotations from page 1."""
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)


def line_annotation_add(infile, outfile):
    """Add a line annotation to page 1."""
    document = ap.Document(infile)

    line_annotation = ap.annotations.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439, True),
        ap.Point(556, 99),
        ap.Point(556, 443),
    )

    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
    line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266, True),
    )
    line_annotation.popup = popup

    document.pages[1].annotations.append(line_annotation)
    document.save(outfile)


def line_annotations_get(infile, outfile):
    """Print start/end points for line annotations on page 1."""
    document = ap.Document(infile)

    line_annotation = [
        cast(ap.annotations.LineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotation:
        print(
            f"[{annotation.starting.x},{annotation.starting.y}]"
            f"-[{annotation.ending.x},{annotation.ending.y}]"
        )


def line_annotations_delete(infile, outfile):
    """Delete line annotations from page 1."""
    document = ap.Document(infile)
    page = document.pages[1]

    line_annotations = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotations:
        page.annotations.delete(annotation)

    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run shape annotation examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("line_annotation_add", line_annotation_add),
        ("line_annotations_get", line_annotations_get),
        ("line_annotations_delete", line_annotations_delete),
        ("polygon_annotation_add", polygon_annotation_add),
        ("polygon_annotation_get", polygon_annotation_get),
        ("polygon_annotation_delete", polygon_annotation_delete),
        ("polyline_annotation_add", polyline_annotation_add),
        ("polyline_annotation_get", polyline_annotation_get),
        ("polyline_annotation_delete", polyline_annotation_delete),
        ("circle_annotation_add", circle_annotation_add),
        ("circle_annotation_get", circle_annotation_get),
        ("circle_annotation_delete", circle_annotation_delete),
        ("square_annotation_add", square_annotation_add),
        ("square_annotation_get", square_annotation_get),
        ("square_annotation_delete", square_annotation_delete),
    ]

    for name, func in examples:
        input_file_name = path.join(input_dir, "Annotations.pdf")
        output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
        try:
            if "add" in func.__name__:
                input_file_name = path.join(input_dir, "sample.pdf")
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
