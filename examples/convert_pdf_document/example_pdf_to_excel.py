from os import path
import aspose.pdf as ap
import sys

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import initialize_data_dir, set_license


def convert_pdf_to_excel_spread_sheet2003(infile, outfile):
    """
    Convert PDF to Excel 2003 XML SpreadSheet format.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output XLS filename

    Returns:
        None

    Example:
        convert_pdf_to_excel_spread_sheet2003("sample.pdf", "sample_python.xls")
    """
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_pdf_to_excel_2007(infile, outfile):
    """
    Convert PDF to Excel 2007 XLSX format.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output XLSX filename

    Returns:
        None

    Example:
        convert_pdf_to_excel_2007("sample.pdf", "sample_python.xlsx")
    """
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_pdf_to_excel_2007_control_column(infile, outfile):
    """
    Convert PDF to Excel 2007 with blank column insertion.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output XLSX filename

    Returns:
        None

    Example:
        convert_pdf_to_excel_2007_control_column("sample.pdf", "sample_python.xlsx")

    Note:
        Inserts blank column at first position in output.
    """

    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_pdf_to_excel_2007_single_excel_worksheet(infile, outfile):
    """
    Convert PDF to Excel 2007 minimizing worksheets.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output XLSX filename

    Returns:
        None

    Example:
        convert_pdf_to_excel_2007_single_excel_worksheet("sample.pdf", "sample_python.xlsx")

    Note:
        Minimizes the number of worksheets in output file.
    """
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_pdf_to_excel_2007_macro(infile, outfile):
    """
    Convert PDF to Excel 2007 Macro-Enabled format.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output XLSM filename

    Returns:
        None

    Example:
        convert_pdf_to_excel_2007_macro("sample.pdf", "sample_python.xlsm")
    """

    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_pdf_to_excel_2007_csv(infile, outfile):
    """
    Convert PDF to CSV format.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output CSV filename

    Returns:
        None

    Example:
        convert_pdf_to_excel_2007_csv("sample.pdf", "sample_python.csv")
    """

    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.CSV
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def convert_pdf_to_ods(infile, outfile):
    """
    Convert PDF to ODS (OpenDocument Spreadsheet) format.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output ODS filename

    Returns:
        None

    Example:
        convert_pdf_to_ods("sample.pdf", "sample_python.ods")
    """

    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.ODS
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)


def run_all_examples(data_dir=None, license_path=None):
    """Run PDF to Excel examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    input_dir, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "PDF to Excel 2003",
            convert_pdf_to_excel_spread_sheet2003,
            "sample_python.xls",
        ),
        ("PDF to Excel 2007", convert_pdf_to_excel_2007, "sample_python.xlsx"),
        (
            "PDF to Excel with column",
            convert_pdf_to_excel_2007_control_column,
            "sample_python.xlsx",
        ),
        (
            "PDF to Excel single sheet",
            convert_pdf_to_excel_2007_single_excel_worksheet,
            "sample_python.xlsx",
        ),
        ("PDF to Excel Macro", convert_pdf_to_excel_2007_macro, "sample_python.xlsm"),
        ("PDF to CSV", convert_pdf_to_excel_2007_csv, "sample_python.csv"),
        ("PDF to ODS", convert_pdf_to_ods, "sample_python.ods"),
    ]

    for name, func, o in examples:
        infile = path.join(input_dir, "sample.pdf")
        outfile = path.join(output_dir, o)
        try:
            func(infile, outfile)
            print(f"✅ Success: {name}")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")


if __name__ == "__main__":

    run_all_examples()
