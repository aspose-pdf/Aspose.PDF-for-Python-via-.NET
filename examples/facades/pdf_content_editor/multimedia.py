import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

# Ensure "examples/config.py" is importable from nested folders like examples/facades/form
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import set_license, initialize_data_dir  # noqa: E402


def add_movie_annotation(infile, movie_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add movie annotation to page 1
    content_editor.create_movie(apd.Rectangle(80, 500, 220, 120), movie_file, 1)
    # Save updated document
    content_editor.save(outfile)


def add_sound_annotation(infile, sound_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add sound annotation to page 1
    content_editor.create_sound(
        apd.Rectangle(80, 450, 30, 30), sound_file, "Speaker", 1, "8000"
    )
    # Save updated document
    content_editor.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run all multimedia examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add Movie Annotation", add_movie_annotation),
        ("Add Sound Annotation", add_sound_annotation),
    ]

    for name, func in examples:
        try:
            if func.__name__ == "add_movie_annotation":
                func(
                    path.join(input_dir, "sample.pdf"),
                    path.join(input_dir, "sample_video.avi"),
                    path.join(output_dir, f"{func.__name__}.pdf"),
                )
            else:
                func(
                    path.join(input_dir, "sample.pdf"),
                    path.join(input_dir, "sample_audio.wav"),
                    path.join(output_dir, f"{func.__name__}.pdf"),
                )
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()
