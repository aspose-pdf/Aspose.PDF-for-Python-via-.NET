from os import path
import aspose.pdf as ap
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

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
    # Create TextFragmentAbsorber object to find a phone number
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Accept the absorber for the 1st page only
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Create Link Annotation and set the action to call a phone number
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Add annotation to page
    document.pages[1].annotations.append(linkAnnotation)
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
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)    


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
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(outfile)


def add_line_annotation():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Open PDF document
    document = ap.Document(data_dir + "Appartments.pdf")

    # Create Line Annotation
    line_annotation = ann.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439),
        ap.Point(556, 99),
        ap.Point(556, 443)
    )

    # Set properties
    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ann.LineEnding.open_arrow
    line_annotation.ending_style = ann.LineEnding.open_arrow

    # Create Popup Annotation
    popup = ann.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266)
    )

    line_annotation.popup = popup

    # Add annotation to the page
    document.pages[1].annotations.append(line_annotation)

    # Save PDF document
    document.save(data_dir + "AddLineAnnotation_out.pdf")    


def add_navigation_buttons():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Open PDF document
    document = ap.Document(data_dir + "JSON Fundamenals.pdf")

    # Create an array of button fields
    buttons = [None] * 4

    # Define alternate names and normal captions
    alternate_names = [
        "Go to first page",
        "Go to prev page",
        "Go to next page",
        "Go to last page"
    ]

    normal_captions = ["First", "Prev", "Next", "Last"]

    # Define predefined actions
    actions = [
        ann.PredefinedAction.first_page,
        ann.PredefinedAction.prev_page,
        ann.PredefinedAction.next_page,
        ann.PredefinedAction.last_page
    ]

    # Define border and background colors
    clr_border = drawing.Color.from_argb(255, 0, 255, 0)
    clr_background = drawing.Color.from_argb(255, 0, 96, 70)

    # Create buttons (not yet attached to pages)
    for i in range(4):
        rect = ap.Rectangle(32 + i * 80, 28, 104 + i * 80, 68)

        buttons[i] = forms.ButtonField(document, rect)
        buttons[i].alternate_name = alternate_names[i]
        buttons[i].color = ap.Color.white
        buttons[i].normal_caption = normal_captions[i]

        # Set navigation action
        buttons[i].on_activated = ann.NamedAction(actions[i])

        # Set border
        border = ann.Border(buttons[i])
        border.style = ann.BorderStyle.solid
        border.width = 2
        buttons[i].border = border

        # Set colors
        buttons[i].characteristics.border = clr_border
        buttons[i].characteristics.background = clr_background

    # Add buttons to each page
    for page_index in range(1, len(document.pages) + 1):
        for i in range(4):
            document.form.add(buttons[i], f"btn{page_index}_{i + 1}", page_index)

    # Disable buttons on first and last pages
    document.form["btn1_1"].read_only = True
    document.form["btn1_2"].read_only = True

    last_page = len(document.pages)
    document.form[f"btn{last_page}_3"].read_only = True
    document.form[f"btn{last_page}_4"].read_only = True

    # Save PDF document
    document.save(data_dir + "NavigationButtons_out.pdf")

def add_print_button():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Define the rectangle for the button
    rect = ap.Rectangle(72, 748, 164, 768)

    # Create a button field
    print_button = forms.ButtonField(page, rect)
    print_button.alternate_name = "Print current document"
    print_button.color = ap.Color.black
    print_button.partial_name = "printBtn1"
    print_button.normal_caption = "Print Document"

    # Set the border style for the button
    border = ann.Border(print_button)
    border.style = ann.BorderStyle.solid
    border.width = 2
    print_button.border = border

    # Set border and background color characteristics
    print_button.characteristics.border = drawing.Color.from_argb(255, 0, 0, 255)
    print_button.characteristics.background = drawing.Color.from_argb(255, 0, 191, 255)

    # Add the button to the form
    document.form.add(print_button)

    # Save PDF document
    document.save(data_dir + "PrintButton_out.pdf")    
    

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
        ("line_annotation_add", add_line_annotation),
        ("navigation_buttons_add", add_navigation_buttons),
        ("print_button_add", add_print_button)

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
