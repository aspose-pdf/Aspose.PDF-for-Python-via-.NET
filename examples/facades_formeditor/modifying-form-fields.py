from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_list_item(infile,outfile):
    # Open document
    doc = ap.Document(infile)
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Add list item to list box field
    form_editor.add_list_item(doc, "list_box", "item 4")
    # Save updated document
    doc.save(outfile)

def del_list_item(infile,outfile):
    # Open document
    doc = ap.Document(infile)
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Delete list item from list box field
    form_editor.del_list_item(doc, "list_box", "item 2")
    # Save updated document
    doc.save(outfile)

def move_field(infile,outfile): 
    # Open document
    doc = ap.Document(infile)
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Move field to new page
    form_editor.move_field(doc, "text_box", 2)
    # Save updated document
    doc.save(outfile)

def remove_field(infile,outfile):
    # Open document
    doc = ap.Document(infile)
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Remove field from document
    form_editor.remove_field(doc, "text_box")
    # Save updated document
    doc.save(outfile)

def rename_field(infile,outfile):
    # Open document
    doc = ap.Document(infile)
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Rename field in document
    form_editor.rename_field(doc, "text_box", "new_text_box")
    # Save updated document
    doc.save(outfile)

def single2multiple(infile,outfile):
    # Open document
    doc = ap.Document(infile)
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Convert single field to multiple fields
    form_editor.single2multiple(doc, "text_box", 3)
    # Save updated document
    doc.save(outfile)

def copy_inner_field(infile, outfile):
    # Open document
    doc = ap.Document(infile)
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Copy inner field to new page
    form_editor.copy_inner_field(doc, "text_box", 2)
    # Save updated document
    doc.save(outfile)

def copy_outer_field(infile, outfile):
    # Open document
    doc = ap.Document(infile)
    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Copy outer field to new page
    form_editor.copy_outer_field(doc, "text_box", 2)
    # Save updated document
    doc.save(outfile)    

def run_all_examples(data_dir=None, license_path=None):
    """Run all import/export form data examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add List Item", add_list_item, "add_list_item.pdf"),
        ("Delete List Item", del_list_item, "del_list_item.pdf"),
        ("Move Field", move_field, "move_field.pdf"),
        ("Remove Field", remove_field, "remove_field.pdf"),
        ("Rename Field", rename_field, "rename_field.pdf"),
        ("Single to Multiple", single2multiple, "single2multiple.pdf"),
        ("Copy Inner Field", copy_inner_field, "copy_inner_field.pdf"),
        ("Copy Outer Field", copy_outer_field, "copy_outer_field.pdf")
    ]

    for name, func, data_file_name in examples:
        try:
            input_file_name = path.join(input_dir, "sample_form.pdf")
            output_file_name = path.join(output_dir, data_file_name)
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Modifying Form Fields examples finished.")


if __name__ == "__main__":
    run_all_examples()