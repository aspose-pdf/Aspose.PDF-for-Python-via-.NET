# Delete a Specific Annotation
# Delete All Annotations
# Delete Annotations by Type

from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Delete a Specific Annotation
def delete_specific_annotation(infile, outfile, annotation_id):

    pdf_annotation_editor = pdf_facades.PdfAnnotationEditor()
    pdf_annotation_editor.bind_pdf(infile)
    pdf_annotation_editor.delete_annotation(annotation_id)
    pdf_annotation_editor.save(outfile)

# Delete All Annotations
def delete_all_annotations(infile, outfile):

    pdf_annotation_editor = pdf_facades.PdfAnnotationEditor()
    pdf_annotation_editor.bind_pdf(infile)
    pdf_annotation_editor.delete_all_annotations()
    pdf_annotation_editor.save(outfile)

# Delete Annotations by Type
def delete_annotations_by_type(infile, outfile, annotation_type):
    pdf_annotation_editor = pdf_facades.PdfAnnotationEditor()
    pdf_annotation_editor.bind_pdf(infile)
    pdf_annotation_editor.delete_annotations_by_type(annotation_type)
    pdf_annotation_editor.save(outfile)