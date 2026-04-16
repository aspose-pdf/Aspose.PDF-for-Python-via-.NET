import sys
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
from os import path


sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir

def watermark_add(infile, outfile):
    """
    Add a watermark annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> watermark_add("sample.pdf", "output.pdf")

    Note:
        The watermark is positioned at coordinates (100, 0, 400, 100) with blue text
        at 25pt font size and 50% opacity.
    """
    document = ap.Document(infile)
    # Create Annotation
    # Load Page object to add Annotation
    page = document.pages[1]

    # Create Annotation
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Add annotation into Annotation collection of Page
    page.annotations.append(wa)

    # Create TextState for Font settings
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Set opacity level of Annotation Text
    wa.opacity = 0.5

    # Add Text in Annotation
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(outfile)


def watermark_get(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all watermark annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> watermark_get("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all watermark annotations found on the first page.
    """
    document = ap.Document(infile)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)    


def watermark_delete(infile, outfile):
    """
    Delete all watermark annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> watermark_delete("sample.pdf", "output.pdf")

    Note:
        This function removes all watermark annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

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
        ("Add Watermark Annotation", watermark_add, ["sample.pdf", "output_watermark_add.pdf"]),
        ("Get Watermark Annotation", watermark_get, ["sample.pdf", "output_watermark_get.pdf"]),
        ("Delete Watermark Annotation", watermark_delete, ["sample.pdf", "output_watermark_delete.pdf"])

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
