---
name: spec-generator
description: Generate and maintain repository example specs and example scaffolding artifacts for Aspose.PDF for Python via .NET.
metadata:
  short-description: Example spec generation workflow
  version: "1.0"
---

# Spec Generator

## Use This Skill When

- Refreshing machine-readable metadata for the example catalog
- Generating repo documentation from the current `examples/` tree
- Scaffolding a new example file with the standard repository template
- Keeping Codex-facing specs aligned with the actual source tree

## Pipeline Entry Points

- Refresh generated specs:
  - `python scripts/generate_example_specs.py`
- Scaffold a new example:
  - `python scripts/generate_example_stub.py --category <category> --name <slug> --operation <function_name>`

## Generated Outputs

- `specs/examples/index.json`
- `specs/examples/index.md`

These artifacts should be deterministic so they can be regenerated after source changes.

## Generator Expectations

- Scan `examples/` recursively
- Ignore generated caches and `examples/config.py`
- Extract stable metadata from Python source
- Preserve sorted output for low-noise diffs
- Fail loudly on invalid Python modules instead of silently producing partial garbage

## Integration Rules

- After adding or materially changing an example module, refresh specs before closing the task
- Prefer updating generator scripts instead of hand-editing generated spec artifacts
- Keep scaffolded examples aligned with the `pdf-operations` and `code-style` skills
