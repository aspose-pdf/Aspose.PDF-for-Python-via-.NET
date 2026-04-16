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
        ("add_sound_annotation", add_sound_annotation),
        ("get_multimedia_annotations", get_multimedia_annotations),
        ("delete_rich_media_annotations", delete_rich_media_annotations),
        ("add_rich_media_annotation", add_rich_media_annotation)

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
