# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfviewer\working-with-pdf-printing-facades
# Code fence language: python


import aspose.pdf as pdf

def printing_pdf_hide_print_dialog():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_printing()

    # Create PdfViewer object
    viewer = pdf.facades.PdfViewer()

    try:
        # Bind PDF document
        viewer.bind_pdf(data_dir + "PrintDocument.pdf")

        # Set attributes for printing
        # Print the file with adjusted size
        viewer.auto_resize = True
        # Print the file with adjusted rotation
        viewer.auto_rotate = True
        # Do not show the page number dialog
        viewer.print_page_dialog = False

        # Create printer and page settings
        ps = pdf.printing.PrinterSettings()
        pgs = pdf.printing.PageSettings()

        # Set XPS/PDF printer name
        ps.printer_name = "OneNote for Windows 10"

        # Set page size (A4)
        pgs.paper_size = pdf.printing.PaperSizes.A4

        # Set page margins (left, right, top, bottom)
        pgs.margins = pdf.devices.Margins(0, 0, 0, 0)

        # Print document using printer and page settings
        viewer.print_document_with_settings(pgs, ps)

    finally:
        # Close viewer and release resources
        viewer.close()
