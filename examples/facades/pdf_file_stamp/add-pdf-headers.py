import aspose.pdf.facades as pdf_facades

from examples.config import initialize_data_dir, set_license

from examples.config import initialize_data_dir

def add_text_header(infile, outfile):
    pdf_editor = pdf_facades.PdfFileStamp()
    try:
        pdf_editor.bind_pdf(infile)
        pdf_editor.add_header("Sample Header")
        pdf_editor.save(outfile)
    finally:
        pdf_editor.close()

import aspose.pdf.facades as pdf_facades

def add_image_header(infile, image_file, outfile):
    pdf_editor = pdf_facades.PdfFileStamp()
    try:
        pdf_editor.bind_pdf(infile)
        pdf_editor.add_header(image_file)
        pdf_editor.save(outfile)
    finally:
        pdf_editor.close()

import aspose.pdf.facades as pdf_facades

def add_header_with_margins(infile, outfile):
    pdf_editor = pdf_facades.PdfFileStamp()
    try:
        pdf_editor.bind_pdf(infile)
        pdf_editor.add_header("Custom Header", 20, 20, 20)
        pdf_editor.save(outfile)
    finally:
        pdf_editor.close()   

def run_all_examples(data_dir=None, license_path=None):
    """Run all header examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add Text Header", add_text_header),
        ("Add Image Header", add_image_header),
        ("Add Header with Margins", add_header_with_margins),
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