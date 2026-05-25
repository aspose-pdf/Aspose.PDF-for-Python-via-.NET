import os
import shutil
from pathlib import Path


def clean_directory_contents(directory: Path) -> None:
    """Remove all files and subdirectories within the given directory."""
    for item in directory.iterdir():
        try:
            if item.is_file() or item.is_symlink():
                item.unlink()
                print(f"  Deleted file: {item}")
            elif item.is_dir():
                shutil.rmtree(item)
                print(f"  Deleted directory: {item}")
        except Exception as e:
            print(f"  Error deleting {item}: {e}")


def clean_output_folders(base_path):
    """Scan for 'output' folders and remove all files inside them."""
    base = Path(base_path)

    if not base.exists():
        print(f"Path does not exist: {base}")
        return

    for root, dirs, _ in os.walk(base):
        if "output" in dirs:
            output_path = Path(root) / "output"
            print(f"Cleaning: {output_path}")

            try:
                clean_directory_contents(output_path)
            except Exception as e:
                print(f"  Error cleaning {output_path}: {e}")


if __name__ == "__main__":
    clean_output_folders("sample_data")
    print("Done!")