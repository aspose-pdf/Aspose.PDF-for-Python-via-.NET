import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def clear_text_in_form(input_file_name, output_file_name):
    """Clear text in form XObjects on first page.

    Args:
        input_file_name (str): Path to input PDF.
        output_file_name (str): Path to output PDF.
    Returns:
        None
    """
    document = ap.Document(input_file_name)

    forms = document.pages[1].resources.forms

    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            absorber = ap.text.TextFragmentAbsorber()
            absorber.visit(form)

            for fragment in absorber.text_fragments:
                fragment.text = ""

    document.save(output_file_name)


def set_field_limit(input_file_name, output_file_name):
    """Set character limit for a form field.

    Args:
        input_file_name (str): Path to input PDF.
        output_file_name (str): Path to output PDF.
    Returns:
        None
    """
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)


def get_field_limit(input_file_name):
    """Get character limit for first form field.

    Args:
        input_file_name (str): Path to input PDF.
    Returns:
        None
    """
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {textBoxField.max_len}")


def set_form_field_font(input_file_name, output_file_name):
    """Set font for first form field.

    Args:
        input_file_name (str): Path to input PDF.
        output_file_name (str): Path to output PDF.
    Returns:
        None
    """
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        textBoxField.default_appearance = ap.annotations.DefaultAppearance(
            font, 10, ap.Color.black.to_rgb()
        )

    document.save(output_file_name)


def delete_form_field(input_file_name, output_file_name):
    """Delete a specific form field by name.

    Args:
        input_file_name (str): Path to input PDF.
        output_file_name (str): Path to output PDF.
    Returns:
        None
    """
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)


def run_all_examples(data_dir=None, license_path=None):
    """Run acroforms modification examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    input_file = path.join(input_dir, "StudentInfoFormElectronic.pdf")

    examples = [
        ("clear_text", clear_text_in_form),
        ("set_field_limit", set_field_limit),
        ("get_field_limit", get_field_limit),
        ("set_form_field_font", set_form_field_font),
        ("delete_form_field", delete_form_field),
    ]

    for name, func in examples:
        try:
            output_file = path.join(output_dir, f"{func.__name__}_out.pdf")
            if func.__name__ == "get_field_limit":
                get_field_limit(input_file)
            else:
                func(input_file, output_file)
            print(f"✅ Success: {name} completed.")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")

    print(
        f"\nAll Acroforms modification examples finished. Check output in {output_dir}"
    )


if __name__ == "__main__":
    run_all_examples()
