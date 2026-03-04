from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as ap_pydrawing
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def decorate_field(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)
    form_editor.facade = pdf_facades.FormFieldFacade()
    form_editor.facade.background_color = ap_pydrawing.Color.red
    form_editor.facade.text_color = ap_pydrawing.Color.blue
    form_editor.facade.border_color = ap_pydrawing.Color.green
    form_editor.facade.alignment = pdf_facades.FormFieldFacade.ALIGN_CENTER
    form_editor.decorate_field("First Name")

    # Save updated document
    form_editor.save(outfile)


def set_field_alignment(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field alignment to center
    if (form_editor.set_field_alignment(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_CENTER
    )):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception("Failed to set field alignment. Field may not support alignment.")


def set_field_alignment_vertical(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field vertical alignment to top
    if form_editor.set_field_alignment_v(
        "First Name", pdf_facades.FormFieldFacade.ALIGN_BOTTOM
    ):
        # Save updated document
        form_editor.save(outfile)
    else:
        raise Exception("Failed to set field vertical alignment. Field may not support vertical alignment.")

def set_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field appearance to invisible
    if not form_editor.set_field_appearance("First Name", ap.annotations.AnnotationFlags.INVISIBLE):
        raise Exception("Failed to set field appearance. Field may not support appearance flags.")

    # Save updated document
    form_editor.save(outfile)


def set_field_attribute(infile, outfile):
    # # Open document
    # doc = ap.Document(infile)

    # # Create FormEditor object
    # form_editor = pdf_facades.FormEditor(doc)

    # # Set field attribute to "ReadOnly"
    # if not form_editor.set_field_attribute("Country",  pdf_facades.PropertyFlags.READ_ONLY):
    #     raise Exception("Failed to set field attribute. Field may not support specified attribute.")
    
    # Save updated document
    # form_editor.save(outfile)
    pass


def set_field_comb_number(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field comb number to 5
    form_editor.set_field_comb_number("PIN", 5)
    
    # Save updated document
    form_editor.save(outfile)


def set_field_limit(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field limit to 10
    if not form_editor.set_field_limit("Last Name", 10):
        raise Exception("Failed to set field limit. Field may not support specified limit.")
    
    # Save updated document
    form_editor.save(outfile)


def get_field_appearance(infile, outfile):
    # Open document
    doc = ap.Document(infile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Get field appearance
    appearance = form_editor.get_field_appearance("Last Name")
    print("Field Appearance: " + str(appearance))


def run_all_examples(data_dir=None, license_path=None):
    """

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Decorate Field", decorate_field),
        ("Set Field Alignment", set_field_alignment),
        ("Set Field Alignment Vertical", set_field_alignment_vertical),
        ("Set Field Appearance", set_field_appearance),
        ("Set Field Attribute", set_field_attribute),
        ("Set Field Comb Number", set_field_comb_number),
        ("Set Field Limit", set_field_limit),
        ("Get Field Appearance", get_field_appearance),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}.pdf")
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Modifying Form Fields examples finished.")


if __name__ == "__main__":
    run_all_examples()
