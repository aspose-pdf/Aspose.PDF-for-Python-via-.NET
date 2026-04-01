import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import sys
from os import path

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import set_license, initialize_data_dir

def add_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set JavaScript action for the field
    form_editor.set_field_script("Script_Demo_Button", "app.alert('Script 1 has been executed');")

    # Add JavaScript action to the field
    form_editor.add_field_script("Script_Demo_Button", "app.alert('Script 2 has been executed');")

    # Save output PDF file
    form_editor.save(output_file_name)

def set_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Add JavaScript action to the field
    form_editor.add_field_script("Script_Demo_Button", "app.alert('Script 1 has been executed');")

    # Set JavaScript action for the field
    form_editor.set_field_script("Script_Demo_Button", "app.alert('Script 2 has been executed');")

    # Save output PDF file
    form_editor.save(output_file_name)

def remove_field_script(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Remove JavaScript action from the field
    form_editor.remove_field_action("Script_Demo_Button")
    
    # Save output PDF file
    form_editor.save(output_file_name)

def set_submit_flag(input_file_name, output_file_name):    
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit flag for the form
    form_editor.set_submit_flag("Script_Demo_Button", ap.facades.SubmitFormFlag.XFDF)

    # Save output PDF file
    form_editor.save(output_file_name)

def set_submit_url(input_file_name, output_file_name):
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Set license
    set_license()

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(input_file_name)

    # Set submit URL for the button
    if not form_editor.set_submit_url("Script_Demo_Button", "http://www.example.com/submit"):
        raise Exception("Failed to set submit URL")

    # Save output PDF file
    form_editor.save(output_file_name)

def run_all_examples(data_dir=None, license_path=None):
    """Run all examples for adding scripts and submit actions with status reporting.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add Field Script", add_field_script),
        ("Set Field Script", set_field_script),
        ("Remove Field Script", remove_field_script),
        ("Set Submit Flag", set_submit_flag),
        ("Set Submit URL", set_submit_url),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, func.__name__ + ".pdf")
            output_file_name = path.join(output_dir, func.__name__ + ".pdf")
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Modifying Form Fields examples finished.")


if __name__ == "__main__":
    run_all_examples()
