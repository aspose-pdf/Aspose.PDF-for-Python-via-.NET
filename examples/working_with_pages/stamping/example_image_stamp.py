import sys
import aspose.pdf as ap
from os import path

sys.path.append(path.join(path.dirname(__file__), "../.."))

from config import set_license, initialize_data_dir


def add_image_stamp(infile, input_image_file, outfile):
    document = ap.Document(infile)
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)


def add_image_stamp_with_quality_control(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)


def add_image_as_background_in_floating_box(infile, input_image_file, outfile):

    document = ap.Document(infile)
    page = document.pages[1]
    # Create FloatingBox object
    box = ap.FloatingBox(200.0, 100.0)
    # Set left position for FloatingBox
    box.left = 40
    # Set Top position for FloatingBox
    box.top = 80
    # Set the Horizontal alignment for FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Add text fragment to paragraphs collection of FloatingBox
    box.paragraphs.add(ap.text.TextFragment("Text in Floating Box"))
    # Set border for FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Add background image
    box.background_image = img
    # Set background color for FloatingBox
    box.background_color = ap.Color.yellow
    # Add FloatingBox to paragraphs collection of page object
    page.paragraphs.add(box)
    # Save the PDF document
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run image stamps examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)
    examples = [
        ("add_image_stamp", add_image_stamp),
        (
            "add_image_stamp_image_control_image_quality",
            add_image_stamp_with_quality_control,
        ),
        (
            "add_image_as_background_in_floating_box",
            add_image_as_background_in_floating_box,
        ),
    ]

    input_file_name = path.join(input_dir, "sample.pdf")
    input_image_name = path.join(input_dir, "logo.jpg")

    for name, func in examples:
        output_file_name = path.join(output_dir, f"{name}_out.pdf")
        try:
            func(input_file_name, input_image_name, output_file_name)
            print(f"✅ {name} completed. Output: {output_file_name}")
        except Exception as e:
            print(f"❌ {name} failed: {e}")

    print(f"\nAll image stamps examples finished. Check output in {output_dir}")


# Main execution
if __name__ == "__main__":
    run_all_examples()
