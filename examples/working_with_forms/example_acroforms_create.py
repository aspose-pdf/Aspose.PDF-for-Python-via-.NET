import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def add_text_box_field(output_file_name):
    """Add a single text box field to a new PDF and save it.

    Args:
        output_file_name (str): Full path for the output PDF.
    Returns:
        None
    Example:
        >>> add_text_box_field("E:/Samples/Forms/text_box_field.pdf")
    Note:
        Field appearance uses dashed border and custom colors.
    """
    document = ap.Document()
    page = document.pages.add()

    rectangle = ap.Rectangle(10, 600, 110, 620, True)
    text_box_field = ap.forms.TextBoxField(page, rectangle)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Text Box"

    text_box_field.default_appearance = ap.annotations.DefaultAppearance(
        "Arial", 10, drawing.Color.dark_blue
    )

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field, 1)
    document.save(output_file_name)


def add_text_box_field_nt(output_file_name):
    """Add a text box field with multiple widget annotations and save it.

    Args:
        output_file_name (str): Full path for the output PDF.
    Returns:
        None
    Example:
        >>> add_text_box_field_nt("E:/Samples/Forms/text_box_field_nt.pdf")
    Note:
        Each widget uses its own font, size, and color via ``DefaultAppearance``.
    """
    document = ap.Document()
    page = document.pages.add()

    rects = [
        ap.Rectangle(10, 600, 110, 620, normalize_coordinates=True),
        ap.Rectangle(10, 630, 110, 650, normalize_coordinates=True),
        ap.Rectangle(10, 660, 110, 680, normalize_coordinates=True),
    ]

    default_appearances = [
        ap.annotations.DefaultAppearance("Arial", 10, drawing.Color.dark_blue),
        ap.annotations.DefaultAppearance("Helvetica", 12, drawing.Color.dark_green),
        ap.annotations.DefaultAppearance(
            ap.text.FontRepository.find_font("Calibri"), 14, drawing.Color.dark_magenta
        ),
    ]

    text_box_field = ap.forms.TextBoxField(page, rects)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Some text"

    for i, widget in enumerate(text_box_field):
        widget.default_appearance = default_appearances[i]

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field)
    document.save(output_file_name)


def add_radio_button(output_file_name):
    """Add a radio button field with two options to a new PDF.

    Args:
        output_file_name (str): Full path for the output PDF.
    Returns:
        None
    Example:
        >>> add_radio_button("E:/Samples/Forms/radio_button.pdf")
    Note:
        Options are placed using normalized coordinates on the first page.
    """
    document = ap.Document()
    document.pages.add()

    radio = ap.forms.RadioButtonField(document.pages[1])
    radio.add_option(
        "Option 1", ap.Rectangle(100, 640, 120, 680, normalize_coordinates=True)
    )
    radio.add_option(
        "Option 2", ap.Rectangle(140, 640, 160, 680, normalize_coordinates=True)
    )

    document.form.add(radio)
    document.save(output_file_name)


def add_combo_box(output_file_name):
    """Add a combo box field with multiple options to a new PDF.

    Args:
        output_file_name (str): Full path for the output PDF.
    Returns:
        None
    Example:
        >>> add_combo_box("E:/Samples/Forms/combo_box.pdf")
    Note:
        The ``selected`` index is zero-based; here it selects the fourth item.
    """
    document = ap.Document()
    page = document.pages.add()

    combo = ap.forms.ComboBoxField(
        page, ap.Rectangle(100, 640, 150, 656, normalize_coordinates=True)
    )
    combo.add_option("Red")
    combo.add_option("Yellow")
    combo.add_option("Green")
    combo.add_option("Blue")
    combo.selected = 3

    document.form.add(combo)
    document.save(output_file_name)


def add_checkbox_field_to_pdf(output_file_name):
    """Add a circular checkbox with aqua background to a new PDF.

    Args:
        output_file_name (str): Full path for the output PDF.
    Returns:
        None
    Example:
        >>> add_checkbox_field_to_pdf("E:/Samples/Forms/checkbox.pdf")
    Note:
        Checkbox style set to ``BoxStyle.CIRCLE`` with background color applied.
    """
    document = ap.Document()
    page = document.pages.add()

    checkbox = ap.forms.CheckboxField(
        page, ap.Rectangle(50, 620, 100, 650, normalize_coordinates=True)
    )
    checkbox.characteristics.background = ap.Color.aqua.to_rgb()
    checkbox.style = ap.forms.BoxStyle.CIRCLE

    document.form.add(checkbox)
    document.save(output_file_name)


def add_list_box_field_to_pdf(output_file_name):
    """Add a ListBox field with options to a new PDF.

    Args:
        output_file_name (str): Full path for the output PDF.
    Returns:
        None
    Example:
        >>> add_list_box_field_to_pdf("E:/Samples/Forms/list_box.pdf")
    Note:
        Options are simple strings; use value/display pairs if needed.
    """
    document = ap.Document()
    page = document.pages.add()

    list_box = ap.forms.ListBoxField(
        page, ap.Rectangle(50, 650, 100, 700, normalize_coordinates=True)
    )
    list_box.partial_name = "list"
    list_box.add_option("Red")
    list_box.add_option("Green")
    list_box.add_option("Blue")

    document.form.add(list_box)
    document.save(output_file_name)


def add_signature_field(output_file_name):
    """Add a signature field to a new PDF.

    Args:
        output_file_name (str): Full path for the output PDF.
    Returns:
        None
    Example:
        >>> add_signature_field("E:/Samples/Forms/signature.pdf")
    Note:
        The field rectangle uses absolute coordinates and spans a visible area.
    """
    document = ap.Document()
    page = document.pages.add()

    signature_field = ap.forms.SignatureField(
        page, ap.Rectangle(100, 700, 200, 800, True)
    )
    signature_field.partial_name = "Signature1"
    document.form.add(signature_field)
    document.save(output_file_name)


def add_barcode_field(output_file_name):
    """Add a barcode field to a new PDF and save it.

    Args:
        output_file_name (str): Full path for the output PDF.
    Returns:
        None
    Example:
        >>> add_barcode_field("E:/Samples/Forms/barcode.pdf")
    Note:
        Encodes the sample value ``"1234567890"`` into the barcode widget.
    """
    document = ap.Document()
    page = document.pages.add()

    barcode = ap.forms.BarcodeField(page, ap.Rectangle(100, 700, 200, 740, True))
    barcode.partial_name = "Barcode1"
    barcode.add_barcode("1234567890")
    document.form.add(barcode)
    document.save(output_file_name)


def run_all_examples(data_dir=None, license_path=None):
    """Run all Acroforms creation examples and report status.

    Args:
        data_dir (str, optional): Output directory override. Defaults to ``DATA_DIR``.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    Example:
        >>> run_all_examples()
    Note:
        Each example writes a separate PDF named after the function.
    """

    set_license(license_path)
    _, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("text_box_field", add_text_box_field),
        ("text_box_field_nt", add_text_box_field_nt),
        ("radio_button", add_radio_button),
        ("combo_box", add_combo_box),
        ("checkbox", add_checkbox_field_to_pdf),
        ("list_box", add_list_box_field_to_pdf),
        ("barcode", add_barcode_field),
        ("signature", add_signature_field),
    ]

    for name, func in examples:
        output_file_name = path.join(output_dir, f"{name}_out.pdf")
        try:
            func(output_file_name)
            print(f"✅ {name} completed. Output: {output_file_name}")
        except Exception as e:
            print(f"❌ {name} failed: {e}")

    print(f"\nAll Acroforms creation examples finished. Check output in {output_dir}")


if __name__ == "__main__":
    run_all_examples()
