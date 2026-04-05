def print_document(file_path):
    printer = pdf_facades.PdfPrinter()
    printer.print_pdf(file_path)

def print_document_with_setup(file_path, printer_name="Microsoft Print to PDF"):
    printer = pdf_facades.PdfPrinter()
    printer.printer_name = printer_name
    printer.print_pdf(file_path)

def print_document_with_settings(file_path, printer_settings):
    printer = pdf_facades.PdfPrinter()
    printer.printer_settings = printer_settings
    printer.print_pdf(file_path)

def print_document_with_settings_and_pages(file_path, page_settings, printer_settings):
    printer = pdf_facades.PdfPrinter()
    printer.page_settings = page_settings
    printer.printer_settings = printer_settings
    printer.print_pdf(file_path)


def run_all_examples(data_dir=None, license_path=None):
    """Run all print examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Print Document with Default Settings", print_document),
        ("Print Document with Printer Setup", print_document_with_setup),
        ("Print Document with Printer Settings", lambda infile: print_document_with_settings(infile, {"printer_name": "Microsoft Print to PDF"})),
        ("Print Document with Page and Printer Settings", lambda infile: print_document_with_settings_and_pages(infile, {"orientation": "landscape"}, {"printer_name": "Microsoft Print to PDF"})),
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