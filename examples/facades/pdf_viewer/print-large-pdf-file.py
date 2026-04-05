def print_large_pdf(file_path, page_settings=None, printer_settings=None):
    printer = pdf_facades.PdfPrinter()
    if page_settings:
        printer.page_settings = page_settings
    if printer_settings:
        printer.printer_settings = printer_settings
    printer.print_pdf(file_path)

def print_large_pdf_from_stream(input_stream, page_settings=None, printer_settings=None):
    printer = pdf_facades.PdfPrinter()
    if page_settings:
        printer.page_settings = page_settings
    if printer_settings:
        printer.printer_settings = printer_settings
    printer.print_pdf(input_stream)

def run_all_examples(data_dir=None, license_path=None):
    """Run all print examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Print Large PDF with Default Settings", lambda infile: print_large_pdf(infile)),
        ("Print Large PDF with Page Settings", lambda infile: print_large_pdf(infile, page_settings={"orientation": "landscape"})),
        ("Print Large PDF with Printer Settings", lambda infile: print_large_pdf(infile, printer_settings={"printer_name": "Microsoft Print to PDF"})),
        ("Print Large PDF from Stream", lambda infile: print_large_pdf_from_stream(open(infile, "rb"))),
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