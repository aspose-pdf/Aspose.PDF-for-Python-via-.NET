from os import path
import aspose.pdf as ap
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir

def text_annotation_add(infile, outfile):
    """
    Add a text annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file
        outfile (str): The name of the output PDF file

    Returns:
        None

    Example:
        >>> text_annotation_add("sample.pdf", "output.pdf")

    Note:
        The annotation is positioned at coordinates (299.988, 613.664, 428.708, 680.769)
        and appears with a blue color and "Aspose User" as the title.
    """
    document = ap.Document(infile)

    textAnnotation = ap.annotations.TextAnnotation(
        document.pages[1], ap.Rectangle(299.988, 613.664, 428.708, 680.769, True)
    )
    textAnnotation.title = "Aspose User"
    textAnnotation.subject = "Inserted text 1"
    textAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    textAnnotation.color = ap.Color.blue

    document.pages[1].annotations.add(textAnnotation, consider_rotation=False)
    document.save(outfile)


def text_annotation_get(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all text annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> text_annotation_get("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all text annotations found on the first page.
    """
    document = ap.Document(infile)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        print(ta.rect)


def text_annotation_delete(infile, outfile):
    """
    Delete all text annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> text_annotation_delete("sample.pdf", "output.pdf")

    Note:
        This function removes all text annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    textAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.TEXT)
    ]

    for ta in textAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(outfile)


def free_text_annotation_add(infile, outfile):
    """
    Add a free text annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> free_text_annotation_add("sample.pdf", "output.pdf")

    Note:
        The free text annotation is positioned at coordinates (299, 713, 308, 720)
        with light green color and "Aspose User" as the title.
    """
    document = ap.Document(infile)

    freeTextAnnotation = ap.annotations.FreeTextAnnotation(
        document.pages[1], ap.Rectangle(299, 713, 308, 720, True), ap.annotations.DefaultAppearance()
    )
    freeTextAnnotation.title = "Aspose User"
    freeTextAnnotation.color = ap.Color.light_green

    document.pages[1].annotations.append(freeTextAnnotation)
    document.save(outfile)  


def free_text_annotation_get(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all free text annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> free_text_annotation_get("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all free text annotations found on the first page.
    """
    document = ap.Document(infile)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        print(fa.rect)  


def free_text_annotation_delete(infile, outfile):
    """
    Delete all free text annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> free_text_annotation_delete("sample.pdf", "output.pdf")

    Note:
        This function removes all free text annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    freeTextAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.FREE_TEXT)
    ]

    for fa in freeTextAnnotations:
        document.pages[1].annotations.delete(fa)

    document.save(outfile)    


def add_text_strikeout_annotation(infile, outfile):
    """
    Add a strikeout annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> add_text_strikeout_annotation("sample.pdf", "output.pdf")

    Note:
        The strikeout annotation is positioned at coordinates (299.988, 713.664, 308.708, 720.769)
        with blue color and "Aspose User" as the title.
    """
    document = ap.Document(infile)

    strikeoutAnnotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    strikeoutAnnotation.title = "Aspose User"
    strikeoutAnnotation.subject = "Inserted text 1"
    strikeoutAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeoutAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeoutAnnotation)
    document.save(outfile)


def get_text_strikeout_annotation(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all strikeout annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> get_text_strikeout_annotation("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all strikeout annotations found on the first page.
    """
    document = ap.Document(infile)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        print(pa.rect)


def delete_text_strikeout_annotation(infile, outfile):
    """
    Delete all strikeout annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> delete_text_strikeout_annotation("sample.pdf", "output.pdf")

    Note:
        This function removes all strikeout annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    StrikeoutAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT)
    ]

    for pa in StrikeoutAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(outfile)
    

def run_all_examples(data_dir=None, license_path=None):
    """Run adding text annotations examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("text_annotation_add", text_annotation_add),
        ("text_annotation_get", text_annotation_get),
        ("text_annotation_delete", text_annotation_delete),
        ("free_text_annotation_add", free_text_annotation_add),
        ("free_text_annotation_get", free_text_annotation_get),
        ("free_text_annotation_delete", free_text_annotation_delete),
        ("add_text_strikeout_annotation", add_text_strikeout_annotation),
        ("get_text_strikeout_annotation", get_text_strikeout_annotation),
        ("delete_text_strikeout_annotation", delete_text_strikeout_annotation),
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
