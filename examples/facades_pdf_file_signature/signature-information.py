from importlib.resources import path

from PyPDF2 import PdfFileReader
from examples.config import initialize_data_dir, set_license
from examples.config import initialize_data_dir    
# Function to get signature information from a PDF file
def get_signature_information(pdf_file_path):
    # Open the PDF file
    with open(pdf_file_path, 'rb') as file:
        reader = PdfFileReader(file)
        
        # Check if the PDF has any signatures
        if reader.getNumPages() > 0:
            # Get the first page of the PDF
            page = reader.getPage(0)
            
            # Extract signature information
            signature_info = {
                "Signature Names": [],
                "Signer Details": [],
                "Signature Date and Time": [],
                "Signature Reason and Location": []
            }
            
            # Loop through the annotations to find signatures
            for annotation in page['/Annots']:
                if annotation['/Subtype'] == '/Widget' and annotation['/FT'] == '/Sig':
                    signature_info["Signature Names"].append(annotation['/T'])
                    signature_info["Signer Details"].append(annotation['/V']['/Name'])
                    signature_info["Signature Date and Time"].append(annotation['/V']['/M'])
                    signature_info["Signature Reason and Location"].append(annotation['/V']['/Reason'])
            
            return signature_info
        else:
            return "No signatures found in the PDF."

def run_all_examples(data_dir=None, license_path=None):
    """Run all certificate configuration examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Get Signature Information", get_signature_information),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "signed_document.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(input_file_name, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll signature information examples finished.")

if __name__ == "__main__":
    run_all_examples() 




