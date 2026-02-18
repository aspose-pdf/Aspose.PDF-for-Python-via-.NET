import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def form_fields(infile, outfile):
    # Load the input PDF form
    form = pdf_facades.Form(infile)

    # Get all field names
    all_fields = form.field_names

    with open(outfile, "w") as f:
        for field_name in all_fields:
            print(field_name)
            f.write(field_name + "\n")


def flatten_single_fields(infile, outfile):
    # Load the input PDF form
    pdf_form = pdf_facades.Form(infile)

    pdf_form.flatten_field("Country")
    pdf_form.save(outfile)


def flatten_all_fields(infile, outfile):
    # Load the input PDF form
    pdf_form = pdf_facades.Form(infile)

    pdf_form.flatten_all_fields()
    pdf_form.save(outfile)


def fill_single_field(infile, outfile):
    # Load the input PDF form
    pdf_form = pdf_facades.Form(infile)

    pdf_form.fill_field("Country", "India")
    pdf_form.save(outfile)


def form_fields_old(infile1, infile2, outfile):

    # Load the input PDF form
    form = pdf_facades.Form(infile1)

    # Get all field names
    all_fields = form.FieldNames

    # Create an array to hold field location rectangles
    boxes = [None] * len(all_fields)

    for i, field_name in enumerate(all_fields):
        # Get appearance attributes of each field
        field_facade = form.get_field_facade(field_name)
        # Store the field's location rectangle
        boxes[i] = field_facade.Box

    # Open another PDF document
    document = ap.Document(infile2)

    # Create FormEditor to add new fields
    editor = pdf_facades.FormEditor(document)

    for i, field_name in enumerate(all_fields):
        # Add a text field beneath each existing form field
        editor.add_field(
            pdf_facades.FieldType.Text,
            f"TextField{i}",
            field_name,
            1,
            boxes[i].left,
            boxes[i].top,
            boxes[i].left + 50,
            boxes[i].left + 10,
        )

    # Save updated PDF
    editor.save(outfile)

    print("Form fields identified and new text fields added successfully.")


def run_all_examples(data_dir=None, license_path=None):
    """Run text adding examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
        Returns:
            None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Identify Form Fields", form_fields, "field_list.txt"),
        ("Flatten field", flatten_single_fields, "flatten_field.pdf"),
        ("Flatten all fields", flatten_all_fields, "flatten_all_fields.pdf"),
        ("Fill single field", fill_single_field, "fill_single_fields.pdf"),
    ]

    for name, func, out_file in examples:
        try:
            input_file_name = path.join(input_dir, "sample_form.pdf")
            output_file_name = path.join(output_dir, out_file)
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name} completed.")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")

    print(f"\nAll text adding examples finished. Check output in {output_dir}")


# Main execution
if __name__ == "__main__":
    run_all_examples()
