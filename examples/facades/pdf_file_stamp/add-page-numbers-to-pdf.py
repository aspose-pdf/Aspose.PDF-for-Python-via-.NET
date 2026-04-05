import aspose.pdf.facades as pdf_facades

from examples.config import initialize_data_dir, set_license

def add_page_numbers_default(infile, outfile):
    pdf_editor = pdf_facades.PdfFileStamp()
    try:
        pdf_editor.bind_pdf(infile)
        pdf_editor.add_page_number("Page #")
        pdf_editor.save(outfile)
    finally:
        pdf_editor.close()

def add_page_numbers_custom_position(infile, outfile):
    pdf_editor = pdf_facades.PdfFileStamp()
    try:
        pdf_editor.bind_pdf(infile)
        pdf_editor.add_page_number("Page #", 300, 20)
        pdf_editor.save(outfile)
    finally:
        pdf_editor.close()

def add_page_numbers_with_margins(infile, outfile):
    pdf_editor = pdf_facades.PdfFileStamp()
    try:
        pdf_editor.bind_pdf(infile)
        pdf_editor.add_page_number("Page #", 10, 10, 10)
        pdf_editor.save(outfile)
    finally:
        pdf_editor.close()

def run_all_examples(data_dir=None, license_path=None):
    """Run all page number examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add Page Numbers with Default Position", add_page_numbers_default),
        ("Add Page Numbers with Custom Position", add_page_numbers_custom_position),
        ("Add Page Numbers with Margins", add_page_numbers_with_margins),
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
