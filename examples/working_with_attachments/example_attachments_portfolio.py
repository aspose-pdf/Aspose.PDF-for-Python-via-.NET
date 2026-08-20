from os import path
import aspose.pdf as ap
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_pdf_portfolio(input_files, outfile):
    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_files[0])
    word = ap.FileSpecification(input_files[1])
    image = ap.FileSpecification(input_files[2])

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(outfile)


def remove_files_from_PDF_Portfolio(infile, outfile):
    # Open document
    document = ap.Document(infile)
    document.collection.delete()

    # Save updated file
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run attachments examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "Create PDF Portfolio",
            create_pdf_portfolio,
            (
                [
                    path.join(input_dir, "sample_word.docx"),
                    path.join(input_dir, "sample_excel.xlsx"),
                    path.join(input_dir, "sample_image.png"),
                ],
                path.join(output_dir, "sample_with_portfolio.pdf"),
            ),
        ),
        (
            "Remove files from PDF Portfolio",
            remove_files_from_PDF_Portfolio,
            (
                path.join(input_dir, "sample_with_portfolio.pdf"),
                path.join(output_dir, "sample_portfolio_removed.pdf"),
            ),
        ),
    ]

    for example in examples:
        name, func, args = example
        try:
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()
