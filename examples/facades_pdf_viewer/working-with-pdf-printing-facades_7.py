# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfviewer\working-with-pdf-printing-facades
# Code fence language: python


import aspose.pdf as pdf

def checking_print_job_status():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_printing()

    # Instantiate PdfViewer object
    viewer = pdf.facades.PdfViewer()

    try:
        # Bind PDF document
        viewer.bind_pdf(data_dir + "PrintDocument.pdf")

        # Set attributes for printing
        viewer.auto_resize = True
        viewer.auto_rotate = True
        viewer.print_page_dialog = False
        viewer.print_as_image = False

        # Create printer and page settings
        ps = pdf.printing.PrinterSettings()
        pgs = pdf.printing.PageSettings()

        # Specify the printer name
        ps.printer_name = "Microsoft XPS Document Writer"

        # Set output file name and enable PrintToFile
        ps.print_file_name = data_dir + "CheckingPrintJobStatus_out.xps"
        ps.print_to_file = True

        # Set page size (A4)
        pgs.paper_size = pdf.printing.PaperSizes.A4

        # Set page margins
        pgs.margins = pdf.devices.Margins(0, 0, 0, 0)

        # Print document using printer and page settings
        viewer.print_document_with_settings(pgs, ps)

        # Check the print status
        if viewer.print_status is not None:
            # An exception was thrown during printing
            print(str(viewer.print_status))
        else:
            # Printing completed successfully
            print("Printing completed without any issue.")

    finally:
        # Release resources
        viewer.close()
