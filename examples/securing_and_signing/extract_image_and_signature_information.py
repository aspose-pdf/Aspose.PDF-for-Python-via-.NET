import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import initialize_data_dir, set_license


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

def run_all_examples(data_dir=None, license_path=None) -> None:
    """Run security and signing examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
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
            "Check signatures for compromise",
            check,
            (path.join(input_dir, "signed_rsa.pdf"),),
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

