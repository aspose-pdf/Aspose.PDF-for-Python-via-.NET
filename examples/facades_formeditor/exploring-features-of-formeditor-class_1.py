# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\formeditor\exploring-features-of-formeditor-class
# Code fence language: python


import os
import clr

# Add references to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Annotations import AnnotationFlags

def exploring_form_editor_features():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "inFile.pdf"))

    # Create instance of FormEditor
    editor = pdf_facades.FormEditor(document)

    # Add a text field
    editor.AddField(pdf_facades.FieldType.Text, "field1", 1, 300, 500, 350, 525)

    # Add a list box field
    editor.AddField(pdf_facades.FieldType.ListBox, "field2", 1, 300, 200, 350, 225)

    # Add list items
    editor.AddListItem("field2", "item 1")
    editor.AddListItem("field2", "item 2")

    # Add a submit button
    editor.AddSubmitBtn("submitbutton", 1, "Submit Form", "http://Testwebsite.com/testpage", 200, 200, 250, 225)

    # Delete a list item
    editor.DelListItem("field2", "item 1")

    # Move field to new position
    editor.MoveField("field1", 10, 10, 50, 50)

    # Remove existing field
    editor.RemoveField("field1")

    # Rename field
    editor.RenameField("field1", "newfieldname")

    # Reset all visual attributes
    editor.ResetFacade()

    # Set alignment style of a text field
    editor.SetFieldAlignment("field1", pdf_facades.FormFieldFacade.AlignLeft)

    # Set appearance of the field
    editor.SetFieldAppearance("field1", AnnotationFlags.NoRotate)

    # Set field attribute (e.g., ReadOnly)
    editor.SetFieldAttribute("field1", pdf_facades.PropertyFlag.ReadOnly)

    # Set field character limit
    editor.SetFieldLimit("field1", 25)

    # Save modifications
    editor.save(os.path.join(data_dir, "FormEditorFeatures2_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("FormEditor features demonstrated successfully.")
