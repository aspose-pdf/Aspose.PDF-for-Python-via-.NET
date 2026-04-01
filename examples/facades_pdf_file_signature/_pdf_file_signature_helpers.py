import os
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd


DEFAULT_CERTIFICATE_FILENAME = "certificate.pfx"
DEFAULT_CERTIFICATE_PASSWORD = "password"
DEFAULT_INPUT_PDF = "sample.pdf"
DEFAULT_SIGNED_PDF = "signed.pdf"
DEFAULT_CERTIFIED_PDF = "certified.pdf"
DEFAULT_SIGNATURE_NAME = "Signature1"


def create_pdf_file_signature(infile):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(infile)
    return pdf_signature


def create_signature_rectangle():
    return apd.Rectangle(10, 10, 200, 60)


def get_certificate_path(certificate_path=None):
    if certificate_path:
        return certificate_path
    return path.join(path.dirname(__file__), DEFAULT_CERTIFICATE_FILENAME)


def ensure_certificate_file(certificate_path=None):
    resolved_path = get_certificate_path(certificate_path)
    if not path.exists(resolved_path):
        raise FileNotFoundError(
            "Certificate file not found. "
            f"Place '{DEFAULT_CERTIFICATE_FILENAME}' next to this example or pass a custom path: {resolved_path}"
        )
    return resolved_path


def configure_signature_certificate(pdf_signature, certificate_path=None, certificate_password=DEFAULT_CERTIFICATE_PASSWORD):
    resolved_path = ensure_certificate_file(certificate_path)
    pdf_signature.set_certificate(resolved_path, certificate_password)
    return resolved_path


def create_pkcs7_signature(
    certificate_path=None,
    certificate_password=DEFAULT_CERTIFICATE_PASSWORD,
    reason="Document approval",
    contact_info="qa@example.com",
    location="New York, USA",
    authority="Aspose.PDF Example",
):
    resolved_path = ensure_certificate_file(certificate_path)
    signature = ap.forms.PKCS7(resolved_path, certificate_password)
    signature.reason = reason
    signature.contact_info = contact_info
    signature.location = location
    signature.authority = authority
    return signature


def create_custom_signature_appearance():
    appearance = ap.forms.SignatureCustomAppearance()
    appearance.font_family_name = "Arial"
    appearance.font_size = 10
    appearance.show_contact_info = True
    appearance.show_location = True
    appearance.show_reason = True
    return appearance


def create_doc_mdp_signature(
    access_permissions,
    certificate_path=None,
    certificate_password=DEFAULT_CERTIFICATE_PASSWORD,
    reason="Document certification",
    contact_info="security@example.com",
    location="New York, USA",
):
    signature = create_pkcs7_signature(
        certificate_path=certificate_path,
        certificate_password=certificate_password,
        reason=reason,
        contact_info=contact_info,
        location=location,
        authority="Aspose.PDF Certification Example",
    )
    return ap.forms.DocMDPSignature(signature, access_permissions)


def list_signature_names(pdf_signature, only_active=False):
    names = pdf_signature.get_sign_names(only_active)
    if names is None:
        return []
    return [str(name) for name in names]


def require_signature_name(pdf_signature, sign_name=None, only_active=False):
    if sign_name:
        return sign_name

    names = list_signature_names(pdf_signature, only_active=only_active)
    if not names:
        raise ValueError("No signatures were found in the input PDF.")
    return names[0]


def write_stream_data(stream_data, outfile):
    if stream_data is None:
        raise ValueError("The API returned no stream data to write.")

    if isinstance(stream_data, (bytes, bytearray)):
        payload = bytes(stream_data)
    elif hasattr(stream_data, "to_array"):
        payload = bytes(stream_data.to_array())
    elif hasattr(stream_data, "read"):
        try:
            payload = stream_data.read()
        except TypeError:
            payload = bytes(stream_data)
    else:
        payload = bytes(stream_data)

    output_dir = path.dirname(outfile)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(outfile, "wb") as output_file:
        output_file.write(payload)
