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
        ("add_caret_annotations", add_caret_annotations),
        ("get_caret_annotations", get_caret_annotations),
        ("delete_caret_annotation", delete_caret_annotation),

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
