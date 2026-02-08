from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

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

# Export Data to XML
def export_pdf_form_data_to_xml(infile, datafile):
    """Export PDF form data to XML file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, 'w') as xml_output_stream:
        # Export data from PDF form fields to XML
        pdf_form.export_xml(xml_output_stream)

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

# Export Data to FDF
def export_form_data_to_fdf(infile, outfile):
    """Export PDF form data to FDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create FDF file stream
    with open(outfile, 'wb') as fdf_output_stream:
        # Export form data to FDF file
        pdf_form.export_fdf(fdf_output_stream)

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

# Export Data to XFDF
def export_pdf_form_to_xfdf(infile, outfile):
    """Export PDF form data to XFDF file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Create XFDF file stream
    with open(outfile, "wb") as xfdf_output_stream:
        # Export form data to XFDF file
        pdf_form.export_xfdf(xfdf_output_stream)

# Export Data to JSON
def export_form_to_json(infile, outfile):
    """Export PDF form field values to JSON file."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Create JSON file stream
    with FileIO(outfile, 'w') as json_stream:
        # Export form field values to JSON
        form.export_json(json_stream, indented=True)

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

def run_all_examples(data_dir=None, license_path=None):
    """Run all import/export form data examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Export Data to XML", export_pdf_form_data_to_xml, "sample_form.xml"),
        ("Import Data from XML", import_xml_to_pdf_fields, "sample_form.xml"),
        ("Export Data to FDF", export_form_data_to_fdf, "sample_form.fdf"),
        ("Import Data from FDF", import_fdf_to_pdf_form, "sample_form.fdf"),
        ("Export Data to XFDF", export_pdf_form_to_xfdf, "sample_form.xfdf"),
        ("Import Data from XFDF", import_data_from_xfdf, "sample_form.xfdf"),
        ("Export Values to JSON", export_form_to_json, "sample_form.json"),
        ("Import Values from JSON", import_json_to_pdf_form, "sample_form.json"),
    ]

    for name, func, data_file_name in examples:
        try:
            if name.startswith("Import"):
                input_file_name = path.join(input_dir, "sample_form_new.pdf")
                form_data_file_name = path.join(input_dir, data_file_name)
                output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
                func(input_file_name, form_data_file_name, output_file_name)
            else:
                input_file_name = path.join(input_dir, "sample_form.pdf")
                output_file_name = path.join(output_dir, data_file_name)
                func(input_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Export/Import Form Data examples finished.")


if __name__ == "__main__":
    run_all_examples()