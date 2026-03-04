import aspose.pdf as ap
import aspose.pydrawing as apd
import aspose.pdf.facades as pdf_facades

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_free_text_annotation(infile, outfile):
    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor()
    # Bind PDF document to PdfContentEditor
    editor.bind_pdf(infile)

    # Search for the text "PDF" on the first page
    tfa = ap.text.TextFragmentAbsorber("PDF")
    tfa.visit(editor.document.pages[1])

    # Define rectangle above the found text fragment
    rect = apd.Rectangle(
        int(tfa.text_fragments[1].rectangle.llx),
        int(tfa.text_fragments[1].rectangle.ury) + 5,
        100,   # Width
        18     # Height        
    )

    # Add free text annotation on page 1
    editor.create_free_text(rect, "Free Text Demo", 1)

    # Save updated PDF document
    editor.save(outfile)
    editor.close()

def add_text_annotation(infile, outfile):
    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor()
    # Bind PDF document to PdfContentEditor
    editor.bind_pdf(infile)

    # Search for the text "PDF" on the first page
    tfa = ap.text.TextFragmentAbsorber("PDF")
    tfa.visit(editor.document.pages[1])

    # Define rectangle above the found text fragment
    rect = apd.Rectangle(
        int(tfa.text_fragments[1].rectangle.llx),
        int(tfa.text_fragments[1].rectangle.ury) + 5,
        100,   # Width
        18     # Height        
    )

    # Add free text annotation on page 1
    editor.create_text(rect, "Title", "Content", True, "Subject", 1)

    # Save updated PDF document
    editor.save(outfile)
    editor.close()

def add_line_annotation(infile, outfile):
    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor()
    # Bind PDF document to PdfContentEditor
    editor.bind_pdf(infile)

    # Add line annotation on page 1
    editor.create_line(        
        apd.Rectangle(550, 93, 562, 439),   # Bounding rectangle
        "A sample line",                # Content
        556, 99,                        # Starting coordinates (X1, Y1)
        556, 443,                       # Ending coordinates (X2, Y2)
        1,                              # Starting border style
        2,                              # Ending border style
        apd.Color.dark_red,             # Line color
        "dash",                         # Line style
        [1, 0, 3],                      # Dash pattern
        ["Open", "Open"]                # Line ending styles
    )


    # Save updated PDF document
    editor.save(outfile)
    editor.close()


def run_all_examples(data_dir=None, license_path=None):
    """Run all form field modification examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add Free Text Annotation", add_free_text_annotation),
        ("Add Text Annotation", add_text_annotation),
        ("Add Line Annotation", add_line_annotation)
    ]

    for name, func in examples:
        try:
            func(path.join(input_dir, f"{func.__name__}.pdf"),
                 path.join(output_dir, f"{func.__name__}.pdf"))
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()