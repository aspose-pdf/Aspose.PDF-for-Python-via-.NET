import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import BytesIO
import sys
from os import path

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import set_license, initialize_data_dir  # noqa: E402


def constructor_with_document_and_save_stream(infile, outfile):
    # Initialize PdfContentEditor using constructor overload that accepts Document
    document = ap.Document(infile)
    content_editor = pdf_facades.PdfContentEditor(document)

    # Save to memory stream using save(stream) overload, then persist to file
    output_stream = BytesIO()
    content_editor.save(output_stream)
    with open(outfile, "wb") as target_stream:
        target_stream.write(output_stream.getvalue())

    content_editor.close()


def bind_from_stream_and_save_stream(infile, outfile):
    # Create editor and bind PDF from in-memory stream
    content_editor = pdf_facades.PdfContentEditor()
    with open(infile, "rb") as source_stream:
        input_stream = BytesIO(source_stream.read())
    content_editor.bind_pdf(input_stream)

    # Save through stream overload to demonstrate bind(stream) + save(stream)
    output_stream = BytesIO()
    content_editor.save(output_stream)
    with open(outfile, "wb") as target_stream:
        target_stream.write(output_stream.getvalue())

    content_editor.close()


def bind_from_document_and_save_file(infile, outfile):
    # Create editor and bind from Document overload
    source_document = ap.Document(infile)
    content_editor = pdf_facades.PdfContentEditor()
    content_editor.bind_pdf(source_document)

    # Save to file-path overload
    content_editor.save(outfile)
    content_editor.close()


def run_all_examples(data_dir=None, license_path=None):
    """Run PdfContentEditor binding and stream overload examples."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "Constructor With Document And Save Stream",
            constructor_with_document_and_save_stream,
        ),
        ("Bind From Stream And Save Stream", bind_from_stream_and_save_stream),
        ("Bind From Document And Save File", bind_from_document_and_save_file),
    ]

    for name, func in examples:
        try:
            func(
                path.join(input_dir, "sample.pdf"),
                path.join(output_dir, f"{func.__name__}.pdf"),
            )
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()
