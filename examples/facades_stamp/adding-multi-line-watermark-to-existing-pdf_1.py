# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\stamp\adding-multi-line-watermark-to-existing-pdf
# Code fence language: python


import aspose.pdf as pdf
import System
from System.Drawing import Color

def add_text_stamp_to_pdf():
    # Instantiate a Stamp object
    logo_stamp = pdf.facades.Stamp()

    # Create a FormattedText object (first line)
    formatted_text = pdf.facades.FormattedText(
        "Hello World!",
        Color.FromArgb(180, 0, 0),                 # Semi-transparent red
        pdf.facades.FontStyle.TimesItalic,         # Font style
        pdf.facades.EncodingType.Winansi,          # Encoding
        False,                                     # Embedded font
        50                                         # Font size
    )

    # Add another line to the stamp
    formatted_text.add_new_line_text("Good Luck")

    # Bind formatted text to the stamp
    logo_stamp.bind_logo(formatted_text)

    return logo_stamp
