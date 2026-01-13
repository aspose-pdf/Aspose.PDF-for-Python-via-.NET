from os import path
from collections import Counter
import sys

import aspose.pdf as ap
sys.path.append(path.join(path.dirname(__file__), ".."))
from config import initialize_data_dir, set_license


def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")


def run_all_examples(data_dir=None, license_path=None):
    """Run all PDF artifact examples and report status."""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("count_pdf_artifacts", count_pdf_artifacts),
    ]

    for name, func in examples:
        input_file = path.join(input_dir, f"{func.__name__}.pdf")
        try:
            func(input_file)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()
