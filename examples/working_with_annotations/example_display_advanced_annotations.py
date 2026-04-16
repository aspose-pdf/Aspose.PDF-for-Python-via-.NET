import sys
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
from os import path


sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir

def watermark_add(infile, outfile):
    """
    Add a watermark annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> watermark_add("sample.pdf", "output.pdf")

    Note:
        The watermark is positioned at coordinates (100, 0, 400, 100) with blue text
        at 25pt font size and 50% opacity.
    """
    document = ap.Document(infile)
    # Create Annotation
    # Load Page object to add Annotation
    page = document.pages[1]

    # Create Annotation
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Add annotation into Annotation collection of Page
    page.annotations.append(wa)

    # Create TextState for Font settings
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Set opacity level of Annotation Text
    wa.opacity = 0.5

    # Add Text in Annotation
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(outfile)


def watermark_get(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all watermark annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> watermark_get("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all watermark annotations found on the first page.
    """
    document = ap.Document(infile)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)    


def watermark_delete(infile, outfile):
    """
    Delete all watermark annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> watermark_delete("sample.pdf", "output.pdf")

    Note:
        This function removes all watermark annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(outfile)        

def add_3d_annotation():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Create PDF document
    document = ap.Document()

    # Load 3D content
    pdf3d_content = ann.PDF3DContent(data_dir + "Ring.u3d")

    # Create 3D artwork
    pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
    pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(ann.LightingSchemeType.cad)
    pdf3d_artwork.render_mode = ann.PDF3DRenderMode(ann.RenderModeType.solid)

    # Define matrices for different views
    top_matrix = ann.Matrix3D(
        1, 0, 0,
        0, -1, 0,
        0, 0, -1,
        0.10271, 0.08184, 0.273836
    )

    front_matrix = ann.Matrix3D(
        0, -1, 0,
        0, 0, 1,
        -1, 0, 0,
        0.332652, 0.08184, 0.085273
    )

    # Add views to the 3D artwork
    pdf3d_artwork.view_array.append(
        ann.PDF3DView(document, top_matrix, 0.188563, "Top")
    )
    pdf3d_artwork.view_array.append(
        ann.PDF3DView(document, front_matrix, 0.188563, "Left")
    )

    # Add page
    page = document.pages.add()

    # Create 3D annotation
    pdf3d_annotation = ann.PDF3DAnnotation(
        page,
        ap.Rectangle(100, 500, 300, 700),
        pdf3d_artwork
    )

    # Set properties
    pdf3d_annotation.border = ann.Border(pdf3d_annotation)
    pdf3d_annotation.set_default_view_index(1)
    pdf3d_annotation.flags = ann.AnnotationFlags.no_zoom
    pdf3d_annotation.name = "Ring.u3d"

    # Optional preview image
    # pdf3d_annotation.set_image_preview(data_dir + "sample_3d.png")

    # Add annotation to the page
    page.annotations.append(pdf3d_annotation)

    # Save PDF document
    document.save(data_dir + "Add3dAnnotation_out.pdf")


def add_screen_annotation_with_media():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Open PDF document
    document = ap.Document(data_dir + "sample.pdf")

    # Path to the media file (e.g., SWF)
    media_file = data_dir + "input.swf"

    # Create Screen Annotation
    screen_annotation = ann.ScreenAnnotation(
        document.pages[1],
        ap.Rectangle(170, 190, 470, 380),
        media_file
    )

    # Add the annotation to the page
    document.pages[1].annotations.append(screen_annotation)

    # Save PDF document
    document.save(data_dir + "AddScreenAnnotationWithMedia_out.pdf")    

def run_all_examples(data_dir=None, license_path=None):
    """Run adding extra annotations examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Add Watermark Annotation", watermark_add, ["sample.pdf", "output_watermark_add.pdf"]),
        ("Get Watermark Annotation", watermark_get, ["sample.pdf", "output_watermark_get.pdf"]),
        ("Delete Watermark Annotation", watermark_delete, ["sample.pdf", "output_watermark_delete.pdf"]),
        ("Add 3D Annotation", add_3d_annotation, ["sample.pdf", "output_3d_add.pdf"]),
        ("Add Screen Annotation with Media", add_screen_annotation_with_media, ["sample.pdf", "output_screen_annotation.pdf"])


    ]

    for name, func, args in examples:
        input_file_name = path.join(input_dir, args[0])
        output_file_name = path.join(output_dir, args[1])
        try:
            if (len(args)>2):
                func(input_file_name, output_file_name, args[2])
            else:
                func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
