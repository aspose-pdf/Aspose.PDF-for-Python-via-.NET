import aspose.pdf as ap
from aspose.pycore import *
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import initialize_data_dir, set_license


# region Extract Tagged Content from PDF
def get_tagged_content(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Work with Tagged PDF content
        # Set Title and Language for Document
        tagged_content.set_title("Simple Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Save Tagged PDF Document
        document.save(outfile)


def get_root_structure(outfile):

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Properties StructTreeRootElement and RootElement are used for access to
        # StructTreeRoot object of pdf document and to root structure element (Document structure element).
        struct_tree_root_element = tagged_content.struct_tree_root_element
        root_element = tagged_content.root_element


def access_child_elements(infile, outfile):

    # Open PDF Document
    with ap.Document(infile) as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Access to root element(s)
        element_list = tagged_content.struct_tree_root_element.child_elements

        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = cast(ap.logical_structure.StructureElement, element)

                # Get properties
                title = structure_element.title
                language = structure_element.language
                actual_text = structure_element.actual_text
                expansion_text = structure_element.expansion_text
                alternative_text = structure_element.alternative_text

        # Access to child elements of first element in root element
        element_list = tagged_content.root_element.child_elements[1].child_elements
        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = element

                # Set properties
                structure_element.title = "title"
                structure_element.language = "fr-FR"
                structure_element.actual_text = "actual text"
                structure_element.expansion_text = "exp"
                structure_element.alternative_text = "alt"

        # Save Tagged PDF Document
        document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run Extract Tagged Content examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "Get Tagged Content",
            get_tagged_content,
            [path.join(output_dir, "tagged_pdf_content.pdf")],
        ),
        (
            "Get Root Structure",
            get_root_structure,
            [path.join(output_dir, "root_structure.pdf")],
        ),
        (
            "Access Child Elements",
            access_child_elements,
            [
                path.join(input_dir, "StructureElementsTree.pdf"),
                path.join(output_dir, "access_child_elements.pdf"),
            ],
        ),
    ]

    for name, func, args in examples:
        try:
            func(*args)
            print(f"✅ Success: {name} completed.")

        except Exception as e:
            print(f"❌ Failed: {name} - {e}")

    print(f"\nAll Extract Tagged Content examples finished. Check output in {output_dir}")


if __name__ == "__main__":
    run_all_examples()
