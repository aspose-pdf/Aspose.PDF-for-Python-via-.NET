import sys
from os import path

import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import initialize_data_dir, set_license


def extract_xfa_form_fields(infile):

    document = ap.Document(infile)
    # Get names of XFA form fields
    names = document.form.xfa.field_names

    # Get field position
    if len(names) > 0:
        name0=names[0]
        t = document.form.xfa.get_field_template(name0)
        print(t.attributes["x"].value)
        print(t.attributes["y"].value)


def run_all_examples(data_dir=None, license_path=None):
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Extract XFA form fields", extract_xfa_form_fields, "sample-xfa.pdf", None),
    ]

    for name, func, input_file, output_file in examples:
        try:
            args = [path.join(input_dir, input_file)]
            if output_file:
                args.append(path.join(output_dir, output_file))
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()