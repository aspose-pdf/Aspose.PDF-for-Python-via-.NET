import aspose.pdf as ap
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def extract(infile: str) -> None:
    """Extract and print all tables from a PDF file."""
    document = ap.Document(infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row:")
                row_txt = ""
                for cell in row.cell_list:
                    cell_txt = ""
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        for seg in fragment.segments:
                            cell_txt += seg.text
                    row_txt += " | "
                    row_txt += cell_txt
                print(row_txt)


def run_all_examples(data_dir=None, license_path=None):
    set_license(license_path)
    input_dir, _ = initialize_data_dir(data_dir)

    examples = [
        ("extract", extract),
    ]

    for name, func in examples:
        try:
            input_file_name = path.join(input_dir, f"{name}.pdf")
            func(input_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")



if __name__ == "__main__":
    run_all_examples()
