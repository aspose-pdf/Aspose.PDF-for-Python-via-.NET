import aspose.pdf.facades as pdf_facades
import sys
from os import path

from examples.config import initialize_data_dir, set_license

def add_image_stamp(infile, image_file, outfile):
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: add_image_stamp.py <input_pdf> <image_file> <output_pdf>")
        sys.exit(1)

    infile = sys.argv[1]
    image_file = sys.argv[2]
    outfile = sys.argv[3]

    add_image_stamp(infile, image_file, outfile)
    print(f"Image stamp added successfully to {outfile}")

def run_all_examples(data_dir=None, license_path=None):
    """Run all stamp examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add Image Stamp", add_image_stamp),
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
