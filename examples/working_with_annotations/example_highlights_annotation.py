from os import path
import aspose.pdf as ap
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir

def add_text_highlight_annotation(infile, outfile):
    """
    Add a highlight annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> add_text_highlight_annotation("sample.pdf", "output.pdf")

    Note:
        The highlight annotation is positioned at coordinates (300, 750, 320, 770).
    """
    document = ap.Document(infile)

    # Create Circle Annotation
    highlightAnnotation = ap.annotations.HighlightAnnotation(
        document.pages[1], ap.Rectangle(300, 750, 320, 770, True)
    )
    document.pages[1].annotations.append(highlightAnnotation)
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


def add_text_squiggly_annotation(infile, outfile):
    """
    Add a squiggly annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> add_text_squiggly_annotation("sample.pdf", "output.pdf")

    Note:
        The squiggly annotation is positioned at coordinates (67, 317, 261, 459)
        with blue color and "John Smith" as the title.
    """
    document = ap.Document(infile)
    page = document.pages[1]
    squigglyAnnotation = ap.annotations.SquigglyAnnotation(page, ap.Rectangle(67, 317, 261, 459, True))
    squigglyAnnotation.title = "John Smith"
    squigglyAnnotation.color = ap.Color.blue

    page.annotations.append(squigglyAnnotation)

    document.save(outfile)
    

def add_text_underline_annotation(infile, outfile):
    """
    Add an underline annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> add_text_underline_annotation("sample.pdf", "output.pdf")

    Note:
        The underline annotation is positioned at coordinates (299.988, 713.664, 308.708, 720.769)
        with blue color and "Aspose User" as the title.
    """
    document = ap.Document(infile)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "Inserted Underline 1"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(outfile)


def get_text_highlight_annotation(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all highlight annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> get_text_highlight_annotation("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all highlight annotations found on the first page.
    """
    document = ap.Document(infile)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for ha in highlightAnnotations:
        print(ha.rect)


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


def get_text_squiggly_annotation(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all squiggly annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> get_text_squiggly_annotation("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all squiggly annotations found on the first page.
    """
    document = ap.Document(infile)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        print(pa.rect)


def get_text_underline_annotation(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all underline annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> get_text_underline_annotation("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all underline annotations found on the first page.
    """
    document = ap.Document(infile)
    UnderlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in UnderlineAnnotations:
        print(ta.rect)   


def delete_text_highlight_annotation(infile, outfile):
    """
    Delete all highlight annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> delete_text_highlight_annotation("sample.pdf", "output.pdf")

    Note:
        This function removes all highlight annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(outfile)


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


def delete_text_squiggly_annotation(infile, outfile):
    """
    Delete all squiggly annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> delete_text_squiggly_annotation("sample.pdf", "output.pdf")

    Note:
        This function removes all squiggly annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    squigglyAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.SQUIGGLY)
    ]

    for pa in squigglyAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(outfile)


def delete_text_underline_annotation(infile, outfile):
    """
    Delete all underline annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> delete_text_underline_annotation("sample.pdf", "output.pdf")

    Note:
        This function removes all underline annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    underlineAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.UNDERLINE)
    ]

    for ta in underlineAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(outfile)         

def run_all_examples(data_dir=None, license_path=None):
    """Run adding highlights annotations examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("add_text_highlight_annotation", add_text_highlight_annotation),
        ("add_text_strikeout_annotation", add_text_strikeout_annotation),
        ("add_text_squiggly_annotation", add_text_squiggly_annotation),
        ("add_text_underline_annotation", add_text_underline_annotation),
        ("get_text_highlight_annotation", get_text_highlight_annotation),
        ("get_text_strikeout_annotation", get_text_strikeout_annotation),
        ("get_text_squiggly_annotation", get_text_squiggly_annotation),
        ("get_text_underline_annotation", get_text_underline_annotation),
        ("delete_text_highlight_annotation", delete_text_highlight_annotation),
        ("delete_text_strikeout_annotation", delete_text_strikeout_annotation),
        ("delete_text_squiggly_annotation", delete_text_squiggly_annotation),
        ("delete_text_underline_annotation", delete_text_underline_annotation),
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
