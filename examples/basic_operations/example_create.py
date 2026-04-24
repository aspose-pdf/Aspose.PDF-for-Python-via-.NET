import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def example_create(outfile):
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
    text_builder.append_text(textFragment)

    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Create PDF Document", example_create),
    ]

    for name, func in examples:
        try:
            output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
            func(output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Create PDF Document examples finished.")


if __name__ == "__main__":
    run_all_examples()
