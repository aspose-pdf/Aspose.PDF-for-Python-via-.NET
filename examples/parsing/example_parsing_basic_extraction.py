import aspose.pdf as ap
from os import path
import sys

sys.path.append(path.join(path.dirname(__file__), ".."))
from config import set_license, initialize_data_dir


def extract_text_from_all_pages(infile, outfile):
    """
    Extract all text from every page of the PDF and write to an output text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    # Open the PDF document
    document = ap.Document(infile)
    # Create a TextAbsorber to extract text
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber for all pages
    document.pages.accept(text_absorber)
    # Get extracted text
    extracted_text = text_absorber.text
    # Write the text to an output file
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)


def extract_text_from_page(infile, outfile, page_number):
    """
    Extract text from a specific page number of the PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1-based page index to extract.
    """
    document = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    # Accept the absorber on only the specified page
    document.pages[page_number].accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)


def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraph’s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)

    absorber = ap.text.ParagraphAbsorber()
    absorber.visit(document)

    with open(outfile, "w", encoding="utf-8") as tw:
        for page_markup in absorber.page_markups:
            for sec_idx, section in enumerate(page_markup.sections, start=1):
                for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                    # Concatenate all fragments/lines in the paragraph
                    parts = []
                    for line in paragraph.lines:
                        for fragment in line:
                            parts.append(fragment.text)
                        parts.append("\r\n")
                    paragraph_text = "".join(parts)
                    tw.write(
                        f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n"
                    )
                    tw.write(paragraph_text + "\n")


def run_all_examples(data_dir=None, license_path=None):
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "extract_text_from_all_pages",
            extract_text_from_all_pages,
            "sample.pdf",
            "sample.txt",
            None,
        ),
        (
            "extract_text_from_page",
            extract_text_from_page,
            "sample.pdf",
            "extract_text_from_page.txt",
            1,
        ),
        (
            "extract_paragraphs_from_pdf",
            extract_paragraphs_from_pdf,
            "sample.pdf",
            "extract_paragraphs_from_pdf.txt",
            None,
        ),
    ]

    for name, func, input_file, output_file, page_num in examples:
        try:
            args = [
                path.join(input_dir, input_file),
                path.join(output_dir, output_file),
            ]
            if page_num:
                args.append(page_num)
            func(*args)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":
    run_all_examples()
