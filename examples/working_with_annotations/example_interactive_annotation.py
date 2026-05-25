from os import path
import sys

import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def link_add(infile, outfile):
    """
    Add a link annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> link_add("sample.pdf", "output.pdf")

    Note:
        This function finds the text "file" on the first page and creates a link annotation
        that navigates to www.aspose.com when clicked.
    """
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

    # Accept the absorber for the 1st page only
    document.pages[1].accept(text_fragment_absorber)

    phone_number_fragment = text_fragment_absorber.text_fragments[1]

    link_annotation = ap.annotations.LinkAnnotation(document.pages[1], phone_number_fragment.rectangle)
    link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")

    # Add annotation to page
    document.pages[1].annotations.append(link_annotation)
    document.save(outfile)


def link_get(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all link annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> link_get("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all link annotations found on the first page.
    """
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        print(link_annotation.rect)


def link_delete(infile, outfile):
    """
    Delete all link annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> link_delete("sample.pdf", "output.pdf")

    Note:
        This function removes all link annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        document.pages[1].annotations.delete(link_annotation)

    document.save(outfile)


def line_annotation_add(infile, outfile):
    """Add a line annotation to the first page."""
    document = ap.Document(infile)

    # Create Line Annotation
    line_annotation = ap.annotations.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439, True),
        ap.Point(556, 99),
        ap.Point(556, 443)
    )

    # Set properties
    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
    line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW

    # Create Popup Annotation
    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266, True)
    )

    line_annotation.popup = popup

    # Add annotation to the page
    document.pages[1].annotations.append(line_annotation)

    # Save PDF document
    document.save(outfile)


def navigation_buttons_add(infile, outfile):
    """Add next/previous navigation buttons to each page."""
    button_config = [        
        ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE ),
        ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE ),        
    ]

    document = ap.Document(infile)
    document.pages.add()  # Ensure there are at least 2 pages for navigation
    
    # Add navigation buttons to each page
    for page in document.pages:
        for name, x_pos, action in button_config:
            # Create button rectangle
            rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ap.forms.ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            # Disable button when not applicable            
            button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
            document.form.add(button)

    document.save(outfile)


def print_button_add(infile, outfile):
    """Create a one-page PDF and add a print button."""
    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Define the rectangle for the button
    rect = ap.Rectangle(72, 748, 164, 768, True)

    # Create a button field
    print_button = ap.forms.ButtonField(page, rect)
    print_button.alternate_name = "Print current document"
    print_button.color = ap.Color.black
    print_button.partial_name = "printBtn1"
    print_button.value = "Print Document"
    print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
        ap.annotations.PredefinedAction.FILE_PRINT
    )

    # Set the border style for the button
    border = ap.annotations.Border(print_button)
    border.style = ap.annotations.BorderStyle.SOLID
    border.width = 2
    print_button.border = border

    # Set border and background color characteristics
    print_button.characteristics.border = ap.Color.blue.to_rgb()
    print_button.characteristics.background = ap.Color.light_blue.to_rgb()

    # Add the button to the form
    document.form.add(print_button)

    # Save PDF document
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run all interactive annotation examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("link_add", link_add),
        ("link_get", link_get),
        ("link_delete", link_delete),        
        ("navigation_buttons_add", navigation_buttons_add),
        ("print_button_add", print_button_add),
    ]

    for name, func in examples:
        input_file_name = path.join(input_dir, "sample_n.pdf")
        output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
        try:
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()
