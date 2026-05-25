import aspose.pdf as ap
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import initialize_data_dir, set_license


def convert_dynamic_xfa_to_acroform(infile: str, outfile: str):
    """Convert dynamic XFA form to standard AcroForm."""
    with ap.Document(infile) as document:
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)


def convert_xfa_form_with_ignore_needs_rendering(infile: str, outfile: str):
    """Convert XFA form ignoring needs rendering flag."""
    with ap.Document(infile) as document:
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run XFAForms examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Convert Dynamic XFA to Acroform", convert_dynamic_xfa_to_acroform),
        (
            "Convert XFA form with ignore needs_rendering",
            convert_xfa_form_with_ignore_needs_rendering,
        ),
    ]

    for name, func in examples:
        try:
            input_file = path.join(input_dir, "DynamicXFAToAcroForm.pdf")
            output_file = path.join(output_dir, f"{name}_out.pdf")

            func(input_file, output_file)
            print(f"✅ Success: {name} completed.")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")

    print(f"\nAll XFAForms conversion examples finished. Check output in {output_dir}")


if __name__ == "__main__":
    run_all_examples()
