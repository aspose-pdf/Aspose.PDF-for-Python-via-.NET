import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import initialize_data_dir, set_license


def set_privileges_on_existing_pdf_file(infile: str, outfile: str) -> None:
    """Set restricted privileges on an existing PDF document."""
    with ap.Document(infile) as document:
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        document_privilege.allow_screen_readers = True
        document.encrypt(
            "user",
            "owner",
            document_privilege,
            ap.CryptoAlgorithm.AESx128,
            False,
        )
        document.save(outfile)


def encrypt_pdf_file(infile: str, outfile: str) -> None:
    """Encrypt a PDF document with user and owner passwords."""
    with ap.Document(infile) as document:
        document.encrypt(
            "user",
            "owner",
            ap.Permissions.EXTRACT_CONTENT,
            ap.CryptoAlgorithm.AESx128,
        )
        document.save(outfile)


def decrypt_pdf_file(infile: str, outfile: str) -> None:
    """Decrypt a password-protected PDF document."""
    with ap.Document(infile, "password") as document:
        document.decrypt()
        document.save(outfile)


def pub_sec_encryption(
    crypto_algorithm,
    pub_cert: str,
    in_pfx: str,
    outfile: str,
) -> None:
    """Demonstrate public-key encryption and decryption."""
    pfx_password = "12345"

    with ap.Document() as document:
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("Hello World!"))

        with open(pub_cert, "rb") as file_stream:
            byte_content = file_stream.read()

        document.encrypt(
            ap.Permissions.PRINT_DOCUMENT,
            crypto_algorithm,
            [byte_content],
        )
        document.save(outfile)

    with ap.Document(
        outfile,
        ap.security.CertificateEncryptionOptions(pub_cert, in_pfx, pfx_password),
    ) as document:
        print(document.info.title)
        print(document.info.author)

        text_absorber = ap.text.TextAbsorber()
        document.pages[1].accept(text_absorber)
        print(text_absorber.text)

        document.decrypt()
        document.save(path.join(path.dirname(outfile), "pubsec_decrypted_out.pdf"))


def change_password(infile: str, outfile: str) -> None:
    """Change the passwords of a password-protected PDF document."""
    with ap.Document(infile, "owner") as document:
        document.change_passwords("owner", "newuser", "newowner")
        document.save(outfile)


def determine_correct_password_from_array(infile: str) -> None:
    """Try a list of passwords until the document opens successfully."""
    with ap.facades.PdfFileInfo() as pdf_file_info:
        pdf_file_info.bind_pdf(infile)
        print(f"File is password protected {pdf_file_info.is_encrypted}")

    passwords = ["test", "test1", "test2", "test3", "sample"]

    for password in passwords:
        try:
            with ap.Document(infile, password) as document:
                if len(document.pages) > 0:
                    print(f"Password = {password} is correct")
                    print(f"Number of pages in document = {len(document.pages)}")
                    break
        except Exception:
            print(f"Password = {password} is not correct")

def run_all_examples(data_dir=None, license_path=None) -> None:
    """Run security and signing examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "Set document privileges",
            set_privileges_on_existing_pdf_file,
            (
                path.join(input_dir, "input.pdf"),
                path.join(output_dir, "SetPrivileges_out.pdf"),
            ),
        ),
        (
            "Encrypt PDF",
            encrypt_pdf_file,
            (
                path.join(input_dir, "Encrypt.pdf"),
                path.join(output_dir, "Encrypt_out.pdf"),
            ),
        ),
        (
            "Decrypt PDF",
            decrypt_pdf_file,
            (
                path.join(input_dir, "Decrypt.pdf"),
                path.join(output_dir, "Decrypt_out.pdf"),
            ),
        ),
        (
            "Public-key encryption",
            pub_sec_encryption,
            (
                ap.CryptoAlgorithm.AESx128,
                path.join(input_dir, "pub_sec.crt"),
                path.join(input_dir, "pub_sec.pfx"),
                path.join(output_dir, "pubsec_encrypted_out.pdf"),
            ),
        ),
        (
            "Change PDF password",
            change_password,
            (
                path.join(input_dir, "ChangePassword.pdf"),
                path.join(output_dir, "ChangePassword_out.pdf"),
            ),
        ),
        (
            "Determine password from list",
            determine_correct_password_from_array,
            (path.join(input_dir, "IsPasswordProtected.pdf"),),
        )
    ]

    for name, func, args in examples:
        try:
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as exc:
            print(f"❌ Failed: {name} - {exc}")


if __name__ == "__main__":
    run_all_examples()
