from io import FileIO, StringIO
import json
import sys
from os import path
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir

def import_data_from_xml(input_file_name, data_file_name, output_file_name):
    """Import form data from XML file.

    Args:
        input_file_name (str): Path to input PDF.
        data_file_name (str): Path to XML data file.
        output_file_name (str): Path to output PDF.
    Returns:
        None
    """
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xml(f)

    form.save(output_file_name)


def export_data_to_xml(input_file_name, output_file_name):
    """Export form data to XML file.

    Args:
        input_file_name (str): Path to input PDF.
        output_file_name (str): Path to XML output file.
    Returns:
        None
    """
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)


def import_data_from_fdf(input_file_name, data_file_name, output_file_name):
    """Import form data from FDF file.

    Args:
        input_file_name (str): Path to input PDF.
        data_file_name (str): Path to FDF data file.
        output_file_name (str): Path to output PDF.
    Returns:
        None
    """
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_fdf(f)
        form.save(output_file_name)


def export_data_to_fdf(input_file_name, output_file_name):
    """Export form data to FDF file.

    Args:
        input_file_name (str): Path to input PDF.
        output_file_name (str): Path to FDF output file.
    Returns:
        None
    """
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)


def import_data_from_xfdf(input_file_name, data_file_name, output_file_name):
    """Import form data from XFDF file.

    Args:
        input_file_name (str): Path to input PDF.
        data_file_name (str): Path to XFDF data file.
        output_file_name (str): Path to output PDF.
    Returns:
        None
    """
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xfdf(f)
        form.save(output_file_name)


def export_data_to_xfdf(input_file_name, output_file_name):
    """Export form data to XFDF file.

    Args:
        input_file_name (str): Path to input PDF.
        output_file_name (str): Path to XFDF output file.
    Returns:
        None
    """
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)


def import_data_from_another_pdf(input_file_name, output_file_name):
    """Import form data from another PDF.

    Args:
        input_file_name (str): Path to source PDF.
        output_file_name (str): Path to destination PDF.
    Returns:
        None
    """
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    form_source.bind_pdf(input_file_name)
    form_dest.bind_pdf(output_file_name)

    with StringIO() as f:
        form_source.export_xfdf(f)
        form_dest.import_xfdf(f)
        form_dest.save()


def extract_form_fields_to_json(input_file_name, output_file_name):
    """Extract form fields to JSON file.

    Args:
        input_file_name (str): Path to input PDF.
        output_file_name (str): Path to JSON output file.
    Returns:
        None
    """
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)


def extract_form_fields_to_json_doc(input_file_name, output_file_name):
    """Extract form fields to JSON document.

    Args:
        input_file_name (str): Path to input PDF.
        output_file_name (str): Path to JSON output file.
    Returns:
        None
    """
    form = ap.facades.Form(input_file_name)
    form_data = {}
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    json_string = json.dumps(form_data, indent=4)

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)


def run_all_examples(data_dir=None, license_path=None):
    """Run acroforms import/export examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    base_file = path.join(input_dir, "StudentInfoFormElectronic.pdf")
    xml_file = path.join(output_dir, "StudentInfoFormElectronic.xml")
    fdf_file = path.join(output_dir, "StudentInfoFormElectronic.fdf")
    xfdf_file = path.join(output_dir, "StudentInfoFormElectronic.xfdf")
    examples = [
        ("export_xml", lambda: export_data_to_xml(base_file, xml_file)),
        ("import_xml", lambda: import_data_from_xml(base_file, xml_file, path.join(output_dir, "StudentInfoFormElectronic_xml.pdf"))),
        ("export_fdf", lambda: export_data_to_fdf(base_file, fdf_file)),
        ("import_fdf", lambda: import_data_from_fdf(base_file, fdf_file, path.join(output_dir, "StudentInfoFormElectronic_fdf.pdf"))),
        ("export_xfdf", lambda: export_data_to_xfdf(base_file, xfdf_file)),
        ("import_xfdf", lambda: import_data_from_xfdf(base_file, xfdf_file, path.join(output_dir, "StudentInfoFormElectronic_xfdf.pdf"))),
        ("extract_json", lambda: extract_form_fields_to_json(base_file, path.join(output_dir, "StudentInfoFormElectronic1.json"))),
        ("extract_json_doc", lambda: extract_form_fields_to_json_doc(base_file, path.join(output_dir, "StudentInfoFormElectronic2.json"))),
    ]

    for name, func in examples:
        try:
            func()
            print(f"✅ Success: {name} completed.")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")

    print(f"\nAll Acroforms import/export examples finished. Check output in {output_dir}")


if __name__ == "__main__":
    run_all_examples()
