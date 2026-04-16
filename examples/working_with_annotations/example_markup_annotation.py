import sys
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
from os import path


sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def add_caret_annotations():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Open PDF document
    document = ap.Document(data_dir + "sample.pdf")
    page = document.pages[1]

    # Create Caret Annotation for text insertion
    caret_annotation1 = ap.annotations.CaretAnnotation(
        page,
        ap.Rectangle(299.988, 713.664, 308.708, 720.769)
    )
    caret_annotation1.title = "Aspose User"
    caret_annotation1.subject = "Inserted text 1"
    caret_annotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation1.color = ap.Color.blue

    # Create Caret Annotation for text replacement
    caret_annotation2 = ap.annotations.CaretAnnotation(
        page,
        ap.Rectangle(361.246, 727.908, 370.081, 735.107)
    )
    caret_annotation2.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation2.subject = "Inserted text 2"
    caret_annotation2.title = "Aspose User"
    caret_annotation2.color = ap.Color.blue

    # Create StrikeOut Annotation
    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        page,
        ap.Rectangle(318.407, 727.826, 368.916, 740.098)
    )
    strikeout_annotation.color = ap.Color.blue
    strikeout_annotation.quad_points = [
        ap.Point(321.66, 739.416),
        ap.Point(365.664, 739.416),
        ap.Point(321.66, 728.508),
        ap.Point(365.664, 728.508)
    ]
    strikeout_annotation.subject = "Cross-out"
    strikeout_annotation.in_reply_to = caret_annotation2
    strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP

    # Add annotations to the page
    page.annotations.append(caret_annotation1)
    page.annotations.append(caret_annotation2)
    page.annotations.append(strikeout_annotation)

    # Save PDF document
    document.save(data_dir + "AddCaretAnnotations_out.pdf")


def get_caret_annotations():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Open PDF document
    document = ap.Document(data_dir + "sample_caret.pdf")

    page = document.pages[1]

    # Iterate through annotations and filter Caret annotations
    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.CARET:
            # Print annotation rectangle
            print(annot.rect)
  

def delete_caret_annotation():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Open PDF document
    document = ap.Document(data_dir + "sample_caret.pdf")
    page = document.pages[1]

    # Collect caret annotations first (avoid modifying collection while iterating)
    caret_annotations = [
        annot for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.CARET
    ]

    # Delete each Caret annotation
    for annot in caret_annotations:
        page.annotations.delete(annot)

    # Save PDF document after deleting annotations
    document.save(data_dir + "DeleteCaretAnnotation_out.pdf")


def add_replace_annotations(infile, outfile):
    """
    Add replace annotations to a PDF document to mark text that should be replaced.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> add_replace_annotations("sample.pdf", "output.pdf")

    Note:
        Replace annotations are used to indicate text that should be replaced.
    """
    # Open PDF document
    document = ap.Document(infile)
    page = document.pages[1]

    # Create first Replace Annotation
    replace_annotation1 = ap.annotations.ReplaceAnnotation(
        page,
        ap.Rectangle(299.988, 713.664, 308.708, 720.769)
    )
    replace_annotation1.title = "Aspose User"
    replace_annotation1.subject = "Text to replace"
    replace_annotation1.flags = ap.annotations.AnnotationFlags.PRINT
    replace_annotation1.color = ap.Color.red

    # Create second Replace Annotation
    replace_annotation2 = ap.annotations.ReplaceAnnotation(
        page,
        ap.Rectangle(361.246, 727.908, 370.081, 735.107)
    )
    replace_annotation2.title = "Aspose User"
    replace_annotation2.subject = "Another text to replace"
    replace_annotation2.flags = ap.annotations.AnnotationFlags.PRINT
    replace_annotation2.color = ap.Color.red

    # Add annotations to the page
    page.annotations.append(replace_annotation1)
    page.annotations.append(replace_annotation2)

    # Save PDF document
    document.save(outfile)


def get_replace_annotations(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all replace annotations on a page.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): Not used.

    Returns:
        None

    Example:
        >>> get_replace_annotations("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all replace annotations found on the first page.
    """
    # Open PDF document
    document = ap.Document(infile)
    page = document.pages[1]

    # Iterate through annotations and filter Replace annotations
    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.REPLACE:
            # Print annotation rectangle
            print(f"Replace annotation rect: {annot.rect}")


def delete_replace_annotation(infile, outfile):
    """
    Delete all replace annotations from a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> delete_replace_annotation("sample.pdf", "output.pdf")

    Note:
        This function removes all replace annotations from the first page and saves the modified PDF.
    """
    # Open PDF document
    document = ap.Document(infile)
    page = document.pages[1]

    # Collect replace annotations first (avoid modifying collection while iterating)
    replace_annotations = [
        annot for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.REPLACE
    ]

    # Delete each Replace annotation
    for annot in replace_annotations:
        page.annotations.delete(annot)

    # Save PDF document after deleting annotations
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run adding markup annotations examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("caret_annotations_add", add_caret_annotations),
        ("caret_annotations_get", get_caret_annotations),
        ("caret_annotations_delete", delete_caret_annotation),
        ("replace_annotations_add", add_replace_annotations),
        ("replace_annotations_get", get_replace_annotations),
        ("replace_annotations_delete", delete_replace_annotation),
    ]

    for name, func in examples:
        input_file_name = path.join(input_dir, "Annotations.pdf")
        output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
        try:
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
