import os
from pathlib import Path

def clean_output_folders(base_path):
    """Scan for 'output' folders and remove all files inside them."""
    base = Path(base_path)

    if not base.exists():
        print(f"Path does not exist: {base}")
        return

    for root, dirs, files in os.walk(base):
        if 'output' in dirs:
            output_path = Path(root) / 'output'
            print(f"Cleaning: {output_path}")

            try:
                for item in output_path.iterdir():
                    if item.is_file():
                        item.unlink()
                        print(f"  Deleted: {item.name}")
            except Exception as e:
                print(f"  Error cleaning {output_path}: {e}")

if __name__ == "__main__":
    clean_output_folders("sample_data")
    print("Done!")