# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfviewer\working-with-pdf-printing-facades
# Code fence language: python


import aspose.pdf as pdf

viewer = pdf.facades.PdfViewer()
viewer.bind_pdf("PrintDocument.pdf")

viewer.auto_resize = True
viewer.auto_rotate = True
viewer.print_page_dialog = False

ps = pdf.printing.PrinterSettings()
pgs = pdf.printing.PageSettings()

# Set soft printer and print to file
ps.printer_name = "Adobe PDF"  # Or another virtual printer
ps.print_file_name = "OutFile.pdf"
ps.print_to_file = True

pgs.paper_size = pdf.printing.PaperSizes.A4

viewer.print_document_with_settings(pgs, ps)
viewer.close()
