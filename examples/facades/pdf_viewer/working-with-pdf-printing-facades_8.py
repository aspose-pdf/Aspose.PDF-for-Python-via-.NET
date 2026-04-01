# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfviewer\working-with-pdf-printing-facades
# Code fence language: python


import aspose.pdf as pdf
import os

class PrintingJobSettings:
    def __init__(self, from_page, to_page, output_file, duplex_mode):
        self.from_page = from_page
        self.to_page = to_page
        self.output_file = output_file
        self.mode = duplex_mode


def printing_pages_in_simplex_and_duplex_mode():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_printing()
    output_dir = data_dir

    printing_job_index = 0
    printing_jobs = []

    # Create printing jobs
    printing_jobs.append(
        PrintingJobSettings(
            from_page=1,
            to_page=3,
            output_file=output_dir + "PrintPageRange_p1-3_out.xps",
            duplex_mode=pdf.printing.Duplex.Default
        )
    )

    printing_jobs.append(
        PrintingJobSettings(
            from_page=4,
            to_page=6,
            output_file=output_dir + "PrintPageRange_p4-6_out.xps",
            duplex_mode=pdf.printing.Duplex.Simplex
        )
    )

    printing_jobs.append(
        PrintingJobSettings(
            from_page=7,
            to_page=7,
            output_file=output_dir + "PrintPageRange_p7_out.xps",
            duplex_mode=pdf.printing.Duplex.Default
        )
    )

    # Create PdfViewer object
    viewer = pdf.facades.PdfViewer()

    try:
        # Bind PDF document
        viewer.bind_pdf(data_dir + "Print-PageRange.pdf")

        # Set printing attributes
        viewer.auto_resize = True
        viewer.auto_rotate = True
        viewer.print_page_dialog = False

        # Create printer and page settings
        ps = pdf.printing.PrinterSettings()
        pgs = pdf.printing.PageSettings()

        # Set printer name
        ps.printer_name = "Microsoft XPS Document Writer"

        # Set initial job settings
        ps.print_to_file = True
        ps.print_range = pdf.printing.PrintRange.SomePages

        # Paper size and margins
        pgs.paper_size = pdf.printing.PaperSizes.A4
        ps.default_page_settings.paper_size = pgs.paper_size
        pgs.margins = pdf.devices.Margins(0, 0, 0, 0)

        # Helper to apply a print job
        def apply_print_job(index):
            job = printing_jobs[index]
            ps.print_file_name = os.path.abspath(job.output_file)
            ps.from_page = job.from_page
            ps.to_page = job.to_page
            ps.duplex = job.mode

        # Apply first job
        apply_print_job(printing_job_index)

        # EndPrint event handler (chain next jobs)
        def on_end_print(sender, args):
            nonlocal printing_job_index
            printing_job_index += 1

            if printing_job_index < len(printing_jobs):
                apply_print_job(printing_job_index)
                viewer.print_document_with_settings(pgs, ps)

        viewer.end_print += on_end_print

        # Start first print job
        viewer.print_document_with_settings(pgs, ps)

    finally:
        # Release resources
        viewer.close()
