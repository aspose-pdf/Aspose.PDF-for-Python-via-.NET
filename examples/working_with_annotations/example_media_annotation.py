from os import path
import sys

import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


ann = ap.annotations


def rich_media_annotations_add(infile, outfile):
    """Add a rich media annotation using input media files from infile directory."""
    media_dir = path.dirname(infile)
    path_to_adobe_app = r"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins"

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    video_name = "file_example_MP4_480_1_5MG.mp4"
    poster_name = "file_example_MP4_480_1_5MG_poster.jpg"
    skin_name = "SkinOverAllNoFullNoCaption.swf"

    # Create RichMediaAnnotation
    rich_media_annotation = ann.RichMediaAnnotation(
        page,
        ap.Rectangle(100, 500, 300, 600, True),
    )

    # Set custom player and media assets
    player_path = path.join(path_to_adobe_app, "Players", "Videoplayer.swf")
    rich_media_annotation.custom_player = open(player_path, "rb")
    rich_media_annotation.custom_flash_variables = f"source={video_name}&skin={skin_name}"

    skin_path = path.join(path_to_adobe_app, skin_name)
    rich_media_annotation.add_custom_data(skin_name, open(skin_path, "rb"))

    poster_path = path.join(media_dir, poster_name)
    rich_media_annotation.set_poster(open(poster_path, "rb"))

    video_path = path.join(media_dir, video_name)
    with open(video_path, "rb") as video_file:
        rich_media_annotation.set_content(video_name, video_file)

    # Set type of the content (video)
    rich_media_annotation.type = ann.RichMediaAnnotation.ContentType.VIDEO

    # Activate player by click
    rich_media_annotation.activate_on = ann.RichMediaAnnotation.ActivationEvent.CLICK
    
    rich_media_annotation.update()

    page.annotations.append(rich_media_annotation)
    document.save(outfile)


def rich_media_annotations_delete(infile, outfile):
    """Delete all rich media annotations from page 1."""
    document = ap.Document(infile)
    page = document.pages[1]

    to_delete = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ann.AnnotationType.RICH_MEDIA
    ]

    for annotation in to_delete:
        page.annotations.delete(annotation)

    document.save(outfile)


def multimedia_annotations_get(infile, outfile):
    """Print screen/sound/rich-media annotation rectangles on page 1."""
    document = ap.Document(infile)

    target_types = {
        ann.AnnotationType.SCREEN,
        ann.AnnotationType.SOUND,
        ann.AnnotationType.RICH_MEDIA,
    }

    for annotation in document.pages[1].annotations:
        if annotation.annotation_type in target_types:
            print(f"{annotation.annotation_type} [{annotation.rect}]")


def annotation_3d_add(infile, outfile):
    """Create a PDF with a 3D annotation using U3D file from infile."""
    model_file = infile

    document = ap.Document()

    pdf3d_content = ann.PDF3DContent(model_file)
    pdf3d_artwork = ann.PDF3DArtwork(document, pdf3d_content)
    pdf3d_artwork.lighting_scheme = ann.PDF3DLightingScheme(ann.LightingSchemeType.CAD)
    pdf3d_artwork.render_mode = ann.PDF3DRenderMode(ann.RenderModeType.SOLID)

    top_matrix = ap.Matrix3D(
        1,
        0,
        0,
        0,
        -1,
        0,
        0,
        0,
        -1,
        0.10271,
        0.08184,
        0.273836,
    )

    front_matrix = ap.Matrix3D(
        0,
        -1,
        0,
        0,
        0,
        1,
        -1,
        0,
        0,
        0.332652,
        0.08184,
        0.085273,
    )

    pdf3d_artwork.view_array.add(
        ann.PDF3DView(document, top_matrix, 0.188563, "Top")
    )
    pdf3d_artwork.view_array.add(
        ann.PDF3DView(document, front_matrix, 0.188563, "Left")
    )

    page = document.pages.add()

    pdf3d_annotation = ann.PDF3DAnnotation(
        page,
        ap.Rectangle(100, 500, 300, 700, True),
        pdf3d_artwork,
    )

    pdf3d_annotation.border = ann.Border(pdf3d_annotation)
    pdf3d_annotation.set_default_view_index(1)
    pdf3d_annotation.flags = ann.AnnotationFlags.NO_ZOOM
    pdf3d_annotation.name = path.basename(model_file)

    page.annotations.append(pdf3d_annotation)
    document.save(outfile)


def screen_annotation_with_media_add(infile, outfile):
    """Add a screen annotation using a SWF media file from infile."""
    media_file = infile

    document = ap.Document()
    page = document.pages.add()

    screen_annotation = ann.ScreenAnnotation(
        page,
        ap.Rectangle(170, 190, 470, 380, True),
        media_file,
    )

    page.annotations.append(screen_annotation)
    document.save(outfile)


def sound_annotation_add(infile, outfile):
    """Add a sound annotation to page 1 using WAV file from infile directory."""
    media_dir = path.dirname(infile)

    document = ap.Document(infile)
    page = document.pages[1]

    media_file = path.join(media_dir, "file_example_WAV_1MG.wav")

    sound_annotation = ann.SoundAnnotation(
        page,
        ap.Rectangle(20, 700, 60, 740, True),
        media_file,
    )

    sound_annotation.color = ap.Color.blue
    sound_annotation.title = "John Smith"
    sound_annotation.subject = "Sound Annotation demo"

    sound_annotation.popup = ann.PopupAnnotation(
        page,
        ap.Rectangle(20, 700, 60, 740, True),
    )

    page.annotations.append(sound_annotation)
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run all media annotation examples and report status."""

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "sound_annotation_add",
            sound_annotation_add,
            (path.join(input_dir, "sample.pdf"), path.join(output_dir, "sound_annotation_add_out.pdf")),
        ),
        (
            "multimedia_annotations_get",
            multimedia_annotations_get,
            (path.join(input_dir, "RichMediaAnnotation.pdf"), path.join(output_dir, "multimedia_annotations_get_out.pdf")),
        ),
        (
            "rich_media_annotations_delete",
            rich_media_annotations_delete,
            (path.join(input_dir, "RichMediaAnnotation.pdf"), path.join(output_dir, "rich_media_annotations_delete_out.pdf")),
        ),
        (
            "rich_media_annotations_add",
            rich_media_annotations_add,
            (path.join(input_dir, "sample.pdf"), path.join(output_dir, "rich_media_annotations_add_out.pdf")),
        ),
        (
            "3d_annotation_add",
            annotation_3d_add,
            (path.join(input_dir, "Ring.u3d"), path.join(output_dir, "3d_annotation_add_out.pdf")),
        ),
        (
            "screen_annotation_with_media_add",
            screen_annotation_with_media_add,
            (path.join(input_dir, "input.swf"), path.join(output_dir, "screen_annotation_with_media_add_out.pdf")),
        ),
    ]

    for name, func, args in examples:
        try:
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
