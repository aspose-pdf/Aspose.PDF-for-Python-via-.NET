# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfviewer\working-with-pdf-printing-facades
# Code fence language: python


import aspose.pdf as pdf

viewer = pdf.facades.PdfViewer()
viewer.bind_pdf("PrintDocument.pdf")

viewer.auto_resize = True
viewer.auto_rotate = True
viewer.print_page_dialog = False
viewer.print_as_grayscale = True  # Print in grayscale

ps = pdf.printing.PrinterSettings()
pgs = pdf.printing.PageSettings()
ps.printer_name = "Microsoft XPS Document Writer"
pgs.paper_size = pdf.printing.PaperSizes.A4

viewer.print_document_with_settings(pgs, ps)
viewer.close()
