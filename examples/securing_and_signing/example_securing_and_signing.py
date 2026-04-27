import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import initialize_data_dir, set_license


def sign_document(infile: str, outfile: str, pfxfile: str) -> None:
    """Sign a PDF document with a PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, "12345")
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)


def sign_document_PKCS7_detached(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document with a detached PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)


def verify(infile: str) -> None:
    """Verify all digital signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")


def verify_with_public_key_certificate1(certificate: str, infile: str) -> None:
    """Verify a signature with a public key certificate file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        with open(certificate, "rb") as file_stream:
            certificate_bytes = file_stream.read()
        print(file_sign.verify_signature(signature_names[0], certificate_bytes))


def verify_with_public_key_certificate_from_signature(infile: str) -> None:
    """Verify a signature with the certificate extracted from the file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        certificate = []
        if file_sign.try_extract_certificate(signature_names[0], certificate):
            print(file_sign.verify_signature(signature_names[0], certificate[0]))
        else:
            print(False)


def verify_signature_with_certificate_check(infile: str) -> None:
    """Verify signatures with certificate-chain validation enabled."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                options = ap.security.ValidationOptions()
                options.validation_mode = ap.security.ValidationMode.STRICT
                options.validation_method = ap.security.ValidationMethod.AUTO
                options.check_certificate_chain = True
                options.request_timeout = 20000
                validation_result = []
                verified = signature.verify_signature(
                    signature_name,
                    options,
                    validation_result,
                )
                print(f"Certificate validation result: {validation_result[0].status}")
                print(f"Is verified: {verified}")


def sign_with_time_stamp_server(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document and apply a timestamp from an external server."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, password)
            pkcs.timestamp_settings = ap.TimestampSettings(
                "https://freetsa.org/tsr",
                "",
                ap.DigestHashAlgorithm.SHA256,
            )
            rect = drawing.Rectangle(100, 100, 200, 100)
            signature.sign(
                1, "Signature Reason", "Contact", "Location", True, rect, pkcs
            )
            signature.save(outfile)


def verify_ecdsa(infile: str) -> None:
    """Verify ECDSA signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            if not signature.contains_signature():
                raise Exception("Not contains signature")

            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")


def sign_ecdsa(infile: str, outfile: str, pfxfile: str, password: str) -> None:
    """Sign a PDF document with an ECDSA signature."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)


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


# endregion


# region Extract Image and Signature Information
def extract_images_from_signature_field(infile: str, outfile: str) -> None:
    """Extract the image stored in a signature field."""
    with ap.Document(infile) as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            image_stream = field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            image.save(outfile, drawing.imaging.ImageFormat.jpeg)


def extract_certificate(infile: str, outfile: str) -> None:
    """Extract a certificate from a signature field and save it to disk."""
    with ap.Document(infile, password="owner") as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            certificate_stream = field.extract_certificate()
            if certificate_stream is None:
                continue

            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                certificate_stream.read(bytes_data, 0, len(bytes_data))
                with open(outfile, "wb") as file_stream:
                    file_stream.write(bytes_data)
                return


def extract_certificate_try_extract_certificate_method(infile: str) -> None:
    """Extract certificates with the try_extract_certificate facade method."""
    with ap.Document(infile, password="owner") as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                certificate = []
                if signature.try_extract_certificate(signature_name, certificate):
                    print("The certificate extraction succeeded")


def get_signatures_info(infile: str) -> None:
    """Print information about all signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_info in signature.get_signatures_info():
                print(signature_info.DIGEST_HASH_ALGORITHM)
                print(signature_info.ALGORITHM_TYPE)
                print(signature_info.CRYPTOGRAPHIC_STANDARD)
                print(signature_info.signature_name)


def check(infile: str) -> None:
    """Check whether a PDF contains compromised signatures."""
    with ap.Document(infile) as document:
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        if detector.check(result):
            print("No signature compromise detected")
            return

        if result[0].has_compromised_signatures:
            print(
                f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}"
            )
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        print(result[0].signatures_coverage)


def get_signature_info_using_signature_field(infile: str, outfile: str) -> None:
    """Create a signature field and sign it with an external certificate."""
    with open(infile, "rb+") as file_stream:
        document = ap.Document(file_stream)
        signature_field = ap.forms.SignatureField(
            document.pages[1],
            ap.Rectangle(100, 400, 10, 10, True),
        )
        selected_certificate = get_local_certificate()
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"
        signature_field.partial_name = "sig1"
        document.form.add(signature_field, 1)
        signature_field.sign(external_signature)
        document.save(outfile)


def get_local_certificate():
    """Placeholder for retrieving a local certificate."""
    return None


def verify_external_signature(infile: str) -> None:
    """Verify an external signature in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            for signature_name in pdf_signature.get_signature_names(True):
                if not pdf_signature.verify_signature(signature_name):
                    raise Exception("Not verified")


def sign_with_smart_card(infile: str, outfile: str, pngfile: str) -> None:
    """Sign a PDF document using a smart-card certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            pdf_signature.bind_pdf(document)
            external_signature = ap.forms.ExternalSignature(get_local_certificate())
            pdf_signature.signature_appearance = pngfile
            pdf_signature.sign(
                1,
                "Reason",
                "Contact",
                "Location",
                True,
                drawing.Rectangle(100, 100, 200, 200),
                external_signature,
            )
            pdf_signature.save(outfile)


# endregion
def run_all_examples(data_dir=None, license_path=None) -> None:
    """Run security and signing examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "Sign PDF with PKCS#7",
            sign_document,
            (
                path.join(input_dir, "DigitallySign.pdf"),
                path.join(output_dir, "DigitallySign_out.pdf"),
                path.join(input_dir, "rsa_cert.pfx"),
            ),
        ),
        (
            "Sign PDF with detached PKCS#7",
            sign_document_PKCS7_detached,
            (
                path.join(input_dir, "DigitallySign.pdf"),
                path.join(output_dir, "DigitallySignDetached_out.pdf"),
                path.join(input_dir, "rsa_cert.pfx"),
                "12345",
            ),
        ),
        ("Verify RSA signature", verify, (path.join(input_dir, "signed_rsa.pdf"),)),
        (
            "Verify with public certificate",
            verify_with_public_key_certificate1,
            (
                path.join(input_dir, "pub_sec.crt"),
                path.join(output_dir, "DigitallySign_out.pdf"),
            ),
        ),
        (
            "Verify with extracted certificate",
            verify_with_public_key_certificate_from_signature,
            (path.join(output_dir, "DigitallySign_out.pdf"),),
        ),
        (
            "Sign with timestamp server",
            sign_with_time_stamp_server,
            (
                path.join(input_dir, "SimpleResume.pdf"),
                path.join(output_dir, "DigitallySignWithTimeStamp_out.pdf"),
                path.join(input_dir, "rsa_cert.pfx"),
                "12345",
            ),
        ),
        (
            "Verify ECDSA signature",
            verify_ecdsa,
            (path.join(input_dir, "signed_ecdsa.pdf"),),
        ),
        (
            "Sign with ECDSA",
            sign_ecdsa,
            (
                path.join(input_dir, "input.pdf"),
                path.join(output_dir, "SignEcdsa_out.pdf"),
                path.join(input_dir, "rsa_cert.pfx"),
                "12345",
            ),
        ),
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
        ),
        (
            "Extract image from signature field",
            extract_images_from_signature_field,
            (
                path.join(input_dir, "ExtractingImage.pdf"),
                path.join(output_dir, "output_out.jpg"),
            ),
        ),
        (
            "Extract certificate",
            extract_certificate,
            (
                path.join(input_dir, "ExtractSignatureInfo.pdf"),
                path.join(output_dir, "input.cer"),
            ),
        ),
        (
            "Extract certificate with facade method",
            extract_certificate_try_extract_certificate_method,
            (path.join(input_dir, "ExtractSignatureInfo.pdf"),),
        ),
        (
            "Get signatures info",
            get_signatures_info,
            (path.join(input_dir, "signed_rsa.pdf"),),
        ),
        (
            "Check compromised signatures",
            check,
            (path.join(input_dir, "CheckingSignatures.pdf"),),
        ),
        (
            "Create signature field",
            get_signature_info_using_signature_field,
            (
                path.join(input_dir, "blank.pdf"),
                path.join(output_dir, "externalSignature1_out.pdf"),
            ),
        ),
        (
            "Verify external signature",
            verify_external_signature,
            (path.join(input_dir, "externalSignature1.pdf"),),
        ),
        (
            "Sign with smart card",
            sign_with_smart_card,
            (
                path.join(input_dir, "blank.pdf"),
                path.join(output_dir, "externalSignature2_out.pdf"),
                path.join(input_dir, "demo.png"),
            ),
        ),
    ]

    for name, func, args in examples:
        try:
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as exc:
            print(f"❌ Failed: {name} - {exc}")


if __name__ == "__main__":
    run_all_examples()
