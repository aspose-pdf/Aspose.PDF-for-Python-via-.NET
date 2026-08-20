# Aspose.PDF for Python via .NET Examples

This repository contains Python examples for [Aspose.PDF for Python via .NET](https://products.aspose.com/pdf/python-net) which will help you learn Aspose.PDF for Python via .NET and integrate it into your own projects.

<p align="center">
  <a title="Download Examples ZIP" href="https://github.com/aspose-pdf/Aspose.PDF-for-Python-via-.NET/archive/master.zip">
	<img src="https://raw.github.com/AsposeExamples/java-examples-dashboard/master/images/downloadZip-Button-Large.png" />
  </a>
</p>

| Folder | Description |
| --- | --- |
| [accessibility_tagged_pdf](accessibility_tagged_pdf) | Creating, editing, and extracting tagged PDF content for accessibility and PDF/UA workflows. |
| [basic_operations](basic_operations) | The first and simplest operation with PDF documents. To learn more about check out the following [Basic operations](https://docs.aspose.com/pdf/python-net/basic-operations/) page. |
| [attach_zugferd](attach_zugferd) | Working with Zugferd attachments in PDF documents. |
| [compare](compare) | Comparing and analyzing PDF documents. |
| [convert_pdf_document](convert_pdf_document) | Converting PDF documents to and from other formats. |
| [facades](facades) | Using Aspose.PDF Facades API for form editing, content editing, file operations, stamping, viewing, and signing workflows. |
| [get_started](get_started) | Introductory examples for creating and composing simple PDF documents. |
| [navigation_and_interaction](navigation_and_interaction) | Working with bookmarks, actions, and navigation elements in PDFs. |
| [parsing](parsing) | Extracting and parsing content from PDF documents. |
| [pdf_file_metadata](pdf_file_metadata) | Working with PDF document metadata and properties. |
| [working_with_annotations](working_with_annotations) | Adding, modifying, and working with annotations in PDFs. |
| [working_with_artifacts](working_with_artifacts) | Working with artifacts and page elements in PDFs. |
| [working_with_attachments](working_with_attachments) | Managing attachments and embedded files in PDFs. |
| [working_with_documents](working_with_documents) | Working with PDF document structure and settings. |
| [working_with_forms](working_with_forms) | Creating and working with PDF forms and form fields. |
| [working_with_graphs](working_with_graphs) | Working with graphs and drawing in PDFs. |
| [working_with_images](working_with_images) | Working with images in PDF documents. |
| [working_with_operators](working_with_operators) | Using operators for advanced PDF content manipulation. |
| [working_with_pages](working_with_pages) | Page operations and management. |
| [working_with_tables](working_with_tables) | Creating and working with tables in PDFs. |
| [working_with_text](working_with_text) | Text operations and manipulation in PDFs. |
| [working_with_vector_graphics](working_with_vector_graphics) | Working with vector graphics in PDFs. |

## How to Run the Examples?

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation Steps

1. **Clone or download the repository** to your local machine.

2. **Install dependencies** by running the following command in the examples directory:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the required packages including `aspose-pdf`.

### Running an Example

1. **Navigate to the examples directory**:

   ```bash
   cd examples
   ```

2. **Run a specific example** (e.g., basic_operations):

   ```bash
   python basic_operations/example_open.py
   ```

### Sample Data

The examples use sample files under the `sample_data` directory. The configuration module creates `input` and `output` folders relative to the example category being executed.

- **Input files**: `sample_data/<category>/input/`
- **Output files**: `sample_data/<category>/output/`

Example:

- Running `python basic_operations/example_open.py` uses `sample_data/basic_operations/input/` and `sample_data/basic_operations/output/`

### Running All Examples

To run a small set of examples, navigate to the examples directory and execute them one by one:

```bash
python basic_operations/example_open.py
python basic_operations/example_save.py
python basic_operations/example_merger.py
python basic_operations/example_splitter.py
python basic_operations/example_protect.py
```

To run all example scripts in the `examples` tree:

#### Windows (PowerShell)

```powershell
Get-ChildItem -Path . -Recurse -Filter "example_*.py" |
ForEach-Object {
   Write-Host "Running $($_.FullName)"
   python $_.FullName
}
```

#### macOS/Linux (bash)

```bash
find . -type f -name "example_*.py" -print0 |
while IFS= read -r -d '' file; do
   echo "Running $file"
   python "$file"
done
```

Note:

- Running all examples can take a long time.
- Some examples require specific input files in corresponding `sample_data/<category>/input/` directories.

### Troubleshooting

- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify that sample PDF files exist in the category-specific input directory (for example, `sample_data/basic_operations/input/`)
- Check that you have write permissions for the corresponding category-specific output directory
- Make sure you're running Python 3.7 or higher: `python --version`

## Code Style

Examples are formatted and linted with Ruff.

```bash
ruff check examples --fix
ruff format examples
```
