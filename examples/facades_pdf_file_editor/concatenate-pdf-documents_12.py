# Extracted from: _index.md
# Source folder: E:\Github\Aspose.PDF-Documentation\en\python-net\working-with-facades\pdffileeditor\concatenate-pdf-documents
# Code fence language: python


import aspose.pdf as ap
from aspose.pdf.facades import (
    PdfFileEditor,
    PdfFileStamp,
    PdfContentEditor,
    PdfFileInfo,
    Stamp,
    FormattedText
)
from io import BytesIO


def minimal_toc_sample():
    data_dir = "./"  # <-- путь к PDF

    input1 = data_dir + "ConcatenateInput1.pdf"
    input2 = data_dir + "ConcatenateInput2.pdf"
    output = data_dir + "result_with_toc.pdf"

    # --- 1. Concatenate PDFs into memory ---
    editor = PdfFileEditor()
    concat_stream = BytesIO()

    with open(input1, "rb") as f1, open(input2, "rb") as f2:
        editor.concatenate(f1, f2, concat_stream)

    concat_stream.seek(0)

    # --- 2. Load as Document and insert TOC page ---
    doc = ap.Document(concat_stream)
    doc.pages.insert(1)

    doc_stream = BytesIO()
    doc.save(doc_stream)
    doc_stream.seek(0)

    # --- 3. Add TOC text using stamps ---
    stampper = PdfFileStamp()
    stampper.bind_pdf(doc_stream)

    title = Stamp()
    title.bind_logo(
        FormattedText(
            "Table of Contents",
            ap.Color.black,
            ap.Color.transparent,
            ap.FontStyle.Helvetica,
            ap.EncodingType.Winansi,
            True,
            18
        )
    )
    title.set_origin(200, 750)
    title.pages = [1]
    stampper.add_stamp(title)

    item1 = Stamp()
    item1.bind_logo(
        FormattedText(
            "1. First document",
            ap.Color.black,
            ap.Color.transparent,
            ap.FontStyle.Helvetica,
            ap.EncodingType.Winansi,
            False,
            12
        )
    )
    item1.set_origin(200, 700)
    item1.pages = [1]
    stampper.add_stamp(item1)

    item2 = Stamp()
    item2.bind_logo(
        FormattedText(
            "2. Second document",
            ap.Color.black,
            ap.Color.transparent,
            ap.FontStyle.Helvetica,
            ap.EncodingType.Winansi,
            False,
            12
        )
    )
    item2.set_origin(200, 670)
    item2.pages = [1]
    stampper.add_stamp(item2)

    stamped_stream = BytesIO()
    stampper.save(stamped_stream)
    stampper.close()
    stamped_stream.seek(0)

    # --- 4. Create local links ---
    content = PdfContentEditor()
    content.bind_pdf(stamped_stream)

    # Link to first document (starts at page 2)
    content.create_local_link(
        ap.Rectangle(200, 700, 350, 720),
        2,
        1,
        ap.Color.transparent
    )

    first_doc_pages = PdfFileInfo(input1).number_of_pages

    # Link to second document
    content.create_local_link(
        ap.Rectangle(200, 670, 350, 690),
        first_doc_pages + 2,
        1,
        ap.Color.transparent
    )

    content.save(output)
    content.close()


if __name__ == "__main__":
    minimal_toc_sample()
