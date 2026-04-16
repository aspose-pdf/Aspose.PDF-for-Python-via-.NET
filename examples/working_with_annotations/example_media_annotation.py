import sys
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
from os import path


sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def add_rich_media_annotation():
    # The path to the documents directory
    data_dir = "path/to/your/data/"
    path_to_adobe_app = r"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins"

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Define media files
    video_name = "file_example_MP4_480_1_5MG.mp4"
    poster_name = "file_example_MP4_480_1_5MG_poster.jpg"
    skin_name = "SkinOverAllNoFullNoCaption.swf"

    # Create RichMediaAnnotation
    rma = ann.RichMediaAnnotation(
        page,
        ap.Rectangle(100, 500, 300, 600)
    )

    # Set custom player (SWF)
    player_path = os.path.join(path_to_adobe_app, "Players", "Videoplayer.swf")
    rma.custom_player = open(player_path, "rb")

    # Flash variables
    rma.custom_flash_variables = f"source={video_name}&skin={skin_name}"

    # Add skin
    skin_path = os.path.join(path_to_adobe_app, skin_name)
    rma.add_custom_data(skin_name, open(skin_path, "rb"))

    # Set poster image
    poster_path = os.path.join(data_dir, poster_name)
    rma.set_poster(open(poster_path, "rb"))

    # Set video content
    video_path = os.path.join(data_dir, video_name)
    with open(video_path, "rb") as fs:
        rma.set_content(video_name, fs)

    # Set content type
    rma.type = ann.RichMediaAnnotation.ContentType.video

    # Activate on click
    rma.activate_on = ann.RichMediaAnnotation.ActivationEvent.click

    # Update annotation
    rma.update()

    # Add annotation to the page
    page.annotations.append(rma)

    # Save PDF document
    document.save(data_dir + "RichMediaAnnotation_out.pdf")


def delete_rich_media_annotations():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Open PDF document
    document = ap.Document(data_dir + "RichMediaAnnotation.pdf")

    page = document.pages[1]

    # Collect RichMedia annotations
    to_delete = [
        a for a in page.annotations
        if a.annotation_type == ann.AnnotationType.rich_media
    ]

    # Delete annotations
    for annotation in to_delete:
        page.annotations.delete(annotation)

    # Save PDF document
    document.save(data_dir + "DeletePolyAnnotation_out.pdf")

def get_multimedia_annotations():
    # The path to the documents directory
    data_dir = "path/to/your/data/"

    # Open PDF document
    document = ap.Document(data_dir + "RichMediaAnnotation.pdf")

    # Target annotation types
    target_types = {
        ann.AnnotationType.screen,
        ann.AnnotationType.sound,
        ann.AnnotationType.rich_media
    }

    # Iterate through annotations on the first page
    for annotation in document.pages[1].annotations:
        if annotation.annotation_type in target_types:
            print(f"{annotation.annotation_type} [{annotation.rect}]")  

def annotation_3d_add():
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

def add_sound_annotation():
    # Path to documents directory
    data_dir = "path/to/your/data/"

    # Open PDF document
    document = ap.Document(data_dir + "sample.pdf")
    page = document.pages[1]

    media_file = data_dir + "file_example_WAV_1MG.wav"

    # Create Sound Annotation
    sound_annotation = ap.annotations.SoundAnnotation(
        page,
        ap.Rectangle(20, 700, 60, 740),
        media_file
    )

    sound_annotation.color = ap.Color.blue
    sound_annotation.title = "John Smith"
    sound_annotation.subject = "Sound Annotation demo"

    # Popup annotation
    sound_annotation.popup = ap.annotations.PopupAnnotation(
        page,
        ap.Rectangle(20, 700, 60, 740)
    )

    # Add annotation to page
    page.annotations.append(sound_annotation)

    # Save PDF document
    document.save(data_dir + "AddSoundAnnotation_out.pdf")


if __name__ == "__main__":
    add_sound_annotation()


def run_all_examples(data_dir=None, license_path=None):
    """Run all media annotation examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("sound_annotation_add", add_sound_annotation),
        ("multimedia_annotations_get", get_multimedia_annotations),
        ("rich_media_annotations_delete", delete_rich_media_annotations),
        ("rich_media_annotations_add", add_rich_media_annotation),
        ("3d_annotation_add", annotation_3d_add),
        ("screen_annotation_with_media_add", add_screen_annotation_with_media)

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
