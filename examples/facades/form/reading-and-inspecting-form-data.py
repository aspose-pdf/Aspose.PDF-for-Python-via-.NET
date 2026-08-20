import sys
from os import path
import aspose.pdf.facades as pdf_facades

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import set_license, initialize_data_dir  # noqa: E402


# Get field values
def get_field_values(infile):
    """Get field values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get field values by their names
    field_names = ["First Name", "Last Name"]
    for field_name in field_names:
        value = pdf_form.get_field(field_name)
        print(f"Value of '{field_name}': {value}")


# Get rich text values
def get_rich_text_values(infile):
    """Get rich text values from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get rich text values by their names
    field_names = ["Summary"]
    for field_name in field_names:
        rich_text_value = pdf_form.get_rich_text(field_name)
        print(f"Rich text value of '{field_name}': {rich_text_value}")


# Get radio button options
def get_radio_button_options(infile):
    """Get radio button options from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get radio button options by their names
    field_names = ["WorkType"]
    for field_name in field_names:
        options = pdf_form.get_button_option_current_value(field_name)
        print(f"Options for '{field_name}': {options}")


# Resolve full field names
def resolve_full_field_names(infile):
    """Resolve full field names in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Resolve full field names
    for field in pdf_form.field_names:
        name = pdf_form.get_full_field_name(field)
        print(f"Full field name: {name}")


# Get required field names
def get_required_field_names(infile):
    """Get required field names from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get required field names
    for field in pdf_form.field_names:
        if pdf_form.is_required_field(field):
            print(f"Required field: {field}")


# get field facades
def get_field_facades(infile):
    """Get field facades from a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get field facades
    for field in pdf_form.field_names:
        facade = pdf_form.get_field_facade(field)
        print(f"Field facade for '{field}': {facade.box.location}, {facade.box.size}")
        print(f"Field facade for '{field}': {facade.font.name}, {facade.font_size}")


def run_all_examples(data_dir=None, license_path=None):
    """Run all import form data examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    examples = [
        ("Get Field Values", get_field_values),
        ("Get Rich Text Values", get_rich_text_values),
        ("Get Radio Button Options", get_radio_button_options),
        ("Resolve Full Field Names", resolve_full_field_names),
        ("Get Required Field Names", get_required_field_names),
        ("Get Field Facades", get_field_facades),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}_in.pdf")
            func(input_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll managing PDF form fields examples finished.")


if __name__ == "__main__":
    run_all_examples()
