from io import FileIO
import sys
from os import path
import aspose.pdf.facades as pdf_facades

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import set_license, initialize_data_dir

# Import data from XML
def import_xml_to_pdf_fields(infile, datafile, outfile):
    """Import form data from XML file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, 'r') as xml_input_stream:
        # Import data from XML into PDF form fields
        pdf_form.import_xml(xml_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)

# Import Data from FDF
def import_fdf_to_pdf_form(infile, datafile, outfile):
    """Import form data from FDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open FDF file as stream
    with open(datafile, 'rb') as fdf_input_stream:
        pdf_form.import_fdf(fdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)

# Import Data from XFDF
def import_data_from_xfdf(infile, datafile, outfile):
    """Import form data from XFDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XFDF file as stream
    with open(datafile, 'rb') as xfdf_input_stream:
        # Import data from XFDF into PDF form fields
        pdf_form.import_xfdf(xfdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)

# Import from JSON
def import_json_to_pdf_form(infile, datafile, outfile):
    """Import form data from JSON file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open JSON file as stream
    with FileIO(datafile, 'r') as json_stream:
        # Import data from JSON into PDF form fields
        form.import_json(json_stream)

    # Save updated PDF
    form.save(outfile)

# Replace from XFA data
def replace_xfa_data(infile, datafile, outfile):
    """Import form data from XFA file into PDF form fields."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Open XFA file as stream
    with FileIO(datafile, 'r') as xfa_stream:
        # Import data from XFA into PDF form fields
        form.set_xfa_data(xfa_stream)

    # Save updated PDF
    form.save(outfile)    


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
        ("Import Data from XML", import_xml_to_pdf_fields, "sample_form.xml"),
        ("Import Data from FDF", import_fdf_to_pdf_form, "sample_form.fdf"),
        ("Import Data from XFDF", import_data_from_xfdf, "sample_form.xfdf"),
        ("Import Values from JSON", import_json_to_pdf_form, "sample_form.json"),
        ("Replace XFA Data", replace_xfa_data, "sample_form_xfa.xml"),
    ]

    for name, func, data_file_name in examples:
        try:
            if (func.__name__ == "replace_xfa_data"):
                input_file_name = path.join(input_dir, "sample_xfa_form.pdf")
            else:
                input_file_name = path.join(input_dir, "sample_form_new.pdf")
            form_data_file_name = path.join(input_dir, data_file_name)
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, form_data_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Import Form Data examples finished.")


if __name__ == "__main__":
    run_all_examples()