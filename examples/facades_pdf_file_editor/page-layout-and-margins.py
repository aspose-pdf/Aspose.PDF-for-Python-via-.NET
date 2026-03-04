# Page Layout & Margins
#─ Add Margins to PDF Pages
#─ Resize PDF Page Contents
#─ Add Page Breaks in PDF

from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Add Margins to PDF Pages
def add_margins_to_pdf_pages():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license for Aspose.PDF
    set_license()

    # Open the source PDF document
    with ap.Document(path.join(data_dir, "input.pdf")) as pdf_document:
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the margins to be added (in points)
        left_margin = 36  # 0.5 inch
        right_margin = 36  # 0.5 inch
        top_margin = 36  # 0.5 inch
        bottom_margin = 36  # 0.5 inch

        # Add margins to each page in the PDF document
        for page in pdf_document.pages:
            page.trim_box = ap.Rectangle(
                page.trim_box.llx + left_margin,
                page.trim_box.lly + bottom_margin,
                page.trim_box.urx - right_margin,
                page.trim_box.ury - top_margin,
            )

        # Save the modified PDF document
        output_path = path.join(data_dir, "output_with_margins.pdf")
        pdf_document.save(output_path)
        print(f"PDF with added margins saved to: {output_path}")

# Resize PDF Page Contents
def resize_pdf_page_contents():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license for Aspose.PDF
    set_license()

    # Open the source PDF document
    with ap.Document(path.join(data_dir, "input.pdf")) as pdf_document:
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the scaling factor (e.g., 0.5 for 50% reduction)
        scaling_factor = 0.5

        # Resize the contents of each page in the PDF document
        for page in pdf_document.pages:
            page.scale_content(scaling_factor)

        # Save the modified PDF document
        output_path = path.join(data_dir, "output_resized.pdf")
        pdf_document.save(output_path)
        print(f"PDF with resized contents saved to: {output_path}")

# Add Page Breaks in PDF
def add_page_breaks_in_pdf():
    # Initialize the data directory
    data_dir = initialize_data_dir()

    # Set the license for Aspose.PDF
    set_license()

    # Open the source PDF document
    with ap.Document(path.join(data_dir, "input.pdf")) as pdf_document:
        # Create a PdfFileEditor object
        pdf_editor = pdf_facades.PdfFileEditor()

        # Define the page break position (e.g., after every 2 pages)
        page_break_position = 2

        # Add page breaks at the specified position
        for i in range(page_break_position, len(pdf_document.pages), page_break_position):
            pdf_editor.insert_page(pdf_document, i)

        # Save the modified PDF document
        output_path = path.join(data_dir, "output_with_page_breaks.pdf")
        pdf_document.save(output_path)
        print(f"PDF with added page breaks saved to: {output_path}")                

def run_all_examples(data_dir=None, license_path=None):
    """Run all page layout and margins examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.

    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [

        ("Add Margins to PDF Pages", add_margins_to_pdf, "output_with_margins.pdf"),
        ("Resize PDF Page Contents", resize_pdf_page_contents, "output_resized.pdf"),
        ("Add Page Breaks in PDF", add_page_breaks_in_pdf, "output_with_page_breaks.pdf")
    ]

    for name, func, data_file_name in examples:
        try:
            if (func.__name__ == "add_margins_to_pdf") or (func.__name__ == "resize_pdf_page_contents") or (func.__name__ == "add_page_breaks_in_pdf"):
                input_file_name = path.join(input_dir, "input.pdf")
            else:
                input_file_name = path.join(input_dir, "f")
            output_file_name = path.join(output_dir, data_file_name)
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll page layout and margins examples finished.")


if __name__ == "__main__":
    run_all_examples()