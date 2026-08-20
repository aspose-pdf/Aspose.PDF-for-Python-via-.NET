import os
import sys


def initialize_data_dir(data_dir=None):
    """
    Initialize and create data directories for input and output files.
    This function creates a directory structure for storing input and output data files.
    If no data_dir is provided, it attempts to locate a 'sample_data' directory by finding
    the 'examples' folder in the current script's path and replacing it accordingly.
    Args:
        data_dir (str, optional): The base directory path where input and output folders
            will be created. If None, the function will automatically determine the path
            based on the script location. Defaults to None.
    Returns:
        tuple: A tuple containing two strings (input_dir, output_dir):
            - input_dir (str): Path to the created input directory
            - output_dir (str): Path to the created output directory
    Raises:
        OSError: If any of the required directories (base, input, or output) cannot be created.
    Example:
        >>> input_path, output_path = initialize_data_dir()
        >>> print(input_path)
        '/path/to/sample_data/input'
        >>> print(output_path)
        '/path/to/sample_data/output'
        >>> input_path, output_path = initialize_data_dir('/custom/data/path')
        >>> print(input_path)
        '/custom/data/path/input'
    """
    if data_dir is None:
        script_dir = os.path.dirname(os.path.abspath(sys.modules["__main__"].__file__))
        # Find the last occurrence of "examples" in the path and replace it with "sample_data"
        parts = script_dir.split(os.sep)
        if "examples" in parts:
            idx = len(parts) - 1 - parts[::-1].index("examples")
            sample_data_path = os.sep.join(
                parts[:idx] + ["sample_data"] + parts[idx + 1 :]
            )
            dir_path = sample_data_path
        else:
            dir_path = script_dir
    else:
        dir_path = data_dir

    try:
        os.makedirs(dir_path, exist_ok=True)
    except OSError as e:
        raise OSError(f"Failed to create directory '{dir_path}': {e}") from e

    try:
        input_dir = os.path.join(dir_path, "input")
        os.makedirs(input_dir, exist_ok=True)
    except OSError as e:
        raise OSError(f"Failed to create directory '{input_dir}': {e}") from e

    try:
        output_dir = os.path.join(dir_path, "output")
        os.makedirs(output_dir, exist_ok=True)
    except OSError as e:
        raise OSError(f"Failed to create directory '{output_dir}': {e}") from e

    return (input_dir, output_dir)


def set_license(license_path=None):
    """Optionally set Aspose.PDF license from a file path.

    Args:
      license_path (str, optional): Path to the Aspose license file.
    Returns:
      None
    Example:
      >>> set_license(r"C:\\Secret\\Aspose.Total.lic")
    Note:
      Skip or pass ``None`` to use evaluation mode.
    """
    import aspose.pdf as ap

    if license_path:
        if not os.path.exists(license_path):
            raise FileNotFoundError(f"License file not found: {license_path}")

        try:
            lic = ap.License()
            lic.set_license(license_path)
        except Exception as e:
            raise Exception(f"Failed to set license: {e}")
