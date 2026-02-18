# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfviewer\working-with-pdf-printing-facades
# Code fence language: python


import aspose.pdf as pdf

# Prepare viewer
viewer = pdf.facades.PdfViewer()

# Bind the PDF (open)
viewer.bind_pdf("PrintDocument.pdf")

# Adjust settings
viewer.auto_resize = True
viewer.auto_rotate = True
viewer.print_page_dialog = False

# Create printer and page settings
ps = pdf.printing.PrinterSettings()
pgs = pdf.printing.PageSettings()

# You can explicitly specify printer name (optional)
# ps.printer_name = "Your Printer Name"

# Example: Set A4 page size
pgs.paper_size = pdf.printing.PaperSizes.A4

# Print
viewer.print_document_with_settings(pgs, ps)

# Release resources
viewer.close()
