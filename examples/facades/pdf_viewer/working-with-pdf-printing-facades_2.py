# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfviewer\working-with-pdf-printing-facades
# Code fence language: python


import aspose.pdf as pdf
import System
from System.Windows.Forms import PrintDialog, DialogResult

def printing_pdf_display_print_dialog():
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

        # Show system print dialog
        print_dialog = PrintDialog()

        if print_dialog.ShowDialog() == DialogResult.OK:
            # Convert .NET PrinterSettings to Aspose equivalents
            ps = pdf.printing.PrinterSettings.to_aspose_printer_settings(
                print_dialog.PrinterSettings
            )

            pgs = pdf.printing.PageSettings.to_aspose_page_settings(
                print_dialog.PrinterSettings.DefaultPageSettings
            )

            # Print document using selected printer and page settings
            viewer.print_document_with_settings(pgs, ps)

    finally:
        # Release resources
        viewer.close()
