# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfannotationeditor\delete-annotations
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def delete_all_annotation_by_type():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "DeleteAllAnnotations.pdf"))

    # Collect all annotation types from all pages
    annotation_types = []
    for page in document.Pages:
        if page.Annotations is None:
            continue
        # Retrieve each annotation type from the page
        for ann in page.Annotations:
            annotation_types.append(str(ann.AnnotationType))

    # Make the list of annotation types distinct
    annotation_types = list(set(annotation_types))

    # Display each annotation type to the user
    for idx, ann_type in enumerate(annotation_types, start=1):
        print(f"{idx}. {ann_type}")

    # Prompt user to choose the annotation type to delete
    choice = int(input("Please enter number: ")) - 1
    selected_type = annotation_types[choice]

    # Create an instance of PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.bind_pdf(document)

    # Delete the annotation selected by the user
    annotation_editor.DeleteAnnotations(selected_type)

    # Save updated PDF document
    annotation_editor.save(os.path.join(data_dir, "DeleteAllAnnotationByType_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()
    document.Dispose()

    print(f"All annotations of type '{selected_type}' deleted successfully.")
