import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add text annotation to page 1
    content_editor.create_text(apd.Rectangle(100, 400, 50, 50), "Text Annotation", "This is a text annotation", True, "Insert", 1)
    # Save updated document
    content_editor.save(outfile)

def add_free_text_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add free text annotation to page 1
    content_editor.create_free_text(apd.Rectangle(200, 480, 150, 25), "This is a free text annotation", 1)
    # Save updated document
    content_editor.save(outfile)

def add_caret_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add caret annotation to page 1
    content_editor.create_caret(1, 
                                apd.Rectangle(350, 400, 10, 10), 
                                apd.Rectangle(300, 380, 115, 15), 
                                "P", "This is a caret annotation",
                                apd.Color.red)
    # Save updated document
    content_editor.save(outfile)

def add_markup_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add markup annotation to page 1
    content_editor.create_markup(apd.Rectangle(120, 440, 200, 20), "This is a highlight annotation", 0, 1, apd.Color.yellow)
    content_editor.create_markup(apd.Rectangle(110, 542, 200, 20), "This is a underline annotation", 1, 1, apd.Color.yellow)
    content_editor.create_markup(apd.Rectangle(120, 568, 200, 20), "This is a strikeout annotation", 2, 1, apd.Color.orange_red)
    content_editor.create_markup(apd.Rectangle(110, 598, 200, 20), "This is a squiggly annotation", 3, 1, apd.Color.dark_blue)
    # Save updated document
    content_editor.save(outfile)

def run_all_examples(data_dir=None, license_path=None):
    """Run all form field modification examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add Text Annotation", add_text_annotation),
        ("Add Free Text Annotation", add_free_text_annotation),
        ("Add Caret Annotation", add_caret_annotation),
        ("Add Markup Annotation", add_markup_annotation),
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

