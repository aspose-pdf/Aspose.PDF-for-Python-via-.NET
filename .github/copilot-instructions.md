# Copilot Instructions for Aspose.PDF-for-Python-via-.NET

## Project Overview
This repository contains Python examples demonstrating the **Aspose.PDF for Python via .NET** library. The codebase is structured as an educational resource, providing working examples for common PDF operations like opening, saving, merging, splitting, and protecting PDF documents.

## Architecture & Structure

### Directory Layout
- `examples/`: Contains all example scripts organized by category
  - `basic_operations/`: Core PDF operations (open, save, merge, split, protect)
  - `config.py`: Shared configuration utilities for data directories and licensing
  - `requirements.txt`: Python dependencies (aspose-pdf, lxml, pydicom)
- `sample_data/`: Runtime directory for input/output PDFs (auto-created by config)
  - `input/`: Sample PDF files for testing examples
  - `output/`: Generated output files from examples

### Configuration System
All example scripts import from `examples/config.py` which provides:
- `initialize_data_dir(data_dir=None)`: Auto-creates `sample_data/{input,output}` directories by replacing "examples" with "sample_data" in the script path
- `set_license(license_path=None)`: Optional Aspose license activation (defaults to evaluation mode if omitted)

## Code Patterns

### Standard Example Structure
Every example file follows this template:

```python
import sys
from os import path
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), '..'))
from config import set_license, initialize_data_dir

def operation_function(infile, outfile):
    """Specific PDF operation implementation"""
    document = ap.Document(infile)
    # ... perform operations
    document.save(outfile)

def run_all_examples(data_dir=None, license_path=None):
    """Run all examples with status reporting"""
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        ("Example Name", function_name),
    ]

    for name, func in examples:
        try:
            # ... prepare paths and call function
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {str(e)}")

if __name__ == "__main__":
    run_all_examples()
```

### Key Conventions
- **Path resolution**: Use `sys.path.append(path.join(path.dirname(__file__), '..'))` to import from parent config
- **Status reporting**: Use ✅/❌ emoji prefixes for success/failure (not decorative, but functional output markers)
- **Function signatures**: Operation functions accept file paths as strings, not Document objects
- **Error handling**: Wrap example execution in try/except to report failures without stopping the suite

### PDF Operations
- **Opening**: `ap.Document(path)` or `ap.Document(path, password)` for encrypted PDFs
- **Saving**: `document.save(path)` or `document.save(stream)` for FileIO streams
- **Merging**: `doc1.pages.add(doc2.pages)` - pages collection is mutable
- **Encryption**: Use `document.encrypt(user_pwd, owner_pwd, privileges, algorithm, false)` with `ap.facades.DocumentPrivilege` and `ap.CryptoAlgorithm`
- **Conversion**: `document.convert(log_path, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)` before saving

## Development Workflows

### Running Examples
```bash
cd examples
pip install -r requirements.txt
python basic_operations/example_open.py
```

### Adding New Examples
1. Create new script in appropriate category directory (e.g., `basic_operations/`)
2. Import and call `set_license` + `initialize_data_dir` from config
3. Implement operation functions that accept file paths
4. Create `run_all_examples()` using the standard template with examples list
5. Add example to category README if it exists
6. Ensure input PDFs are placed in `sample_data/input/` with expected names

### Testing
No automated test suite exists. Examples are self-validating via try/except blocks and console output. Verify success by:
- Running `python examples/basic_operations/example_*.py`
- Checking for ✅ status indicators
- Inspecting generated files in `sample_data/output/`

## Critical Details

### Licensing
- Evaluation mode (no license): Adds watermarks and limits functionality
- Licensed mode: Call `set_license(r"C:\path\to\Aspose.Total.lic")` before operations
- License file path is optional in all `run_all_examples()` functions

### Sample Data Requirements
Examples expect specific input files:
- `example_open.py`: Requires `open_document_from_file.pdf`, `open_document_from_stream.pdf`, `open_document_encrypted.pdf`
- `example_save.py`: Requires `sample3.pdf`
- `example_merger.py`: Requires `sample1.pdf` and `sample2.pdf`
- `example_splitter.py`: Requires `sample_split.pdf`
- `example_protect.py`: Requires `sample3.pdf` initially, then uses generated protected files

### Python Requirements
- **Minimum**: Python 3.7+
- **Dependencies**: Only `aspose-pdf`, `lxml`, `pydicom` (see requirements.txt)
- **No virtual env specified**: Examples assume global Python environment or manual venv activation

## When Contributing Examples
- Follow the established `run_all_examples()` pattern for consistency
- Include comprehensive docstrings with Args/Returns/Examples (see `example_protect.py` for reference)
- Name functions descriptively (e.g., `encrypt_password`, `split_documents`)
- Use `path.join()` for cross-platform compatibility (repository targets Windows/Unix)
- Output files should use `{function_name}_out.pdf` naming convention
