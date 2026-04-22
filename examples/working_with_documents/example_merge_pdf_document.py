import sys
import aspose.pdf as ap
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir


def merge_two_documents(infile1, infile2, outfile):
    """Merge two PDF documents into a single output document.

    This operation opens two input PDF files, appends all pages from the
    second document to the first, and saves the merged result to the
    specified output file.

    Args:
        infile1 (str): Path to the first input PDF document. Pages from
            this document will appear first in the merged output.
        infile2 (str): Path to the second input PDF document. All pages
            from this document are appended to ``infile1``.
        outfile (str): Path where the merged PDF document will be saved.

    Returns:
        None

    Examples:
        Merge two sample documents and save the result::

            from os import path
            from working_with_documents.example_merge_pdf_document import merge_two_documents

            input_dir = "sample_data/input"
            output_dir = "sample_data/output"

            infile1 = path.join(input_dir, "sample1.pdf")
            infile2 = path.join(input_dir, "sample3.pdf")
            outfile = path.join(output_dir, "sample_merge.pdf")

            merge_two_documents(infile1, infile2, outfile)
    """
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)


def _append_page_range(source_document, destination_document, start_page, end_page):
    total_pages = len(source_document.pages)
    if total_pages == 0:
        return

    start = max(1, start_page)
    end = min(end_page, total_pages)
    if start > end:
        return

    for page_number in range(start, end + 1):
        destination_document.pages.add(source_document.pages[page_number])


def merge_multiple_documents(input_files, outfile):
    """Merge multiple input PDF documents into one output PDF.

    Args:
        input_files (list[str]): Ordered list of PDF file paths to merge.
        outfile (str): Path where the merged PDF will be saved.
    Returns:
        None
    """
    output_document = ap.Document()

    for input_file in input_files:
        source_document = ap.Document(input_file)
        _append_page_range(source_document, output_document, 1, len(source_document.pages))

    output_document.save(outfile)


def merge_selected_page_ranges(infile1, infile2, outfile):
    """Merge selected page ranges from two PDF documents.

    This example appends pages 1-2 from the first document, then pages 2-3
    from the second document. Ranges are clamped to available page counts.

    Args:
        infile1 (str): Path to first input PDF.
        infile2 (str): Path to second input PDF.
        outfile (str): Path where the merged PDF will be saved.
    Returns:
        None
    """
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    _append_page_range(document1, output_document, 1, 2)
    _append_page_range(document2, output_document, 2, 3)

    output_document.save(outfile)


def merge_insert_document_at_position(infile1, infile2, insert_after_page, outfile):
    """Insert one document into another after a given page index.

    Args:
        infile1 (str): Base PDF file path.
        infile2 (str): PDF file path to insert into the base document.
        insert_after_page (int): Insert after this 1-based page number.
        outfile (str): Path where the merged PDF will be saved.
    Returns:
        None
    """
    base_document = ap.Document(infile1)
    insert_document = ap.Document(infile2)
    output_document = ap.Document()

    base_total_pages = len(base_document.pages)
    insert_index = max(0, min(insert_after_page, base_total_pages))

    _append_page_range(base_document, output_document, 1, insert_index)
    _append_page_range(insert_document, output_document, 1, len(insert_document.pages))
    _append_page_range(base_document, output_document, insert_index + 1, base_total_pages)

    output_document.save(outfile)


def merge_alternating_pages(infile1, infile2, outfile):
    """Merge two documents by alternating pages from each source.

    If page counts differ, remaining pages from the longer document are
    appended at the end in their original order.

    Args:
        infile1 (str): Path to first input PDF.
        infile2 (str): Path to second input PDF.
        outfile (str): Path where the merged PDF will be saved.
    Returns:
        None
    """
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    document1_pages = len(document1.pages)
    document2_pages = len(document2.pages)
    max_pages = max(document1_pages, document2_pages)

    for page_number in range(1, max_pages + 1):
        if page_number <= document1_pages:
            output_document.pages.add(document1.pages[page_number])
        if page_number <= document2_pages:
            output_document.pages.add(document2.pages[page_number])

    output_document.save(outfile)


def merge_with_section_separators_and_bookmarks(input_files, outfile):
    """Merge documents with separator pages and section bookmarks.

    A separator page is inserted before each source document. A top-level
    section bookmark points to the separator page, and a child bookmark
    points to the first content page of that merged section.

    Args:
        input_files (list[str]): Ordered list of PDF file paths to merge.
        outfile (str): Path where the merged PDF will be saved.
    Returns:
        None
    """
    output_document = ap.Document()

    for section_index, input_file in enumerate(input_files, start=1):
        source_document = ap.Document(input_file)
        source_page_count = len(source_document.pages)

        separator_page = output_document.pages.add()
        separator_page.paragraphs.add(
            ap.text.TextFragment(f"Section {section_index}: {path.basename(input_file)}")
        )

        section_bookmark = ap.OutlineItemCollection(output_document.outlines)
        section_bookmark.title = f"Section {section_index}"
        section_bookmark.action = ap.annotations.GoToAction(separator_page)
        output_document.outlines.append(section_bookmark)

        first_content_page_number = len(output_document.pages) + 1
        _append_page_range(source_document, output_document, 1, source_page_count)

        if source_page_count > 0 and first_content_page_number <= len(output_document.pages):
            content_bookmark = ap.OutlineItemCollection(output_document.outlines)
            content_bookmark.title = f"Section {section_index} Content"
            content_bookmark.action = ap.annotations.GoToAction(
                output_document.pages[first_content_page_number]
            )
            section_bookmark.append(content_bookmark)

    output_document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run Merge Document examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Merge two documents", merge_two_documents, "sample_merge_two_documents.pdf"),
        ("Merge multiple documents", merge_multiple_documents, "sample_merge_multiple_documents.pdf"),
        ("Merge selected page ranges", merge_selected_page_ranges, "sample_merge_selected_ranges.pdf"),
        ("Merge with inserted document", merge_insert_document_at_position, "sample_merge_insert_position.pdf"),
        ("Merge alternating pages", merge_alternating_pages, "sample_merge_alternating_pages.pdf"),
        (
            "Merge with section separators and bookmarks",
            merge_with_section_separators_and_bookmarks,
            "sample_merge_sections_bookmarks.pdf",
        ),
    ]

    for name, func, output_file in examples:
        try:
            input_file_name1 = path.join(input_dir, "sample1.pdf")
            input_file_name2 = path.join(input_dir, "sample3.pdf")
            input_file_name3 = path.join(input_dir, "sample2.pdf")
            output_file_name = path.join(output_dir, output_file)

            if func is merge_multiple_documents:
                func([input_file_name1, input_file_name2, input_file_name3], output_file_name)
            elif func is merge_with_section_separators_and_bookmarks:
                func([input_file_name1, input_file_name2, input_file_name3], output_file_name)
            elif func is merge_insert_document_at_position:
                func(input_file_name1, input_file_name2, 2, output_file_name)
            else:
                func(input_file_name1, input_file_name2, output_file_name)

            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

    print("\nAll Merge Document examples finished.")


if __name__ == "__main__":
    run_all_examples()
