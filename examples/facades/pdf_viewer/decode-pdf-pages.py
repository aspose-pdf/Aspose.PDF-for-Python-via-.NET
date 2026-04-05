import aspose.pdf.facades as pdf_facades

from examples.config import initialize_data_dir, set_license

def decode_all_pages(infile):
    """Decode all pages of a PDF document."""
    editor = pdf_facades.PdfContentEditor()
    editor.bind_pdf(infile)
    for i in range(editor.pdf_file_info.number_of_pages):
        editor.extract_text(i + 1)
    editor.close()

def decode_page(infile, page_number):
    """Decode a specific page of a PDF document."""
    editor = pdf_facades.PdfContentEditor()
    editor.bind_pdf(infile)
    text = editor.extract_text(page_number)
    editor.close()
    return text

def run_all_examples(data_dir=None, license_path=None):
    """Run all decode examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Decode All Pages", decode_all_pages),
        ("Decode Specific Page", lambda infile: decode_page(infile, 1)),
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