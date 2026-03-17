import io

import aspose.pdf.facades as pdf_facades
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_attachment(infile, attachment_file ,outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add attachment to page 1
    attachment_stream = io.FileIO(attachment_file, "r")
    content_editor.add_document_attachment(attachment_stream, attachment_file, "This is a sample attachment for demonstration purposes.")
    # Save updated document
    content_editor.save(outfile)

def remove_attachments(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove all attachments from document
    content_editor.delete_attachments()
    # Save updated document
    content_editor.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run all form field modification examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add Attachment", add_attachment),
        ("Remove Attachments", remove_attachments),
    ]

    for name, func in examples:
        try:
            if name == "Add Attachment":
                func(path.join(input_dir, f"{func.__name__}.pdf"),
                     path.join(input_dir, "SampleAttachment.txt"),
                     path.join(output_dir, f"{func.__name__}.pdf"))
            else:
                func(path.join(input_dir, f"{func.__name__}.pdf"),
                     path.join(output_dir, f"{func.__name__}.pdf"))
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

if __name__ == "__main__":
    run_all_examples()
