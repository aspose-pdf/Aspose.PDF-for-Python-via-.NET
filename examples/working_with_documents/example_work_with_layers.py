from io import FileIO
import aspose.pdf as ap
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_layers(outfile):
    """
    Add three colored line layers (red, green, blue) to a new PDF document.

    Args:
        outfile (str): The filename for the output PDF file

    Returns:
        None

    Example:
        >>> add_layers("output.pdf")

    Note:
        Creates a PDF with three layers containing horizontal lines:
        - "Red Line" at y=700
        - "Green Line" at y=750
        - "Blue Line" at y=800
    """
    path_outfile = path.join(outfile)

    try:
        document = ap.Document()
        page = document.pages.add()

        # Red layer
        layer = ap.Layer("oc1", "Red Line")
        layer.contents.append(ap.operators.SetRGBColorStroke(1, 0, 0))
        layer.contents.append(ap.operators.MoveTo(500, 700))
        layer.contents.append(ap.operators.LineTo(400, 700))
        layer.contents.append(ap.operators.Stroke())
        page.layers.append(layer)

        # Green layer
        layer = ap.Layer("oc2", "Green Line")
        layer.contents.append(ap.operators.SetRGBColorStroke(0, 1, 0))
        layer.contents.append(ap.operators.MoveTo(500, 750))
        layer.contents.append(ap.operators.LineTo(400, 750))
        layer.contents.append(ap.operators.Stroke())
        page.layers.append(layer)

        # Blue layer
        layer = ap.Layer("oc3", "Blue Line")
        layer.contents.append(ap.operators.SetRGBColorStroke(0, 0, 1))
        layer.contents.append(ap.operators.MoveTo(500, 800))
        layer.contents.append(ap.operators.LineTo(400, 800))
        layer.contents.append(ap.operators.Stroke())
        page.layers.append(layer)

        document.save(outfile)
        print(f"\nLayers added successfully to PDF file.\nFile saved at {path_outfile}")
    except Exception as e:
        print(f"Error adding layers: {e}")


def lock_layer(infile, outfile):
    """
    Lock the first layer of the first page in a document.

    Args:
        infile (str): The name of the input file
        outfile (str): The name of the output file

    Returns:
        None

    Example:
        >>> lock_layer("input.pdf", "locked_output.pdf")

    Note:
        If no layers are found, prints a message and returns without saving.
    """

    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) > 0:
        layer = page.layers[0]
        layer.lock()
        document.save(outfile)
        print(f"Layer locked successfully. File saved at {outfile}")
    else:
        print("No layers found in the document.")


def extract_layers(infile, outfile):
    """
    Extract all layers from the first page and save each as a separate file.

    Args:
        infile (str): The name of the input PDF file
        outfile (str): The base name for output files (index will be appended)

    Returns:
        None

    Example:
        >>> extract_layers("input.pdf", "layer_output.pdf")
        # Creates layer_output1.pdf, layer_output2.pdf, etc.

    Note:
        Only extracts layers from the first page of the input PDF.
    """
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    index = 1
    for layer in layers:
        output_file = outfile.replace(".pdf", f"{index}.pdf")
        layer.save(output_file)
        print(f"Layer {index} saved to {output_file}")
        index += 1


def extract_layers_stream(infile, outfile):
    """
    Extract the first layer from the first page and save it to a stream.

    Args:
        infile (str): The name of the input file
        outfile (str): The name of the output file

    Returns:
        None

    Example:
        >>> extract_layers_stream("input.pdf", "layer.pdf")

    Note:
        If no layers are found on the first page, prints a message and returns.
        The extracted layer is saved as a binary stream.
    """

    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")


def flatten_layers(infile, outfile):
    """
    Flatten all layers of the first page in a document.

    Args:
        infile (str): The name of the input file
        outfile (str): The name of the output file

    Returns:
        None

    Example:
        >>> flatten_layers("input.pdf", "flattened.pdf")

    Note:
        Flattening makes all layers permanent and non-toggleable.
    """

    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    for layer in layers:
        layer.flatten(True)

    document.save(outfile)
    print(f"Layers flattened successfully. File saved at {outfile}")


def merge_layers(infile, outfile):
    """
    Merge all layers of the first page into a single layer.

    Args:
        infile (str): The name of the input file
        outfile (str): The name of the output file

    Returns:
        None

    Example:
        >>> merge_layers("input.pdf", "merged.pdf")

    Note:
        All layers are combined into a new layer named "LayerNew".
    """

    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) == 0:
        print("No layers found in the document.")
        return

    new_layer_name = "LayerNew"
    page.merge_layers(new_layer_name)
    document.save(outfile)
    print(f"Layers merged successfully. File saved at {outfile}")


def run_all_examples(data_dir=None, license_path=None):
    """Run work with layers examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add layers", add_layers),
        ("Lock layer", lock_layer),
        ("Extract layers", extract_layers),
        ("Extract layers from stream", extract_layers_stream),
        ("Flatten layers", flatten_layers),
        ("Merge layers", merge_layers),
    ]

    input_file_name = path.join(input_dir, "sample_layers.pdf")
    for name, func in examples:
        try:
            if func.__name__ == "add_layers":
                func(input_file_name)
            else:
                output_file_name = path.join(output_dir, f"{func.__name__}.pdf")
                func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
