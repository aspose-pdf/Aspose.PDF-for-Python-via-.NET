import aspose.pdf as ap
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def fill_form(input_file_name, output_file_name):
    """Fill out AcroForm fields in a PDF with provided values and save.

    Uses a predefined mapping to update fields if present.

    Args:
        input_file_name (str): Path to the input PDF file.
        output_file_name (str): Path to the output PDF file.
    Returns:
        None
    Example:
        >>> fill_form("StudentInfoFormElectronic.pdf", "output_filled.pdf")
    Note:
        Only fields present in the ``new_field_values`` mapping are modified.
    """
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New",
    }

    form = ap.facades.Form(input_file_name)

    for field_name in form.field_names:
        if field_name in new_field_values:
            form.fill_field(field_name, new_field_values[field_name])

    form.save(output_file_name)


def run_all_examples(data_dir=None, license_path=None):
    """Run acroforms fill examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override. Defaults to ``DATA_DIR``.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    input_file_name = path.join(input_dir, "StudentInfoFormElectronic.pdf")
    output_file_name = path.join(output_dir, "StudentInfoFormElectronic_out.pdf")

    try:
        fill_form(input_file_name, output_file_name)
        print(f"✅ Success: fill_form completed. Output: {output_file_name}")
    except Exception as e:
        print(f"❌ Failed: fill_form - {e}")

    print(f"\nAll Acroforms fill examples finished. Check output in {output_file_name}")


if __name__ == "__main__":
    run_all_examples()
