import sys
import os
import aspose.pdf.facades as pdf_facades

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir

def get_button_options(infile):
    
    raise NotImplementedError("get_button_option_values is missing")

    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get button option values for the "Gender" field
    option_values = pdf_form.get_button_option_values("Gender")

    # Iterate through option values
    enumerator = option_values.GetEnumerator()
    while enumerator.MoveNext():
        print(f"Key : {enumerator.Key}, Value : {enumerator.Value}")


def get_current_button_option_value(infile):
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Get current value of the "Gender" button field
    option_value = pdf_form.get_button_option_current_value("Gender")

    # Display result
    print(f"Current Value : {option_value}")



def run_all_examples(data_dir=None, license_path=None):
    """Run text adding examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
        Returns:
            None
    """

    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)
    infile = os.path.join(input_dir, "StudentInfoFormElectronic.pdf")
    examples = [
       ("Get button options", get_button_options),
       ("Get current button option value", get_current_button_option_value)
    ]

    for name, func in examples:

        try:
            func(infile)
            print(f"✅ Success: {name} completed.")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")



# Main execution
if __name__ == "__main__":
    run_all_examples()
