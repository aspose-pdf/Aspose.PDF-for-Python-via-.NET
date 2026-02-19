# Flatten Specific Fields
# ├── Flatten All Fields
# └── Rename Form Fields    

from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Flatten specific fields
def flatten_specific_fields(infile, outfile):
    """Flatten specific fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten specific fields by their names
    fields_to_flatten = ["First Name", "Last Name"]
    for field_name in fields_to_flatten:
        pdf_form.flatten_field(field_name)

    # Save updated PDF
    pdf_form.save(outfile)

# Flatten all fields
def flatten_all_fields(infile, outfile):
    """Flatten all fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Flatten all fields in the PDF document
    pdf_form.flatten_all_fields()

    # Save updated PDF
    pdf_form.save(outfile)

# Rename form fields
def rename_form_fields(infile, outfile):
    """Rename form fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Rename form fields by providing a mapping of old names to new names
    field_renaming_map = [
        ("First Name", "NewFirstName"),
        ("Last Name", "NewLastName")
    ]
    for old_name, new_name in field_renaming_map:
        pdf_form.rename_field(old_name, new_name)

    # Save updated PDF
    pdf_form.save(outfile)

def run_all_examples(data_dir=None, license_path=None):
    """Run all import form data examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Flatten Specific Fields", flatten_specific_fields),
        ("Flatten All Fields", flatten_all_fields),
        ("Rename Form Fields", rename_form_fields)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "sample_form.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll managing PDF form fields examples finished.")


if __name__ == "__main__":
    run_all_examples()    