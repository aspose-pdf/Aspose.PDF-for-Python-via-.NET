from os import path
import sys
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import initialize_data_dir, set_license


def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")


def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)


def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF artifact examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add Watermark Artifact", (add_watermark_artifact, False, False)),
        ("Extract Watermark Artifact", (extract_watermark_from_pdf, False, True)),
        ("Delete Watermark Artifact", (delete_watermark_artifact, False, False)),
    ]

    for name, (func, needs_image, no_output) in examples:
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
