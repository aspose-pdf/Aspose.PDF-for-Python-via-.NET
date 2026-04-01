---
name: code-style
description: Apply shared repository style rules for Aspose.PDF Python example files, including structure, naming, path handling, docstrings, status output, and error handling.
metadata:
  short-description: Shared style rules for example scripts
  version: "1.0"
---

# Code Style

## Use This Skill When

- Creating or refactoring repository example scripts
- Normalizing older examples to the current house style
- Reviewing whether generated code matches repository conventions

## Structure Rules

- Keep the import block simple and consistent
- Always use:
  - `from os import path`
  - `sys.path.append(path.join(path.dirname(__file__), '..'))`
- Use following snippet in `facades` subfolder examples:
  ```python
  from os import path
  import sys

  CURRENT_DIR = path.dirname(__file__)
  EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
  if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)
  ```
- Import shared helpers from `examples/config.py`
- Preserve `run_all_examples()` as the entrypoint

## Function Rules

- Operation functions must accept file paths as `str`
- Do not pass `Document` objects between functions
- Use descriptive names tied to the actual action
- Keep one function responsible for one operation

## Path Rules

- Use `path.join(...)` for repository-local paths
- Do not hardcode absolute paths
- Use `initialize_data_dir(...)` instead of hand-rolling sample-data locations

## Error Handling And Output

- Wrap each example run in `try/except`
- Do not stop the full example run because one case failed
- Preserve the repository's success/failure markers:
  - `✅ Success`
  - `❌ Failed`

## Documentation

- Add or preserve concise docstrings on public example functions
- Prefer docstrings with `Args` and `Returns` when the function is non-trivial
- Keep comments brief and useful

## Anti-Patterns

- Hardcoded file system paths
- Breaking `run_all_examples()`
- Removing status prints
- Adding dependencies not already used by the repo
- Large architectural rewrites for narrow example changes
