from facades import PDFDocument
from config import set_license, initialize_data_dir
from os import name, name, path

def remove_usage_rights(input_file_name, output_file_name):
    # Load PDF document
    pdf_document = PDFDocument(input_file_name)

    # Remove usage rights
    pdf_document.remove_usage_rights()

    # Save updated PDF document
    pdf_document.save(output_file_name)
    print(f"Usage rights removed and saved to: {output_file_name}")

def run_all_examples(data_dir=None, license_path=None):
    """Run all usage rights management examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Remove Usage Rights", remove_usage_rights)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "input.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll usage rights management examples finished.")


if __name__ == "__main__":
    run_all_examples()     