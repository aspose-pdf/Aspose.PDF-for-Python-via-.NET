from facades import PDFDocument, PDFSignature
from config import set_license, initialize_data_dir
from os import name, name, path

def get_signature_revision(input_file_name, output_file_name):
    # Load PDF document
    pdf_document = PDFDocument(input_file_name)

    # Create PDF signature object
    pdf_signature = PDFSignature()

    # Get signature revision
    signature_revision = pdf_signature.get_signature_revision(pdf_document)
    print(f"Signature Revision: {signature_revision}")

def get_total_document_revisions(input_file_name, output_file_name):
    # Load PDF document
    pdf_document = PDFDocument(input_file_name)

    # Create PDF signature object
    pdf_signature = PDFSignature()

    # Get total document revisions
    total_revisions = pdf_signature.get_total_document_revisions(pdf_document)
    print(f"Total Document Revisions: {total_revisions}")

def get_access_permissions(input_file_name, output_file_name):
    # Load PDF document
    pdf_document = PDFDocument(input_file_name)

    # Create PDF signature object
    pdf_signature = PDFSignature()

    # Get access permissions
    access_permissions = pdf_signature.get_access_permissions(pdf_document)
    print(f"Access Permissions: {access_permissions}")

def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF revision and permissions examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Get Signature Revision", get_signature_revision),
        ("Get Total Document Revisions", get_total_document_revisions),
        ("Get Access Permissions", get_access_permissions)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "input.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll PDF revision and permissions examples finished.")


if __name__ == "__main__":
    run_all_examples()  
    
