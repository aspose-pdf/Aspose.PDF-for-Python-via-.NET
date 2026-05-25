"""
Navigation and interaction actions examples using Aspose.PDF.

This module demonstrates adding and removing various PDF actions:
- Named actions (print, hide fields)
- Page navigation buttons
- Submit form actions
- Document-level JavaScript launch actions
- Page-level open/close actions and their removal

All examples follow the repository conventions:
- Paths are resolved via examples/config.py helpers
- Operation functions accept file paths and save output PDFs
- Success/failure is reported by run_all_examples()

Requirements:
- Input files must exist under sample_data/input with expected names
- Optional Aspose license can be set via run_all_examples(license_path)
"""

import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_named_action_print(infile, outfile):
    """Add a print button to the first page.

    Creates a button labeled "Print" that triggers the system print dialog
    when clicked. The button is positioned near the bottom-left of the first
    page with a 1-pixel border.

    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to save the output PDF with the print button.

    Returns:
        None

    Example:
        >>> add_named_action_print("sample_data/input/add_named_action_print_in.pdf", "sample_data/output/add_named_action_print_out.pdf")

    Notes:
        - The input file must exist under sample_data/input.
        - Output will be written to sample_data/output.
    """

    document = ap.Document(infile)
    page = document.pages[1]

    # Create print button with specific dimensions and position
    rect = Rectangle(10, 10, 100, 40, True)
    print_button = ButtonField(page, rect)
    print_button.partial_name = "printButton"
    print_button.value = "Print"
    print_button.actions.on_release_mouse_btn = NamedAction(PredefinedAction.FILE_PRINT)

    # Add border for better visibility
    border = ap.annotations.Border(print_button)
    border.width = 1
    print_button.border = border

    # Add button to the form on page 1
    document.form.add(print_button, 1)
    document.save(outfile)


def add_named_action_hide(infile, outfile):
    """Add a hide button that toggles all checkbox fields.

    Creates a button labeled "Hide Checkboxes" that hides or shows
    all checkbox fields in the document. Useful for complex forms.

    Args:
        infile (str): Path to the input PDF file containing checkbox fields.
        outfile (str): Path to save the output PDF with the hide button.

    Returns:
        None

    Example:
        >>> add_named_action_hide("sample_data/input/add_named_action_hide_in.pdf", "sample_data/output/add_named_action_hide_out.pdf")

    Notes:
        - All existing `CheckboxField` instances are targeted by the action.
        - The button is placed on page 1.
    """

    document = ap.Document(infile)
    # Collect all checkbox fields in the document
    checkboxes = [
        field for field in document.form if is_assignable(field, CheckboxField)
    ]

    # Create the hide button
    rect = Rectangle(10, 410, 140, 440, True)
    hide_button = ButtonField(document.pages[1], rect)
    hide_button.partial_name = "HideButton"
    hide_button.value = "Hide Checkboxes"

    # Add HideAction to button - will hide all checkboxes when clicked
    hide_button.actions.on_release_mouse_btn = HideAction(checkboxes, True)

    # Add button to the form on page 1
    document.form.add(hide_button, 1)

    # Save the modified PDF
    document.save(outfile)


def add_navigation_buttons(infile, outfile):
    """Add page navigation buttons across the document.

    Adds four buttons on each page:
    - First Page: Navigate to the first page
    - Previous Page: Navigate to the previous page
    - Next Page: Navigate to the next page
    - Last Page: Navigate to the last page

    Buttons are automatically disabled when not applicable (e.g.,
    "Previous Page" is disabled on page 1; "Next Page" is disabled on the last page).

    Args:
        infile (str): Path to the input multi-page PDF file.
        outfile (str): Path to save the output PDF with navigation buttons.

    Returns:
        None

    Example:
        >>> add_navigation_buttons("sample_data/input/add_navigation_buttons_in.pdf", "sample_data/output/add_navigation_buttons_out.pdf")

    Notes:
        - Buttons use `NamedAction` with `PredefinedAction` for navigation.
        - Buttons have colored border/background for visibility.
    """

    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Add navigation buttons to each page
    for page in document.pages:
        for name, x_pos, action, is_readonly_fn in button_config:
            # Create button rectangle
            rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            # Disable button when not applicable
            button.read_only = is_readonly_fn(page.number, total_pages)
            button.actions.on_release_mouse_btn = NamedAction(action)
            document.form.add(button)

    document.save(outfile)


def add_submit_action(infile, outfile):
    """Add a submit button that posts form data to a URL.

    Creates a button that submits the form data to a specified URL when clicked.
    The action includes export format and click coordinate flags.

    Args:
        infile (str): Path to the input PDF form.
        outfile (str): Path to save the output PDF with the submit button.

    Returns:
        None

    Example:
        >>> add_submit_action("sample_data/input/add_submit_action_in.pdf", "sample_data/output/add_submit_action_out.pdf")

    Notes:
        - The default URL used here is http://localhost:3000/submit.
        - Adjust `submit_action.url` to target a real endpoint.
    """

    document = ap.Document(infile)

    # Create the submit action
    submit_action = SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
    )

    # Create the submit button
    rect = Rectangle(10, 10, 100, 40, True)
    submit_button = ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    # Add the button to the form on page 1
    document.form.add(submit_button, 1)

    # Save the document
    document.save(outfile)


def add_launch_actions(infile, outfile):
    """Add JavaScript launch actions for document events.

    Adds JavaScript actions that launch URLs when specific document events occur:
    - On document open: launches http://localhost:3000/open
    - Before saving: launches http://localhost:3000/save
    - Before printing: launches http://localhost:3000/print

    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to save the output PDF with document actions.

    Returns:
        None

    Example:
        >>> add_launch_actions("sample_data/input/add_launch_actions_in.pdf", "sample_data/output/add_launch_actions_out.pdf")

    Notes:
        - Uses `ap.annotations.JavascriptAction` with `app.launchURL()`.
        - URLs are opened in the default browser depending on viewer support.
    """

    document = ap.Document(infile)

    # Add JavaScript actions for document events
    document.open_action = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/open');"
    )
    document.actions.before_saving = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/save');"
    )
    document.actions.before_printing = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/print');"
    )

    document.save(outfile)


def add_page_actions(infile, outfile):
    """Add open/close actions to the third page.

    Adds two actions to page 3:
    - On page open: Navigate to the top with specific zoom via `GoToAction`.
    - On page close: Launch a URL with page-specific information via JavaScript.

    Args:
        infile (str): Path to the input multi-page PDF file.
        outfile (str): Path to save the output PDF with page actions.

    Returns:
        None

    Example:
        >>> add_page_actions("sample_data/input/add_page_actions_in.pdf", "sample_data/output/add_page_actions_out.pdf")

    Notes:
        - If the document has fewer than 3 pages, prints an error and returns without saving.
        - Uses `XYZExplicitDestination` to set position and zoom.
    """

    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]

    # Add GoTo action on page open - navigate to top of page
    action = ap.annotations.GoToAction(page)
    action.destination = ap.annotations.XYZExplicitDestination(
        page, 0, page.page_info.height, 1
    )
    page.actions.on_open = action

    # Add JavaScript action on page close
    page.actions.on_close = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/page/3');"
    )

    document.save(outfile)


def remove_page_actions(infile, outfile):
    """Remove all actions from the third page.

    Clears all page-specific actions previously added to page 3, including
    both `on_open` and `on_close` actions.

    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to save the output PDF with actions removed.

    Returns:
        None

    Example:
        >>> remove_page_actions("sample_data/input/remove_page_actions_in.pdf", "sample_data/output/remove_page_actions_out.pdf")

    Notes:
        - If the document has fewer than 3 pages, prints an error and returns without saving.
    """

    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]
    page.actions.remove_actions()

    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run all navigation and interaction examples with status reporting.

    Initializes licensing (optional) and sample data directories, then executes
    all example functions in this module, saving outputs to sample_data/output
    with the `{function_name}_out.pdf` naming convention.

    Args:
        data_dir (str, optional): Override base data directory. If None, it is
            derived from the script location and sample_data structure.
        license_path (str, optional): Path to Aspose license file. If None, runs
            in evaluation mode.

    Returns:
        None

    Example:
        >>> run_all_examples()
        >>> run_all_examples(data_dir=r"E:\Github\Aspose.PDF-for-Python-via-.NET\sample_data", license_path=r"C:\Path\Aspose.Total.lic")
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("add_named_action_print", add_named_action_print),
        ("add_named_action_hide", add_named_action_hide),
        ("add_navigation_buttons", add_navigation_buttons),
        ("add_submit_action", add_submit_action),
        ("add_launch_actions", add_launch_actions),
        ("add_page_actions", add_page_actions),
        ("remove_page_actions", remove_page_actions),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}_in.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()
