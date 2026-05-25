import aspose.pdf as ap
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_all_forms(input_file_name, page_num, output_file_name):
    """Remove all XForm resources from a specific page and save.

    Args:
        input_file_name (str): Path to the input PDF.
        page_num (int): 1-based page index to process.
        output_file_name (str): Path for the output PDF.
    Returns:
        None
    Example:
        >>> remove_all_forms("StudentInfoFormElectronic.pdf", 1, "output_remove_all_forms.pdf")
    Note:
        Operates on ``document.pages[page_num].resources.forms`` and clears all entries.
    """
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(output_file_name)


def remove_specified_form(input_file_name, page_num, output_file_name):
    """Remove specific forms from a page by type and subtype.

    Iterates XForm resources and deletes those matching ``it == "Typewriter"``
    and ``subtype == "Form"``.

    Args:
        input_file_name (str): Path to the input PDF.
        page_num (int): 1-based page index to process.
        output_file_name (str): Path for the output PDF.
    Returns:
        None
    Example:
        >>> remove_specified_form("StudentInfoFormElectronic.pdf", 1, "output_remove_specified_form.pdf")
    Note:
        Uses ``forms.get_form_name(form)`` to obtain the resource name for deletion.
    """
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(output_file_name)


def run_all_examples(data_dir=None, license_path=None):
    """Run acroforms deletion examples and report status.

    Args:
        data_dir (str, optional): Output directory override. Defaults to ``DATA_DIR``.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    page_num = 1
    examples = [
        ("remove_all_forms", lambda i, o: remove_all_forms(i, page_num, o)),
        ("remove_specified_form", lambda i, o: remove_specified_form(i, page_num, o)),
    ]

    input_file_name = path.join(input_dir, "StudentInfoFormElectronic.pdf")

    for name, func in examples:
        output_file_name = path.join(output_dir, f"{name}_out.pdf")
        try:
            func(input_file_name, output_file_name)
            print(f"✅ {name} completed. Output: {output_file_name}")
        except Exception as e:
            print(f"❌ {name} failed: {e}")

    print(f"\nAll Acroforms delete examples finished. Check output in {output_dir}")


if __name__ == "__main__":
    run_all_examples()
