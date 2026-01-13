import aspose.pdf as ap
import aspose.pdf.drawing as drawing

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def check_shape_bounds(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = ap.drawing.Graph(100, 100)
    graph.top = 10
    graph.left = 15
    graph.border = ap.BorderInfo(ap.BorderSide.BOX, 1, ap.Color.black)
    page.paragraphs.add(graph)

    rect = drawing.Rectangle(-1, 0, 50, 50)
    rect.graph_info.fill_color = ap.Color.tomato
    try:
        graph.shapes.update_bounds_check_mode(
            ap.BoundsCheckMode.THROW_EXCEPTION_IF_DOES_NOT_FIT
        )
        graph.shapes.add(rect)
    except Exception as e:
        print(e)


def run_all_examples(data_dir=None, license_path=None):
    set_license(license_path)
    _, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Check shape bounds", check_shape_bounds),
    ]

    for name, func in examples:
        try:
            output_file_name = path.join(output_dir, f"{func.__name__}.pdf")
            func(output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
    run_all_examples()
