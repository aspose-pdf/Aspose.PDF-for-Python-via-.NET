# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfviewer\working-with-pdf-printing-facades
# Code fence language: python


import aspose.pdf as pdf

def printing_pdf_to_postscript():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_printing()

    # Create PdfViewer object
    viewer = pdf.facades.PdfViewer()

    try:
        # Bind PDF document
        viewer.bind_pdf(data_dir + "PrintDocument.pdf")

        # Set attributes for printing
        viewer.auto_resize = True
        viewer.auto_rotate = True
        viewer.print_page_dialog = False
        viewer.print_as_image = False  # Do NOT convert pages to images

        # Create printer and page settings
        ps = pdf.printing.PrinterSettings()
        pgs = pdf.printing.PageSettings()

        # Set PostScript printer name
        ps.printer_name = "HP Universal Printing PS (v7.0.0)"

        # Set output file and enable PrintToFile
        ps.print_file_name = data_dir + "PdfToPostScript_out.ps"
        ps.print_to_file = True

        # Set page size (A4)
        pgs.paper_size = pdf.printing.PaperSizes.A4

        # Set page margins (left, right, top, bottom)
        pgs.margins = pdf.devices.Margins(0, 0, 0, 0)

        # Print document using printer and page settings
        viewer.print_document_with_settings(pgs, ps)

    finally:
        # Release resources
        viewer.close()
