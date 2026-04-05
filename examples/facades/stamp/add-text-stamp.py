import aspose.pdf.facades as pdf_facades
import aspose.pdf as ap
import sys
from os import path

from config import initialize_data_dir, set_license

def add_text_stamp(infile, outfile):
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        formatted_text = ap.facades.FormattedText("CONFIDENTIAL")
        stamp.bind_logo(formatted_text)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()

def run_all_examples(data_dir=None, license_path=None):
    """Run all stamp examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add Text Stamp", add_text_stamp),
    ]

    for name, func in examples:
        try:
            func(path.join(input_dir, "sample.pdf"),
                 path.join(output_dir, f"{func.__name__}.pdf"))
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()        