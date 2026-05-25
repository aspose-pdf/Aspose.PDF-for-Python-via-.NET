import aspose.pdf as ap
from aspose.pdf import Rectangle, FileSpecification
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import SubmitFormAction
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_submit_button(input_file_name, output_file_name):
    """Add submit button to PDF form.

    Args:
        input_file_name (str): Path to input PDF.
        output_file_name (str): Path to output PDF.
    Returns:
        None
    """
    editor = ap.facades.FormEditor(input_file_name, output_file_name)
    editor.add_submit_btn(
        "submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475
    )
    editor.save()


def add_submit_action(input_file_name, output_file_name):
    """Add submit action to PDF form.

    Args:
        input_file_name (str): Path to input PDF.
        output_file_name (str): Path to output PDF.
    Returns:
        None
    """
    try:
        document = ap.Document(input_file_name)

        submit_action = ap.SubmitFormAction()
        submit_action.url = FileSpecification("http://localhost:3000/submit")
        submit_action.flags = (
            SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
        )

        rect = Rectangle(10, 10, 100, 40)
        submit_button = ButtonField(document.pages[1], rect)
        submit_button.partial_name = "SubmitButton"
        submit_button.value = "Submit"
        submit_button.actions.on_release_mouse_btn = submit_action

        document.form.add(submit_button, 1)
        document.save(output_file_name)

    except Exception as e:
        print(f"Error adding submit button: {e}")


def run_all_examples(data_dir=None, license_path=None):
    """Run acroforms posting examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add submit button", add_submit_button),
    ]

    for name, func in examples:
        try:
            input_file = path.join(input_dir, "StudentInfoFormElectronic.pdf")
            output_file = path.join(output_dir, "add_submit_button_out.pdf")

            func(input_file, output_file)
            print(f"✅ Success: {name} completed.")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")

    print(f"\nAll Acroforms posting examples finished. Check output in {output_dir}")


if __name__ == "__main__":
    run_all_examples()
