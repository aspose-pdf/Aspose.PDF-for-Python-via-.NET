from facades import PDFDocument, PDFSignature
from config import set_license, initialize_data_dir
from os import name, name, path

def remove_signature(input_file_name, output_file_name):
    # Load PDF document
    pdf_document = PDFDocument(input_file_name)

    # Create PDF signature object
    pdf_signature = PDFSignature()

    # Remove signature from PDF
    pdf_signature.remove_signature(pdf_document)

    # Save updated PDF document
    pdf_document.save(output_file_name)
    print(f"Signature removed and saved to: {output_file_name}")

def remove_signature_with_field_cleanup(input_file_name, output_file_name):
    # Load PDF document
    pdf_document = PDFDocument(input_file_name)

    # Create PDF signature object
    pdf_signature = PDFSignature()

    # Remove signature with field cleanup
    pdf_signature.remove_signature_with_field_cleanup(pdf_document)

    # Save updated PDF document
    pdf_document.save(output_file_name)
    print(f"Signature removed with field cleanup and saved to: {output_file_name}")

def run_all_examples(data_dir=None, license_path=None):
    """Run all signature management examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Remove Signature from PDF", remove_signature),
        ("Remove Signature with Field Cleanup", remove_signature_with_field_cleanup)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "input.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll signature management examples finished.")

if __name__ == "__main__":
    run_all_examples()     
