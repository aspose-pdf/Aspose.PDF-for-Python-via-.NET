import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def replace_image(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Replace image on page 1    
    content_editor.replace_image(1, 1, image_file)
    # Save updated document
    content_editor.save(outfile)


def delete_images(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete image on page 1
    content_editor.delete_image(1, [2])
    # Save updated document
    content_editor.save(outfile)


def delete_all_image(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Delete all images from the document
    content_editor.delete_image()
    # Save updated document
    content_editor.save(outfile)


def run_examples(data_dir=None, license_path=None):
    """Run all form field modification examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Replace Image", replace_image),
        ("Delete Image", delete_images),
        ("Delete All Images", delete_all_image),
    ]

    for name, func in examples:
        try:
            if func.__name__ == "replace_image":
                func(
                    path.join(input_dir, f"{func.__name__}.pdf"),
                    path.join(input_dir, "replacement_image.jpg"),
                    path.join(output_dir, f"{func.__name__}.pdf"),
                )
            else:
                func(
                    path.join(input_dir, f"{func.__name__}.pdf"),
                    path.join(output_dir, f"{func.__name__}.pdf"),
                )
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

if __name__ == "__main__":
    run_examples()
