import sys
from os import path

import aspose.pdf as ap
from aspose.pycore import cast

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir

def text_annotation_add(infile, outfile):
    """Add a text annotation to page 1."""
    document = ap.Document(infile)

    text_annotation = ap.annotations.TextAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
    )
    text_annotation.title = "Aspose User"
    text_annotation.subject = "Sticky Note"
    text_annotation.contents = "This is a text annotation added by Aspose.PDF for Python via .NET"
    text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    text_annotation.color = ap.Color.blue
    text_annotation.icon = ap.annotations.TextIcon.HELP
    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),        
    )
    popup.open = True

    text_annotation.popup = popup
        

    document.pages[1].annotations.add(text_annotation, consider_rotation=False)
    document.save(outfile)


def text_annotation_get(infile, outfile):
    """Print text annotation rectangles on page 1."""
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        print(annotation.rect)


def text_annotation_delete(infile, outfile):
    """Delete text annotations from page 1."""
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)

def caret_annotations_add(infile, outfile):
    """Add a caret annotation to the first page."""
    document = ap.Document(infile)
    page = document.pages[1]

    # Create Caret Annotation for text insertion
    caret_annotation = ap.annotations.CaretAnnotation(
        page,
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    caret_annotation.title = "Aspose User"
    caret_annotation.subject = "Inserted text 1"
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page,
        ap.Rectangle(310, 713, 410, 730, True)
    )
    page.annotations.append(caret_annotation)

    document.save(outfile)


def caret_annotations_get(infile, outfile):
    """Print rectangle coordinates of caret annotations on page 1."""
    document = ap.Document(infile)

    page = document.pages[1]

    # Iterate through annotations and filter Caret annotations
    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.CARET:
            # Print annotation rectangle
            print(annot.rect)
  

def caret_annotations_delete(infile, outfile):
    """Delete caret annotations on page 1."""
    document = ap.Document(infile)
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
    document.save(outfile)


def replace_annotations_add(infile, outfile):
    """
    Add replace annotations to a PDF document to mark text that should be replaced.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> replace_annotations_add("sample.pdf", "output.pdf")

    Note:
        Replace annotations are used to indicate text that should be replaced.
    """
    # Open PDF document
    document = ap.Document(infile)
    page = document.pages[1]

    # Create Caret Annotation for text replacement
    caret_annotation = ap.annotations.CaretAnnotation(
        page,
        ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
    )
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.subject = "Inserted text 2"
    caret_annotation.title = "Aspose User"
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page,
        ap.Rectangle(310, 713, 410, 730, True)
    )
    # Create StrikeOut Annotation
    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        page,
        ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
    )
    strikeout_annotation.color = ap.Color.blue  
    strikeout_annotation.quad_points = [
        ap.Point(321.66, 739.416),
        ap.Point(365.664, 739.416),
        ap.Point(321.66, 728.508),
        ap.Point(365.664, 728.508)
    ]
    strikeout_annotation.subject = "Cross-out"
    strikeout_annotation.in_reply_to = caret_annotation
    strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP

    # Add annotations to the page
    page.annotations.append(caret_annotation)
    page.annotations.append(strikeout_annotation)

    # Save PDF document
    document.save(outfile)


def replace_annotations_get(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all replace annotations on a page.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): Not used.

    Returns:
        None

    Example:
        >>> replace_annotations_get("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all replace annotations found on the first page.
    """
    # Open PDF document
    document = ap.Document(infile)
    page = document.pages[1]

    # Iterate through annotations and filter Replace annotations
    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
            sa = cast(ap.annotations.StrikeOutAnnotation, annot)
            if (sa.in_reply_to is not None and sa.reply_type == ap.annotations.ReplyType.GROUP):
                # Print annotation rectangle
                print(f"Replace annotation rect: {sa.rect}")


def replace_annotations_delete(infile, outfile):
    """
    Delete all replace annotations from a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> replace_annotations_delete("sample.pdf", "output.pdf")

    Note:
        This function removes all replace annotations from the first page and saves the modified PDF.
    """
    # Open PDF document
    document = ap.Document(infile)
    page = document.pages[1]

    # Collect replace annotations first (avoid modifying collection while iterating)
    replace_annotations = [
        cast(ap.annotations.StrikeOutAnnotation, annot)
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
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
        ("Add Text Annotation", text_annotation_add),
        ("Get Text Annotation", text_annotation_get),
        ("Delete Text Annotation", text_annotation_delete),
        ("Add Caret Annotation", caret_annotations_add),
        ("Get Caret Annotation", caret_annotations_get),
        ("Delete Caret Annotation", caret_annotations_delete),
        ("Add Replace Annotation", replace_annotations_add),
        ("Get Replace Annotation", replace_annotations_get),
        ("Delete Replace Annotation", replace_annotations_delete),
    ]

    for name, func in examples:
        input_file_name = path.join(input_dir, "sample_n.pdf")
        output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
        try:
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
