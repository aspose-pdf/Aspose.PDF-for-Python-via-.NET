import aspose.pdf as ap
import io
import json
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir



def extract_form_fields(infile):
    form = ap.facades.Form(infile)
    form_values = {}
    for formField in form.field_names:
        form_values[formField] = form.get_field(formField)

    print(form_values)


def extract_form_field_by_title(input_file_name, field_name):
    form = ap.facades.Form(input_file_name)
    form_value = form.get_field(field_name)

    print(form_value)


def extract_form_fields_JSON(infile, outfile):
    form = ap.facades.Form(infile)
    with io.FileIO(outfile, "w") as json_file:
        form.export_json(json_file, True)

def extract_form_fields_json_doc(infile, outfile):
    form = ap.facades.Form(infile)
    form_data = {}
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    json_string = json.dumps(form_data, indent=4)
    with open(outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)


def extract_data_to_xml(infile, outfile):
    form = ap.facades.Form()
    form.bind_pdf(infile)
    with io.FileIO(outfile, "w") as f:
        form.export_xml(f)


def extract_data_to_fdf(infile, outfile):
    form = ap.facades.Form()
    form.bind_pdf(infile)
    with io.FileIO(outfile, "w") as f:
        form.export_fdf(f)

def extract_data_to_xfdf(infile, outfile):
    form = ap.facades.Form()
    form.bind_pdf(infile)
    with io.FileIO(outfile, "w") as f:
        form.export_xfdf(f)


def run_all_examples(data_dir=None, license_path=None):
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Extract form fields", extract_form_fields, "sample-form.pdf", None),
        ("Extract form field by title", extract_form_field_by_title, "sample-form.pdf", "FieldName"),
        ("Extract form fields to JSON", extract_form_fields_JSON, "sample-form.pdf", "form_output.json"),
        ("Extract form fields to JSON (manual)", extract_form_fields_json_doc, "sample-form.pdf", "form_output_manual.json"),
        ("Extract data to XML", extract_data_to_xml, "sample-form.pdf", "form_output.xml"),
        ("Extract data to FDF", extract_data_to_fdf, "sample-form.pdf", "form_output.fdf"),
        ("Extract data to XFDF", extract_data_to_xfdf, "sample-form.pdf", "form_output.xfdf"),
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
