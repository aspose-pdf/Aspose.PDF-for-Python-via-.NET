from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# AddFieldScript
def add_field_script():
    # Initialize data directory path
    data_dir = initialize_data_dir()

    # Set license
    set_license()

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(data_dir + "input.pdf")

    # Add JavaScript action to the field
    form_editor.add_field_script("TextField1", ap.facades.FieldScriptType.OnFocus, "app.alert('Field is focused');")

    # Save output PDF file
    form_editor.save(data_dir + "output.pdf")

# SetFieldScript    
def set_field_script():
    # Initialize data directory path
    data_dir = initialize_data_dir()

    # Set license
    set_license()

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(data_dir + "input.pdf")

    # Set JavaScript action for the field
    form_editor.set_field_script("TextField1", ap.facades.FieldScriptType.OnBlur, "app.alert('Field is blurred');")

    # Save output PDF file
    form_editor.save(data_dir + "output_set_field_script.pdf")

# RemoveFieldAction 
def remove_field_script():
    # Initialize data directory path
    data_dir = initialize_data_dir()

    # Set license
    set_license()

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(data_dir + "input.pdf")

    # Remove JavaScript action from the field
    form_editor.remove_field_script("TextField1", ap.facades.FieldScriptType.OnFocus)

    # Save output PDF file
    form_editor.save(data_dir + "output_remove_field_script.pdf")

# SetSubmitFlag
def set_submit_flag():
    # Initialize data directory path
    data_dir = initialize_data_dir()

    # Set license
    set_license()

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(data_dir + "input.pdf")

    # Set submit flag for the form
    form_editor.set_submit_flag("SubmitButton1", ap.facades.SubmitFlag.IncludeNoValueFields)

    # Save output PDF file
    form_editor.save(data_dir + "output_set_submit_flag.pdf")

# SetSubmitUrl
def set_submit_url():
    # Initialize data directory path
    data_dir = initialize_data_dir()

    # Set license
    set_license()

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open input PDF file
    form_editor.bind_pdf(data_dir + "input.pdf")

    # Set submit URL for the button
    form_editor.set_submit_url("SubmitButton1", "http://www.example.com/submit")

    # Save output PDF file
    form_editor.save(data_dir + "output_set_submit_url.pdf")

def run_all_examples(data_dir=None, license_path=None):
    """ 

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("AddFieldScript", add_field_script, "output_add_field_script.pdf"),
        ("SetFieldScript", set_field_script, "output_set_field_script.pdf"),
        ("RemoveFieldScript", remove_field_script, "output_remove_field_script.pdf"),
        ("SetSubmitFlag", set_submit_flag, "output_set_submit_flag.pdf"),
        ("SetSubmitUrl", set_submit_url, "output_set_submit_url.pdf"),
    ]

    for name, func, data_file_name in examples:
        try:
            input_file_name = path.join(input_dir, "input.pdf")
            output_file_name = path.join(output_dir, data_file_name)
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Modifying Form Fields examples finished.")


if __name__ == "__main__":
    run_all_examples()            