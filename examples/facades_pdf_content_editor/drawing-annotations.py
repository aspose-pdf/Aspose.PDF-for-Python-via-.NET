import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Drawing Annotations
#     Line
#     Square and Circle
#     Polygon
#     Polyline
#     Curve

def add_line_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)
    
    # Create LineAnnotation object
    rect = apd.Rectangle(100, 100, 200, 200)
    contents = "This is line annotation"
    content_editor.create_line(rect, contents, 100, 100, 200, 200, 1, 1, apd.Color.red, "Solid", [3,2], ["Square"])
    
    # Save output PDF file
    content_editor.save(outfile)

def add_square_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)
    
    # Create SquareAnnotation object
    rect = apd.Rectangle(100, 300, 200, 400)
    contents = "This is square annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, True, 1, 3)
    
    # Save output PDF file
    content_editor.save(outfile)

def add_circle_annotation(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind input PDF file
    content_editor.bind_pdf(infile)
    
    # Create CircleAnnotation object
    rect = apd.Rectangle(300, 300, 400, 400)
    contents = "This is circle annotation"
    content_editor.create_square_circle(rect, contents, apd.Color.blue, False, 1, 3)
    
    # Save output PDF file
    content_editor.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run all form field modification examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Line Annotation", add_line_annotation),
        ("Square Annotation", add_square_annotation),
        ("Circle Annotation", add_circle_annotation)
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
