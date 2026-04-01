from __future__ import annotations

import argparse
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES_ROOT = REPO_ROOT / "examples"


TEMPLATE = """import sys
from os import path

import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), '..'))
from config import set_license, initialize_data_dir


def {operation_name}(infile, outfile):
    \"\"\"Run the {operation_name} example.

    Args:
        infile (str): Input PDF path.
        outfile (str): Output PDF path.

    Returns:
        None
    \"\"\"
    document = ap.Document(infile)
    document.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
    \"\"\"Run all examples in this module.\"\"\"
    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (\"{display_name}\", {operation_name}, \"{input_file}\", \"{output_file}\"),
    ]

    for name, func, infile_name, outfile_name in examples:
        try:
            infile = path.join(input_dir, infile_name)
            outfile = path.join(output_dir, outfile_name)
            print(f\"Running: {{name}}\")
            func(infile, outfile)
            print(f\"✅ Success: {{name}}\")
        except Exception as exc:
            print(f\"❌ Failed: {{name}} - {{exc}}\")


if __name__ == \"__main__\":
    run_all_examples()
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a new example module skeleton.")
    parser.add_argument("--category", required=True, help="Category folder under examples/")
    parser.add_argument("--name", required=True, help="Module slug without the example_ prefix")
    parser.add_argument("--operation", required=True, help="Primary operation function name")
    parser.add_argument(
        "--input-file",
        default="input.pdf",
        help="Default input file name referenced by run_all_examples()",
    )
    parser.add_argument(
        "--output-file",
        default=None,
        help="Default output file name. Defaults to <operation>_out.pdf",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite an existing file")
    return parser


def main() -> None:
    args = build_parser().parse_args()

    category_dir = EXAMPLES_ROOT / args.category
    category_dir.mkdir(parents=True, exist_ok=True)

    output_file = args.output_file or f"{args.operation}_out.pdf"
    target_path = category_dir / f"example_{args.name}.py"

    if target_path.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite existing file: {target_path}")

    content = TEMPLATE.format(
        operation_name=args.operation,
        display_name=args.operation.replace("_", " ").title(),
        input_file=args.input_file,
        output_file=output_file,
    )
    target_path.write_text(content, encoding="utf-8")

    print(f"Created {target_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
