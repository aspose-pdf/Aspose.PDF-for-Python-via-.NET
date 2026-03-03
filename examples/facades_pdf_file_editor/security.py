# Security
#├─ Encrypt
#└─ Decrypt

from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Encrypt
def encrypt_pdf_file():
    set_license()
    data_dir = initialize_data_dir()

    # Open document
    pdf_document = ap.Document(data_dir + "input.pdf")

    # Encrypt document
    pdf_document.encrypt("owner_password", "user_password", ap.PermissionsFlags.PrintDocument, ap.EncryptionAlgorithm.RC4x128)

    # Save output
    pdf_document.save(data_dir + "output_encrypted.pdf")

# Decrypt
def decrypt_pdf_file():
    set_license()
    data_dir = initialize_data_dir()

    # Open document
    pdf_document = ap.Document(data_dir + "output_encrypted.pdf", "user_password")

    # Decrypt document
    pdf_document.decrypt("owner_password")

    # Save output
    pdf_document.save(data_dir + "output_decrypted.pdf")

def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF security examples and report status .

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    examples = [
        ("Encrypt PDF", encrypt_pdf_file),
        ("Decrypt PDF", decrypt_pdf_file)
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{func.__name__}_in.pdf")
            func(input_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll PDF security examples finished.")


if __name__ == "__main__":
    run_all_examples()            