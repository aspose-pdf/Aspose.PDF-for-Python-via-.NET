# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfviewer\working-with-pdf-printing-facades
# Code fence language: python


import aspose.pdf as pdf
import os

def printing_multiple_documents_in_single_job():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_printing()

    # Paths to documents to be printed
    path1 = os.path.join(data_dir, "PrintDocument.pdf")
    path2 = os.path.join(data_dir, "Print-PageRange.pdf")
    path3 = os.path.join(data_dir, "35925_1_3.xps")

    # Create printer settings
    printer_settings = pdf.printing.PrinterSettings()

    # Use default system printer (same idea as PrintDocument.PrinterSettings.PrinterName)
    # If you want to force a printer, uncomment and set it explicitly:
    # printer_settings.printer_name = "Microsoft XPS Document Writer"

    # Create page settings
    page_settings = pdf.printing.PageSettings()
    page_settings.paper_size = pdf.printing.PaperSizes.A4
    page_settings.margins = pdf.devices.Margins(0, 0, 0, 0)

    # Print multiple documents in a single print job
    pdf.facades.PdfViewer.print_documents(
        printer_settings,
        page_settings,
        path1,
        path2,
        path3
    )
