import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import initialize_data_dir, set_license

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

def run_all_examples(data_dir=None, license_path=None) -> None:
    """Run security and signing examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
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
        (
            "Get signature info using signature field",
            get_signature_info_using_signature_field,
            (
                path.join(input_dir, "blank.pdf"),
                path.join(output_dir, "ExtractSignatureInfo_out.pdf"),
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


