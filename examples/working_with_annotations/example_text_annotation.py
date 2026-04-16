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

def add_underline_with_quad_points(infile, outfile):
    """
    Add an underline annotation with quad points to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> add_underline_with_quad_points("sample.pdf", "output.pdf")

    Note:
        Sets quad_points to define the annotation area.
    """
    document = ap.Document(infile)

    rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)

    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "Inserted Underline with Quad Points"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    # Set quad points
    underlineAnnotation.quad_points = [
        ap.Point(rect.llx, rect.lly),
        ap.Point(rect.urx, rect.lly),
        ap.Point(rect.urx, rect.ury),
        ap.Point(rect.llx, rect.ury)
    ]

    document.pages[1].annotations.append(underlineAnnotation)
    document.save(outfile)

def get_underline_marked_text(infile, outfile):
    """
    Get marked text from underline annotations on the first page.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): Not used.

    Returns:
        None

    Example:
        >>> get_underline_marked_text("sample.pdf", "output.pdf")

    Note:
        Prints the marked text for each underline annotation.
    """
    document = ap.Document(infile)

    underlineAnnotations = [
        a for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for ua in underlineAnnotations:
        marked_text = ua.get_marked_text()
        print(f"Marked text: {marked_text}")

def get_underline_marked_text_fragments(infile, outfile):
    """
    Get marked text fragments from underline annotations on the first page.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): Not used.

    Returns:
        None

    Example:
        >>> get_underline_marked_text_fragments("sample.pdf", "output.pdf")

    Note:
        Prints the text of each fragment for each underline annotation.
    """
    document = ap.Document(infile)

    underlineAnnotations = [
        a for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for ua in underlineAnnotations:
        fragments = ua.get_marked_text_fragments()
        for frag in fragments:
            print(f"Fragment text: {frag.text}")

def delete_underline_by_title(infile, outfile):
    """
    Delete underline annotations with a specific title from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> delete_underline_by_title("sample.pdf", "output.pdf")

    Note:
        This function removes underline annotations with title "Aspose User" from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    underlineAnnotations = [
        a for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.UNDERLINE and a.title == "Aspose User"
    ]

    for ua in underlineAnnotations:
        document.pages[1].annotations.delete(ua)

    document.save(outfile)

def add_underline_and_flatten(infile, outfile):
    """
    Add an underline annotation to the first page and flatten it into the page content.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> add_underline_and_flatten("sample.pdf", "output.pdf")

    Note:
        The underline annotation is added and then flattened, making it part of the page content rather than an annotation.
    """
    document = ap.Document(infile)

    underlineAnnotation = ap.annotations.UnderlineAnnotation(
        document.pages[1], ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    underlineAnnotation.title = "Aspose User"
    underlineAnnotation.subject = "Inserted Underline to Flatten"
    underlineAnnotation.flags = ap.annotations.AnnotationFlags.PRINT
    underlineAnnotation.color = ap.Color.blue

    document.pages[1].annotations.append(underlineAnnotation)
    underlineAnnotation.flatten()  # Flatten the annotation into the page content

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
        ("text_strikeout_annotation_add", add_text_strikeout_annotation),
        ("text_strikeout_annotation_get", get_text_strikeout_annotation),
        ("text_strikeout_annotation_delete", delete_text_strikeout_annotation),
        ("text_highlight_annotation_add", add_text_highlight_annotation),
        ("text_strikeout_annotation_add", add_text_strikeout_annotation),
        ("text_squiggly_annotation_add", add_text_squiggly_annotation),
        ("text_underline_annotation_add", add_text_underline_annotation),
        ("text_highlight_annotation_get", get_text_highlight_annotation),
        ("text_strikeout_annotation_get", get_text_strikeout_annotation),
        ("text_squiggly_annotation_get", get_text_squiggly_annotation),
        ("text_underline_annotation_get", get_text_underline_annotation),
        ("text_highlight_annotation_delete", delete_text_highlight_annotation),
        ("text_strikeout_annotation_delete", delete_text_strikeout_annotation),
        ("text_squiggly_annotation_delete", delete_text_squiggly_annotation),
        ("text_underline_annotation_delete", delete_text_underline_annotation),
        ("text_underline_annotation_add", add_underline_with_quad_points),
        ("text_underline_annotation_get", get_underline_marked_text),
        ("text_underline_annotation_get", get_underline_marked_text_fragments),
        ("text_underline_annotation_delete", delete_underline_by_title),
        ("text_underline_annotation_add", add_underline_and_flatten),
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
