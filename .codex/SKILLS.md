# Local Codex Skills

This repository now uses small, task-focused skills instead of one monolithic skill document.

## Skills

- `pdf-operations`
  - Purpose: Aspose.PDF operation patterns, API hints, and example behavior rules.
  - File: `.codex/skills/pdf-operations/SKILL.md`
- `code-style`
  - Purpose: Shared formatting, file layout, naming, path, and error-handling conventions.
  - File: `.codex/skills/code-style/SKILL.md`
- `spec-generator`
  - Purpose: Generate or refresh machine-readable example specs and scaffold new example files.
  - File: `.codex/skills/spec-generator/SKILL.md`

## Suggested Combinations

- New example implementation:
  - `pdf-operations` + `code-style`
- Refactor or normalize an existing example:
  - `pdf-operations` + `code-style`
- Refresh generated repository metadata/specs:
  - `spec-generator`
- Add a new example and keep generated specs in sync:
  - `pdf-operations` + `code-style` + `spec-generator`

## Scripts

- `python scripts/generate_example_specs.py`
  - Scans `examples/` and refreshes generated spec artifacts under `specs/examples/`
- `python scripts/generate_example_stub.py --category <category> --name <slug> --operation <function_name>`
  - Scaffolds a new example file using the repo's standard template

## Generated Artifacts

- `specs/examples/index.json`
- `specs/examples/index.md`

Treat those files as generated outputs. Re-run the generator after adding or materially changing example modules.
