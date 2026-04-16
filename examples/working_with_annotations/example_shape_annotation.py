from os import path
import aspose.pdf as ap
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir

def square_annotation_add(infile, outfile):
    """
    Add a square annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> square_annotation_add("sample.pdf", "output.pdf")

    Note:
        The square annotation is positioned at coordinates (60, 600, 250, 450) with blue color,
        blue-violet interior color, and 25% opacity.
    """
    document = ap.Document(infile)

    squareAnnotation = ap.annotations.SquareAnnotation(document.pages[1], ap.Rectangle(60, 600, 250, 450, True))
    squareAnnotation.title = "John Smith"
    squareAnnotation.color = ap.Color.blue
    squareAnnotation.interior_color = ap.Color.blue_violet
    squareAnnotation.opacity = 0.25

    document.pages[1].annotations.append(squareAnnotation)

    document.save(outfile)
    

def circle_annotation_add(infile, outfile):
    """
    Add a circle annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> circle_annotation_add("sample.pdf", "output.pdf")

    Note:
        The circle annotation is positioned at coordinates (270, 160, 483, 383) with red color,
        misty rose interior color, and 50% opacity. Includes a popup annotation.
    """
    document = ap.Document(infile)

    circleAnnotation = ap.annotations.CircleAnnotation(
        document.pages[1], ap.Rectangle(270, 160, 483, 383, True)
    )
    circleAnnotation.title = "John Smith"
    circleAnnotation.color = ap.Color.red
    circleAnnotation.interior_color = ap.Color.misty_rose
    circleAnnotation.opacity = 0.5
    circleAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 316, 1021, 459, True)
    )

    document.pages[1].annotations.append(circleAnnotation)
    document.save(outfile)


def polygon_annotation_add(infile, outfile):
    """
    Add a polygon annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> polygon_annotation_add("sample.pdf", "output.pdf")

    Note:
        The polygon annotation is defined by 5 points with blue color,
        blue-violet interior color, and 25% opacity.
    """
    document = ap.Document(infile)

    polygonAnnotation = ap.annotations.PolygonAnnotation(
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
    polygonAnnotation.title = "John Smith"
    polygonAnnotation.color = ap.Color.blue
    polygonAnnotation.interior_color = ap.Color.blue_violet
    polygonAnnotation.opacity = 0.25

    document.pages[1].annotations.append(polygonAnnotation)
    document.save(outfile)
 

def polyline_annotation_add(infile, outfile):
    """
    Add a polyline annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> polyline_annotation_add("sample.pdf", "output.pdf")

    Note:
        The polyline annotation is defined by 5 points with red color.
        Includes a popup annotation.
    """
    document = ap.Document(infile)

    polylineAnnotation = ap.annotations.PolylineAnnotation(
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
    polylineAnnotation.title = "John Smith"
    polylineAnnotation.color = ap.Color.red
    polylineAnnotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1], ap.Rectangle(842, 196, 1021, 338, True)
    )

    document.pages[1].annotations.append(polylineAnnotation)
    document.save(outfile)


def square_annotation_get(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all square annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> square_annotation_get("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all square annotations found on the first page.
    """
    document = ap.Document(infile)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        print(pa.rect)


def circle_annotation_get(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all circle annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> circle_annotation_get("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all circle annotations found on the first page.
    """
    document = ap.Document(infile)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        print(ca.rect)


def polygon_annotation_get(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all polygon annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> polygon_annotation_get("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all polygon annotations found on the first page.
    """
    document = ap.Document(infile)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        print(pa.rect)
 

def polyline_annotation_get(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all polyline annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> polyline_annotation_get("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all polyline annotations found on the first page.
    """
    document = ap.Document(infile)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        print(pa.rect)


def square_annotation_delete(infile, outfile):
    """
    Delete all square annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> square_annotation_delete("sample.pdf", "output.pdf")

    Note:
        This function removes all square annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    squareAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUARE)
    ]

    for pa in squareAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(outfile)


def circle_annotation_delete(infile, outfile):
    """
    Delete all circle annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> circle_annotation_delete("sample.pdf", "output.pdf")

    Note:
        This function removes all circle annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    circleAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CIRCLE)
    ]

    for ca in circleAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(outfile)


def polygon_annotation_delete(infile, outfile):
    """
    Delete all polygon annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> polygon_annotation_delete("sample.pdf", "output.pdf")

    Note:
        This function removes all polygon annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    polygonAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLYGON)
    ]

    for pa in polygonAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(outfile)
 

def polyline_annotation_delete(infile, outfile):
    """
    Delete all polyline annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> polyline_annotation_delete("sample.pdf", "output.pdf")

    Note:
        This function removes all polyline annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    polylineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.POLY_LINE)
    ]

    for pa in polylineAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(outfile)   


def add_line_annotation():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Open PDF document
    document = ap.Document(data_dir + "Appartments.pdf")

    # Create Line Annotation
    line_annotation = ap.annotations.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439),
        ap.Point(556, 99),
        ap.Point(556, 443)
    )

    # Set annotation properties
    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ap.annotations.LineEnding.open_arrow
    line_annotation.ending_style = ap.annotations.LineEnding.open_arrow

    # Create and assign popup annotation
    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266)
    )
    line_annotation.popup = popup

    # Add annotation to the page
    document.pages[1].annotations.append(line_annotation)

    # Save PDF document
    document.save(data_dir + "AddLineAnnotation_out.pdf")   

    import aspose.pdf as ap


def read_line_annotations():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Open PDF document
    document = ap.Document(data_dir + "Appartments_mod.pdf")

    # Iterate through annotations on the first page
    for annotation in document.pages[1].annotations:
        # Filter only Line annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE:
            # Cast to LineAnnotation (Python doesn't require explicit casting,
            # but we can treat it as such)
            line_annotation = annotation

            # Print coordinates
            print(f"[{line_annotation.starting.x},{line_annotation.starting.y}]"
                  f"-[{line_annotation.ending.x},{line_annotation.ending.y}]")


def delete_line_annotations():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Open PDF document
    document = ap.Document(data_dir + "Appartments_mod.pdf")

    page = document.pages[1]

    # Collect line annotations first (avoid modifying collection while iterating)
    line_annotations = [
        annot for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    # Delete each line annotation
    for annot in line_annotations:
        page.annotations.delete(annot)

    # Save PDF document
    document.save(data_dir + "DeleteLineAnnotations_out.pdf")


if __name__ == "__main__":
    delete_line_annotations()


def run_all_examples(data_dir=None, license_path=None):
    """Run adding figures annotations examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("polygon_annotation_add", polygon_annotation_add),
        ("polyline_annotation_add", polyline_annotation_add),
        ("circle_annotation_add", circle_annotation_add),
        ("square_annotation_add", square_annotation_add),
        ("polygon_annotation_get", polygon_annotation_get),
        ("polyline_annotation_get", polyline_annotation_get),
        ("circle_annotation_get", circle_annotation_get),
        ("square_annotation_get", square_annotation_get),
        ("polygon_annotation_delete", polygon_annotation_delete),
        ("polyline_annotation_delete", polyline_annotation_delete),
        ("circle_annotation_delete", circle_annotation_delete),
        ("square_annotation_delete", square_annotation_delete),
        ("add_line_annotation", add_line_annotation),
        ("read_line_annotations", read_line_annotations),
        ("delete_line_annotations", delete_line_annotations),
    ]

    for name, func in examples:
        input_file_name = path.join(input_dir, "Annotations.pdf")
        output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
        try:
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

if __name__ == "__main__":
    run_all_examples()