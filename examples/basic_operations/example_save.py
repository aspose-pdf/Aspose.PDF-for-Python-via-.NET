import aspose.pdf as ap
import io
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def save_document_to_file(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    document.save(outfile)


def save_document_to_stream(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    with io.FileIO(outfile, "w") as stream:
        document.save(stream)


def save_document_as_standard(infile, outfile, logfile):
    document = ap.Document(infile)
    document.pages.add()
    document.convert(logfile, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run Save Document examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Save document to file", save_document_to_file),
        ("Save document to stream", save_document_to_stream),
        ("Save document as standard", save_document_as_standard),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, "sample3.pdf")
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            if func == save_document_as_standard:
                log_file_name = path.join(output_dir, f"{func.__name__}_out.log")
                func(input_file_name, output_file_name, log_file_name)
            else:
                func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Save Document examples finished.")


if __name__ == "__main__":
    run_all_examples()
