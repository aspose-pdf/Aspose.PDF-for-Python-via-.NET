import sys
import os
import aspose.pdf as ap

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def attach_invoice_zugferd_format(infile, invoice, outfile):
    """
    Attach Factur-X/ZUGFeRD invoice XML to PDF and convert to PDF/A-3A format.

    Args:
        infile (str): Input PDF filename
        invoice (str): Invoice XML filename (Factur-X/ZUGFeRD compliant)
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        attach_invoice_zugferd_format("input.pdf", "factur-x.xml", "output.pdf")

    Note:
        Embeds invoice XML as alternative file conforming to ZUGFeRD standard.
        Converts PDF to PDF/A-3A format to ensure long-term archival compliance.
    """
    document = ap.Document(infile)

    # Create a FileSpecification object for the XML file that contains the invoice metadata
    description = "Invoice metadata conforming to ZUGFeRD standard"
    file_specification = ap.FileSpecification(invoice, description)

    # Set the MIME type and the AFRelationship properties of the embedded file
    file_specification.mime_type = "text/xml"
    file_specification.af_relationship = ap.AFRelationship.ALTERNATIVE

    # Add the embedded file to the PDF document's embedded files collection
    document.embedded_files.add("factur", file_specification)

    # Convert the PDF document to the PDF/A-3A format
    log_path = outfile.replace(".pdf", "_log.xml")
    document.convert(log_path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run ZUGFeRD attachment examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Attach invoice ZUGFeRD format", attach_invoice_zugferd_format),
    ]

    for name, func in examples:
        input_file_name = os.path.join(input_dir, "ZUGFeRD-test.pdf")
        invoice_file_name = os.path.join(input_dir, "factur-x.xml")
        output_file_name = os.path.join(output_dir, "ZUGFeRD-result.pdf")
        try:
            func(input_file_name, invoice_file_name, output_file_name)
            print(f"✅ Success: {name} completed.")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")

    print(f"\nAll ZUGFeRD adding examples finished. Check output in {output_dir}")


# Main execution
if __name__ == "__main__":
    run_all_examples()
