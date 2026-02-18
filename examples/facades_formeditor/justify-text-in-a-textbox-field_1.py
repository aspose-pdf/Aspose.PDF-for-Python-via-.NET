from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def justify_text_in_textbox_field(infile, outfile):
    # Create Form object
    form = pdf_facades.Form()

    # Bind PDF document
    form.bind_pdf(infile)

    # Fill text field
    form.fill_field("Last Name", "Thank you for using Aspose")

    # Save PDF document into memory stream
    form.save(ms)
    ms.Seek(0, SeekOrigin.Begin)

    # Create destination file stream
    dest = FileStream(os.path.join(data_dir, "JustifyText_out.pdf"), FileMode.Create)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()

    # Open PDF from memory stream
    form_editor.bind_pdf(ms)

    # Set text alignment to Justified
    form_editor.Facade.Alignment = pdf_facades.FormFieldFacade.AlignJustified

    # Decorate the form field
    form_editor.DecorateField()

    # Save updated PDF
    form_editor.save(dest)

    # Dispose resources
    source.Close()
    ms.Close()
    dest.Close()
    form.Dispose()
    form_editor.Dispose()

    print("Text field filled and justified successfully.")
