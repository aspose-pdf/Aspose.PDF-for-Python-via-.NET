from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

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

# Extract XFA Data
def export_xfa_data(infile, outfile):
    """Export XFA form data."""
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)
    
    with FileIO(outfile, 'w') as stream:
        # Export form field values to JSON
        form.extract_xfa_data(stream)

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
        ("Export Data to FDF", export_form_data_to_fdf, "sample_form.fdf"),
        ("Export Data to XFDF", export_pdf_form_to_xfdf, "sample_form.xfdf"),
        ("Export Values to JSON", export_form_to_json, "sample_form.json"),
        ("Export XFA Data", export_xfa_data, "sample_form_xfa.xml"),
    ]

    for name, func, data_file_name in examples:
        try:
            if (func.__name__ == "export_xfa_data"):
                input_file_name = path.join(input_dir, "sample_xfa_form.pdf")
            else:
                input_file_name = path.join(input_dir, "sample_form.pdf")
            output_file_name = path.join(output_dir, data_file_name)
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Export Form Data examples finished.")


if __name__ == "__main__":
    run_all_examples()