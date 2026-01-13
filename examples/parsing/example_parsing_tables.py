import aspose.pdf as ap
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir



def extract_tables_from_pdf(infile):
    # Open PDF document
    document = ap.Document(infile)

    # Iterate through each page in the document
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)

        for table in absorber.table_list:
            print("Table")
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append("".join(seg.text for seg in fragment.segments))
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))


def extract_table_from_specific_area(infile):

    # Open PDF document
    document = ap.Document(infile)

    # Get the first page (index starts from 1 in Aspose.PDF)
    page = document.pages[1]

    # Find the first square annotation
    square_annotation = next(
        (
            ann
            for ann in page.annotations
            if ann.annotation_type == ap.annotations.AnnotationType.SQUARE
        ),
        None,
    )

    if square_annotation is None:
        print("No square annotation found.")
        return

    # Initialize the TableAbsorber
    absorber = ap.text.TableAbsorber()
    absorber.visit(page)

    # Iterate through tables on the page
    for table in absorber.table_list:
        table_rect = table.rectangle
        annotation_rect = square_annotation.rect

        # Check if the table is inside the annotation region
        is_in_region = (
            annotation_rect.llx < table_rect.llx
            and annotation_rect.lly < table_rect.lly
            and annotation_rect.urx > table_rect.urx
            and annotation_rect.ury > table_rect.ury
        )

        if is_in_region:
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append("".join(seg.text for seg in fragment.segments))
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))


def export_tables_to_excel(infile, outfile):
    document = ap.Document(infile)
    excel_save = ap.ExcelSaveOptions()
    excel_save.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(outfile, excel_save)


def run_all_examples(data_dir=None, license_path=None):
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Extract tables from PDF", extract_tables_from_pdf, "sample.pdf", None),
        (
            "Extract table from specific area",
            extract_table_from_specific_area,
            "sample-table-mark.pdf",
            None,
        ),
        (
            "Export tables to Excel",
            export_tables_to_excel,
            "sample.pdf",
            "tables_output.xlsx",
        ),
    ]

    for name, func, input_file, output_file in examples:
        try:
            args = [path.join(input_dir, input_file)]
            if output_file:
                args.append(path.join(output_dir, output_file))
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
