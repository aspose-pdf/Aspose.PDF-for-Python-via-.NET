import sys
from os import path

import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), '..'))
from config import set_license, initialize_data_dir


def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact


def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)


def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)


def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF artifact examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("add_bates_n_artifact", (add_bates_n_artifact, False, False)),
        ("add_bates_n_artifact_pagination", (add_bates_n_artifact_pagination, False, False)),
        ("delete_bates_numbering", (delete_bates_numbering, False, False)),
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