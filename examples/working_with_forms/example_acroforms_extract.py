import aspose.pdf as ap
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_values_from_all_fields(input_file_name):
    """Retrieve values from all AcroForm fields in a PDF.

    Args:
        input_file_name (str): Path to the input PDF file.
    Returns:
        dict: Mapping of field names to their values.
    Example:
        >>> values = get_values_from_all_fields("StudentInfoFormElectronic.pdf")
    Note:
        Uses ``ap.facades.Form`` to access form field names and their values.
    """
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values


def run_all_examples(data_dir=None, license_path=None):
    """Run acroforms extract examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override. Defaults to ``DATA_DIR``.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    input_file_name = path.join(input_dir, "StudentInfoFormElectronic.pdf")

    try:
        values = get_values_from_all_fields(input_file_name)
        print(f"✅ get_values_from_all_fields completed. Fields: {len(values)}")
    except Exception as e:
        print(f"❌ get_values_from_all_fields failed: {e}")

    print(f"\nAll Acroforms extract examples finished. Check input in {output_dir}")


if __name__ == "__main__":
    run_all_examples()
