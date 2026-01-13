from os import path
from io import FileIO

import aspose.pdf as ap

import sys
sys.path.append(path.join(path.dirname(__file__), ".."))
from config import initialize_data_dir, set_license


def add_background_image_to_pdf(infile, imagefile, outfile):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)


def add_background_image_with_opacity_to_pdf(infile, imagefile, outfile):
    """Add a background image with opacity to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = 0.5
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)


def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)


def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF artifact examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = {
        "add_background_image_to_pdf": (add_background_image_to_pdf, True, False),
        "add_background_color_to_pdf": (add_background_color_to_pdf, False, False),
        "add_background_image_with_opacity_to_pdf": (add_background_image_with_opacity_to_pdf, True, False),
        "remove_background": (remove_background, False, False),
    }

    for name, (func, needs_image, no_output) in examples.items():
        input_file = path.join(input_dir, f"{func.__name__}.pdf")
        output_file = path.join(output_dir, f"{func.__name__}_out.pdf")

        try:
            if needs_image:
                func(input_file, path.join(input_dir, "background.jpg"), output_file)
            elif no_output:
                func(input_file)
            else:
                func(input_file, output_file)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()
