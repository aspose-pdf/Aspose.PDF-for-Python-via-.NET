from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# DecorateField
def main():
    set_license()
    data_dir = initialize_data_dir()

    # Open document
    doc = ap.Document(data_dir + "input.pdf")

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Decorate field with red color
    form_editor.decorate_field("text1", ap.Color.red)

    # Save updated document
    form_editor.save(data_dir + "output.pdf")

# SetFieldAlignment  
def set_field_alignment():
    set_license()
    data_dir = initialize_data_dir()

    # Open document
    doc = ap.Document(data_dir + "input.pdf")

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field alignment to center
    form_editor.set_field_alignment("text1", ap.HorizontalAlignment.center)

    # Save updated document
    form_editor.save(data_dir + "output.pdf")  

# SetFieldAlignmentVertical
def set_field_alignment_vertical():
    set_license()
    data_dir = initialize_data_dir()

    # Open document
    doc = ap.Document(data_dir + "input.pdf")

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field vertical alignment to center
    form_editor.set_field_alignment_vertical("text1", ap.VerticalAlignment.center)

    # Save updated document
    form_editor.save(data_dir + "output.pdf")

# SetFieldAppearance
def set_field_appearance():
    set_license()
    data_dir = initialize_data_dir()

    # Open document
    doc = ap.Document(data_dir + "input.pdf")

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field appearance to "Chalk"
    form_editor.set_field_appearance("text1", "Chalk")

    # Save updated document
    form_editor.save(data_dir + "output.pdf")        

# SetFieldAttribute
def set_field_attribute():
    set_license()
    data_dir = initialize_data_dir()

    # Open document
    doc = ap.Document(data_dir + "input.pdf")

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field attribute to "Multiline"
    form_editor.set_field_attribute("text1", ap.Forms.FieldFlags.multiline)

    # Save updated document
    form_editor.save(data_dir + "output.pdf") 

# SetFieldCombNumber
def set_field_comb_number():
    set_license()
    data_dir = initialize_data_dir()

    # Open document
    doc = ap.Document(data_dir + "input.pdf")

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field comb number to 5
    form_editor.set_field_comb_number("text1", 5)

    # Save updated document
    form_editor.save(data_dir + "output.pdf") 

# SetFieldLimit
def set_field_limit():
    set_license()
    data_dir = initialize_data_dir()

    # Open document
    doc = ap.Document(data_dir + "input.pdf")

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Set field limit to 10
    form_editor.set_field_limit("text1", 10)

    # Save updated document
    form_editor.save(data_dir + "output.pdf") 

# GetFieldAppearance
def get_field_appearance():
    set_license()
    data_dir = initialize_data_dir()

    # Open document
    doc = ap.Document(data_dir + "input.pdf")

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor(doc)

    # Get field appearance
    appearance = form_editor.get_field_appearance("text1")
    print("Field Appearance: " + appearance)             

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
        ("DecorateField", main, "output_decorate_field.pdf"),
        ("SetFieldAlignment", set_field_alignment, "output_set_field_alignment.pdf"),
        ("SetFieldAlignmentVertical", set_field_alignment_vertical, "output_set_field_alignment_vertical.pdf"),
        ("SetFieldAppearance", set_field_appearance, "output_set_field_appearance.pdf"),
        ("SetFieldAttribute", set_field_attribute, "output_set_field_attribute.pdf"),
        ("SetFieldCombNumber", set_field_comb_number, "output_set_field_comb_number.pdf"),
        ("SetFieldLimit", set_field_limit, "output_set_field_limit.pdf"),
        ("GetFieldAppearance", get_field_appearance, "output_get_field_appearance.txt")
    ]

    for name, func, data_file_name in examples:
        try:
            input_file_name = path.join(input_dir, "input.pdf")
            output_file_name = path.join(output_dir, data_file_name)
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Modifying Form Fields examples finished.")


if __name__ == "__main__":
    run_all_examples()