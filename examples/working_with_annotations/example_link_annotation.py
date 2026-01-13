from os import path
import aspose.pdf as ap
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import set_license, initialize_data_dir

def link_add(infile, outfile):
    """
    Add a link annotation to the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> link_add("sample.pdf", "output.pdf")

    Note:
        This function finds the text "file" on the first page and creates a link annotation
        that navigates to www.aspose.com when clicked.
    """
    document = ap.Document(infile)
    # Create TextFragmentAbsorber object to find a phone number
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Accept the absorber for the 1st page only
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Create Link Annotation and set the action to call a phone number
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Add annotation to page
    document.pages[1].annotations.append(linkAnnotation)
    document.save(outfile)


def link_get(infile, outfile):
    """
    Retrieve and print the rectangle coordinates of all link annotations on the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file (not used in this function).

    Returns:
        None

    Example:
        >>> link_get("sample.pdf", "output.pdf")

    Note:
        This function prints the rectangle coordinates of all link annotations found on the first page.
    """
    document = ap.Document(infile)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)    


def link_delete(infile, outfile):
    """
    Delete all link annotations from the first page of a PDF document.

    Args:
        infile (str): The name of the input PDF file.
        outfile (str): The name of the output PDF file.

    Returns:
        None

    Example:
        >>> link_delete("sample.pdf", "output.pdf")

    Note:
        This function removes all link annotations from the first page and saves the modified PDF.
    """
    document = ap.Document(infile)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(outfile)
    

def run_all_examples(data_dir=None, license_path=None):
    """Run adding link annotations examples and report status.

    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("link_add", link_add),
        ("link_get", link_get),
        ("link_delete", link_delete),
    ]

    for name, func in examples:
        input_file_name = path.join(input_dir, "Annotations.pdf")
        output_file_name = path.join(output_dir, f"{func.__name__}_out.pdf")
        try:
            func(input_file_name, output_file_name)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

if __name__ == "__main__":
    run_all_examples()
