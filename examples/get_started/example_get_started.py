import aspose.pdf as ap
from datetime import timedelta

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def simple_example(outfile):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    text_fragment = ap.text.TextFragment("Hello, world!")
    text_fragment.position = ap.text.Position(100, 600)

    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.blue
    text_fragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    text_builder.append_text(text_fragment)

    document.save(outfile)


def complex_example(outfile):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    image_file_name = path.join(DATA_DIR, "logo.png")
    page.add_image(image_file_name, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    description_text = (
        "Visitors must buy tickets online and tickets are limited to 5,000 per day. "
        "Ferry service is operating at half capacity and on a reduced schedule. "
        "Expect lineups."
    )
    description = ap.text.TextFragment(description_text)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    header_row = table.rows.add()
    header_row.cells.add("Departs City")
    header_row.cells.add("Departs Island")

    for i in range(header_row.cells.count):
        header_row.cells[i].background_color = ap.Color.gray
        header_row.cells[
            i
        ].default_cell_text_state.foreground_color = ap.Color.white_smoke

    time = timedelta(hours=6, minutes=0)
    inc_time = timedelta(hours=0, minutes=30)

    for _ in range(10):
        data_row = table.rows.add()
        data_row.cells.add(str(time))
        time += inc_time
        data_row.cells.add(str(time))

    page.paragraphs.add(table)

    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Simple Example", simple_example),
        ("Complex Example", complex_example),
    ]

    global DATA_DIR
    DATA_DIR = input_dir

    for name, func in examples:
        try:
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Document examples finished.")


if __name__ == "__main__":
    run_all_examples()
