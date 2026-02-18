# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdfannotationeditor\delete-annotations
# Code fence language: python


import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades

def delete_annotation_by_name():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "DeleteAllAnnotations.pdf"))

    # Display the list of annotations on the first page
    for idx, ann in enumerate(document.Pages[1].Annotations, start=1):
        print(f"{idx}. {ann.Name} {ann.AnnotationType}")

    # Prompt the user to enter the index of the annotation to delete
    choice = int(input("Please enter number: "))

    # Create an instance of PdfAnnotationEditor
    annotation_editor = pdf_facades.PdfAnnotationEditor()

    # Bind PDF document
    annotation_editor.bind_pdf(document)

    # Delete the annotation selected by the user
    selected_annotation_name = document.Pages[1].Annotations[choice].Name
    annotation_editor.DeleteAnnotation(selected_annotation_name)

    # Save updated PDF document
    annotation_editor.save(os.path.join(data_dir, "DeleteAnnotationByName_out.pdf"))

    # Dispose resources
    annotation_editor.Dispose()
    document.Dispose()

    print(f"Annotation '{selected_annotation_name}' deleted successfully.")
