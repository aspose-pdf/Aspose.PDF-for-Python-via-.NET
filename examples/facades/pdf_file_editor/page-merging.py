import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

import sys
from os import path

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)
from config import set_license, initialize_data_dir

def concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge[0], files_to_merge[1], output_file)

def concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.concatenate(files_to_merge, output_file)


def try_concatenate_two_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(files_to_merge[0], files_to_merge[1], output_file):
        print("Concatenation failed for the provided files.")
    
def try_concatenate_pdf_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    if not pdf_editor.try_concatenate(files_to_merge, output_file):
        print("Concatenation failed for the provided files.")

def concatenate_large_number_files(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.use_disk_buffer = True  # Enable disk buffering for large files
    pdf_editor.concatenate(files_to_merge, output_file)

def concatenate_pdf_files_with_optimization(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.optimize_size = True  # Enable optimization for smaller output file size
    pdf_editor.concatenate(files_to_merge, output_file)

def concatenate_pdf_forms(files_to_merge, output_file):
    # Create a PdfFileEditor object
    pdf_editor = pdf_facades.PdfFileEditor()
    pdf_editor.unique_suffix = "_xy_%NUM%"  # Set a unique suffix to avoid form field name conflicts
    pdf_editor.concatenate(files_to_merge, output_file)


def run_all_examples(data_dir=None, license_path=None):
    """Run all page management examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Concatenate Two PDF Files", concatenate_two_files),
        ("Concatenate Multiple PDF Files", concatenate_pdf_files),
        ("Try Concatenate Two PDF Files", try_concatenate_two_files),
        ("Try Concatenate Multiple PDF Files", try_concatenate_pdf_files),
        ("Concatenate Large Number of PDF Files", concatenate_large_number_files),
        ("Concatenate PDF Files with Optimization", concatenate_pdf_files_with_optimization),
        ("Concatenate PDF Forms with Unique Suffix", concatenate_pdf_forms)
    ]

    input_files = ["merge_1.pdf", "merge_2.pdf", "merge_3.pdf"]  # Example input files
    form_files = ["form1.pdf", "form2.pdf"]  # Example form files for concatenation
    pdf_files_to_merge = [path.join(input_dir, file) for file in input_files]
    form_files_to_merge = [path.join(input_dir, file) for file in form_files]

    for name, func in examples:
        try:
            if "Form" in name:
                func(form_files_to_merge, path.join(output_dir, func.__name__ + ".pdf"))
            else:
                func(pdf_files_to_merge, path.join(output_dir, func.__name__ + ".pdf"))
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll page management examples finished.")


if __name__ == "__main__":
    run_all_examples()
