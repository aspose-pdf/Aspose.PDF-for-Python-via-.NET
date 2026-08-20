---
name: pdf-operations
description: Implement or update Aspose.PDF for Python via .NET example logic, including opening, saving, merging, splitting, protecting, converting, and related document operations.
metadata:
  short-description: Aspose.PDF example operation guidance
  version: "1.0"
---

# PDF Operations

## Use This Skill When

- Creating a new example script for a PDF feature
- Updating example logic that touches Aspose.PDF APIs
- Translating a request like merge, split, encrypt, convert, annotate, extract, or optimize into repository code

## Required Behavior

- Operate on file paths, not shared `Document` objects passed between functions
- Keep one public operation function focused on one concrete behavior
- Preserve `run_all_examples()` as the execution entrypoint
- Keep examples runnable in evaluation mode when no license is supplied

## Standard Structure

Every example should align with this flow:

1. Import `aspose.pdf as ap`
2. Append the parent examples directory with:
   `sys.path.append(path.join(path.dirname(__file__), '..'))`
3. Import `set_license` and `initialize_data_dir` from `config`
4. Implement one or more operation functions accepting string paths
5. Implement `run_all_examples(data_dir=None, license_path=None)`
6. Call `set_license(...)` and `initialize_data_dir(...)`
7. Execute examples with per-example `try/except`

For nested example folders, adjust the shared-config import path to match the real directory depth. For example, files under `examples/facades/pdf_content_editor/` can use:

```python
CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import set_license, initialize_data_dir
```

## API Reference

- Open document:
  - `ap.Document(path)`
  - `ap.Document(path, password)`
- Save document:
  - `document.save(path)`
- Merge:
  - `doc1.pages.add(doc2.pages)`
- Encrypt:
  - `document.encrypt(user_pwd, owner_pwd, privileges, algorithm, False)`
- Convert:
  - `document.convert(log_path, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)`

## Facades

Use facade APIs when the repository already demonstrates a task through `aspose.pdf.facades` rather than the core `Document` API. In these examples, the operation function should still accept file paths, but the implementation can create and bind a facade object internally.

### Shared Facade Pattern

For content-editor style examples:

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd

def operation_name(infile, outfile):
    content_editor = pdf_facades.PdfContentEditor()
    content_editor.bind_pdf(infile)
    # perform facade operation
    content_editor.save(outfile)
```

### Facade Rules

- Keep facade object creation inside the operation function
- Bind with `bind_pdf(infile)` before mutating content
- Save with the facade object after the operation is complete
- Use `aspose.pydrawing` geometry and colors when the facade API requires rectangles or color values
- Preserve one function per concrete operation even when multiple operations share the same facade class

### PdfContentEditor Examples

Text annotation:

```python
def add_text_annotation(infile, outfile):
    content_editor = pdf_facades.PdfContentEditor()
    content_editor.bind_pdf(infile)
    content_editor.create_text(
        apd.Rectangle(100, 400, 50, 50),
        "Text Annotation",
        "This is a text annotation",
        True,
        "Insert",
        1,
    )
    content_editor.save(outfile)
```

Free text annotation:

```python
def add_free_text_annotation(infile, outfile):
    content_editor = pdf_facades.PdfContentEditor()
    content_editor.bind_pdf(infile)
    content_editor.create_free_text(
        apd.Rectangle(200, 480, 150, 25),
        "This is a free text annotation",
        1,
    )
    content_editor.save(outfile)
```

Caret annotation:

```python
def add_caret_annotation(infile, outfile):
    content_editor = pdf_facades.PdfContentEditor()
    content_editor.bind_pdf(infile)
    content_editor.create_caret(
        1,
        apd.Rectangle(350, 400, 10, 10),
        apd.Rectangle(300, 380, 115, 15),
        "P",
        "This is a caret annotation",
        apd.Color.red,
    )
    content_editor.save(outfile)
```

Markup annotation variants:

```python
def add_markup_annotation(infile, outfile):
    content_editor = pdf_facades.PdfContentEditor()
    content_editor.bind_pdf(infile)
    content_editor.create_markup(
        apd.Rectangle(120, 440, 200, 20),
        "This is a highlight annotation",
        0,
        1,
        apd.Color.yellow,
    )
    content_editor.create_markup(
        apd.Rectangle(110, 542, 200, 20),
        "This is a underline annotation",
        1,
        1,
        apd.Color.yellow,
    )
    content_editor.save(outfile)
```

Popup annotation:

```python
def add_popup_annotation(infile, outfile):
    content_editor = pdf_facades.PdfContentEditor()
    content_editor.bind_pdf(infile)
    content_editor.create_popup(
        apd.Rectangle(220, 520, 180, 80),
        "This is a popup annotation",
        True,
        1,
    )
    content_editor.save(outfile)
```

### When To Prefer Facades

- The existing repo examples for that feature already use `aspose.pdf.facades`
- The API is centered on editor-style helpers such as content editing, file security, file info, or signatures
- The operation is naturally modeled as bind -> mutate -> save rather than load `Document` -> traverse object model -> save

## Repository Constraints

- Python 3.7+ source style
- Allowed dependencies are limited to the repo requirements
- Do not introduce a test framework just for examples
- Do not redesign folder structure when a focused example change will do

## Output Expectations

- Generated output names should remain descriptive and stable
- Prefer `{function_name}_out.pdf` when producing a single canonical PDF output
- Status lines should remain easy to scan from the console
