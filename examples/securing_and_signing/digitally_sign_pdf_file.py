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
                path.join(input_dir, "ecdsa_cert.pfx"),
                "12345",
            ),
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
