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

## Repository Constraints

- Python 3.7+ source style
- Allowed dependencies are limited to the repo requirements
- Do not introduce a test framework just for examples
- Do not redesign folder structure when a focused example change will do

## Output Expectations

- Generated output names should remain descriptive and stable
- Prefer `{function_name}_out.pdf` when producing a single canonical PDF output
- Status lines should remain easy to scan from the console
