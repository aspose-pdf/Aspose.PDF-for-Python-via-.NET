import aspose.pdf as ap
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from config import initialize_data_dir, set_license


# region Working with Table in Tagged PDFs
def create_table(outfile):

    # Create PDF document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        tagged_content.set_title("Example table")
        tagged_content.set_language("en-US")

        # Get root structure element
        root_element = tagged_content.root_element

        table_element = tagged_content.create_table_element()
        root_element.append_child(table_element, True)

        table_element.border = ap.BorderInfo(ap.BorderSide.ALL, 1.2, ap.Color.dark_blue)

        table_t_head_element = table_element.create_t_head()
        table_t_body_element = table_element.create_t_body()
        table_t_foot_element = table_element.create_t_foot()
        row_count = 50
        col_count = 4

        head_tr_element = table_t_head_element.create_tr()
        head_tr_element.alternative_text = "Head Row"
        head_tr_element.background_color = ap.Color.light_gray

        for column_index in range(col_count):
            th_element = head_tr_element.create_th()
            th_element.set_text(f"Head {column_index}")

            th_element.background_color = ap.Color.green_yellow
            th_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)

            th_element.is_no_border = True
            th_element.margin = ap.MarginInfo(16.0, 2.0, 8.0, 2.0)

            th_element.alignment = ap.HorizontalAlignment.RIGHT

        for row_index in range(row_count):
            tr_element = table_t_body_element.create_tr()
            tr_element.alternative_text = f"Row {row_index}"

            for column_index in range(col_count):
                col_span = 1
                row_span = 1

                if column_index == 1 and row_index == 1:
                    col_span = 2
                    row_span = 2
                elif column_index == 2 and (row_index == 1 or row_index == 2):
                    continue
                elif row_index == 2 and (column_index == 1 or column_index == 2):
                    continue

                td_element = tr_element.create_td()
                td_element.set_text(f"Cell [{row_index}, {column_index}]")

                td_element.background_color = ap.Color.yellow
                td_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)

                td_element.is_no_border = False
                td_element.margin = ap.MarginInfo(8.0, 2.0, 8.0, 2.0)

                td_element.alignment = ap.HorizontalAlignment.CENTER

                cell_text_state = ap.text.TextState()
                cell_text_state.foreground_color = ap.Color.dark_blue
                cell_text_state.font_size = 7.5
                cell_text_state.font_style = ap.text.FontStyles.BOLD
                cell_text_state.font = ap.text.FontRepository.find_font("Arial")
                td_element.default_cell_text_state = cell_text_state

                td_element.is_word_wrapped = True
                td_element.vertical_alignment = ap.VerticalAlignment.CENTER

                td_element.col_span = col_span
                td_element.row_span = row_span

        foot_tr_element = table_t_foot_element.create_tr()
        foot_tr_element.alternative_text = "Foot Row"
        foot_tr_element.background_color = ap.Color.light_sea_green

        for column_index in range(col_count):
            td_element = foot_tr_element.create_td()
            td_element.set_text(f"Foot {column_index}")

            td_element.alignment = ap.HorizontalAlignment.CENTER
            td_element.structure_text_state.font_size = 7
            td_element.structure_text_state.font_style = ap.text.FontStyles.BOLD

        table_attributes = table_element.attributes.get_attributes(
            ap.logicalstructure.AttributeOwnerStandard.TABLE
        )
        summary_attribute = ap.logicalstructure.StructureAttribute(
            ap.logicalstructure.AttributeKey.SUMMARY
        )
        summary_attribute.set_string_value("The summary text for table")
        table_attributes.set_attribute(summary_attribute)

        # Save Tagged PDF Document
        document.save(outfile)


def style_table(outfile):

    # Create PDF document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        tagged_content.set_title("Example table style")
        tagged_content.set_language("en-US")

        # Get root structure element
        root_element = tagged_content.root_element

        # Create table structure element
        table_element = tagged_content.create_table_element()
        root_element.append_child(table_element, True)

        table_element.background_color = ap.Color.beige
        table_element.border = ap.BorderInfo(ap.BorderSide.ALL, 0.80, ap.Color.gray)
        table_element.alignment = ap.HorizontalAlignment.CENTER
        table_element.broken = ap.TableBroken.VERTICAL
        table_element.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW
        table_element.column_widths = "80 80 80 80 80"
        table_element.default_cell_border = ap.BorderInfo(
            ap.BorderSide.ALL, 0.50, ap.Color.dark_blue
        )
        table_element.default_cell_padding = ap.MarginInfo(16.0, 2.0, 8.0, 2.0)
        table_element.default_cell_text_state.foreground_color = ap.Color.dark_cyan
        table_element.default_cell_text_state.font_size = 8.0
        table_element.default_column_width = "70"

        table_element.is_broken = False
        table_element.is_borders_included = True

        table_element.left = 0.0
        table_element.top = 40.0

        table_element.repeating_columns_count = 2
        table_element.repeating_rows_count = 3
        row_style = ap.text.TextState()
        row_style.background_color = ap.Color.light_coral
        table_element.repeating_rows_style = row_style

        table_t_head_element = table_element.create_t_head()
        table_t_body_element = table_element.create_t_body()
        table_t_foot_element = table_element.create_t_foot()
        row_count = 10
        col_count = 5

        head_tr_element = table_t_head_element.create_tr()
        head_tr_element.alternative_text = "Head Row"

        for col_index in range(col_count):
            th_element = head_tr_element.create_th()
            th_element.set_text(f"Head {col_index}")

        for row_index in range(row_count):
            tr_element = table_t_body_element.create_tr()
            tr_element.alternative_text = f"Row {row_index}"

            for col_index in range(col_count):
                td_element = tr_element.create_td()
                td_element.set_text(f"Cell [{row_index}, {col_index}]")

        foot_tr_element = table_t_foot_element.create_tr()
        foot_tr_element.alternative_text = "Foot Row"

        for col_index in range(col_count):
            td_element = foot_tr_element.create_td()
            td_element.set_text(f"Foot {col_index}")

        # Save Tagged PDF Document
        document.save(outfile)


def style_table_row(outfile):
    # Create PDF document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        tagged_content.set_title("Example table style")
        tagged_content.set_language("en-US")

        # Get root structure element
        root_element = tagged_content.root_element

        # Create table structure element
        table_element = tagged_content.create_table_element()
        root_element.append_child(table_element, True)
        table_t_head_element = table_element.create_t_head()
        table_t_body_element = table_element.create_t_body()
        table_t_foot_element = table_element.create_t_foot()
        row_count = 7
        col_count = 3
        head_tr_element = table_t_head_element.create_tr()
        head_tr_element.alternative_text = "Head Row"
        for col_index in range(col_count):
            th_element = head_tr_element.create_th()
            th_element.set_text("Head {}".format(col_index))
        for row_index in range(row_count):
            tr_element = table_t_body_element.create_tr()
            tr_element.alternative_text = "Row {}".format(row_index)
            tr_element.background_color = ap.Color.light_goldenrod_yellow
            tr_element.border = ap.BorderInfo(
                ap.BorderSide.ALL, 0.75, ap.Color.dark_gray
            )
            tr_element.default_cell_border = ap.BorderInfo(
                ap.BorderSide.ALL, 0.50, ap.Color.blue
            )
            tr_element.min_row_height = 100.0
            tr_element.fixed_row_height = 120.0
            tr_element.is_in_new_page = row_index % 3 == 1
            tr_element.is_row_broken = True

            cell_text_state = ap.text.TextState()
            cell_text_state.foreground_color = ap.Color.red
            tr_element.default_cell_text_state = cell_text_state
            tr_element.default_cell_padding = ap.MarginInfo(16.0, 2.0, 8.0, 2.0)
            tr_element.vertical_alignment = ap.VerticalAlignment.BOTTOM
            for col_index in range(col_count):
                td_element = tr_element.create_td()
                td_element.set_text("Cell [{0}, {1}]".format(row_index, col_index))

        foot_tr_element = table_t_foot_element.create_tr()
        foot_tr_element.alternative_text = "Foot Row"

        for col_index in range(col_count):
            td_element = foot_tr_element.create_td()
            td_element.set_text("Foot {}".format(col_index))

        # Save Tagged PDF Document
        document.save(outfile)


def style_table_cell(outfile):

    # Create PDF document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        tagged_content.set_title("Example table cell style")
        tagged_content.set_language("en-US")

        # Get root structure element
        root_element = tagged_content.root_element

        # Create table structure element
        table_element = tagged_content.create_table_element()
        root_element.append_child(table_element, True)

        table_t_head_element = table_element.create_t_head()
        table_t_body_element = table_element.create_t_body()
        table_t_foot_element = table_element.create_t_foot()
        row_count = 4
        col_count = 4

        head_tr_element = table_t_head_element.create_tr()
        head_tr_element.alternative_text = "Head Row"

        for col_index in range(col_count):
            th_element = head_tr_element.create_th()
            th_element.set_text("Head {}".format(col_index))

            th_element.background_color = ap.Color.green_yellow
            th_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)

            th_element.is_no_border = True
            th_element.margin = ap.MarginInfo(16.0, 2.0, 8.0, 2.0)

            th_element.alignment = ap.HorizontalAlignment.RIGHT

        for row_index in range(row_count):
            tr_element = table_t_body_element.create_tr()
            tr_element.alternative_text = "Row {}".format(row_index)

            for col_index in range(col_count):
                col_span = 1
                row_span = 1

                if col_index == 1 and row_index == 1:
                    col_span = 2
                    row_span = 2
                elif col_index == 2 and (row_index == 1 or row_index == 2):
                    continue
                elif row_index == 2 and (col_index == 1 or col_index == 2):
                    continue

                td_element = tr_element.create_td()
                td_element.set_text("Cell [{}, {}]".format(row_index, col_index))

                td_element.background_color = ap.Color.yellow
                td_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)

                td_element.is_no_border = False
                td_element.margin = ap.MarginInfo(8.0, 2.0, 8.0, 2.0)

                td_element.alignment = ap.HorizontalAlignment.CENTER

                cell_text_state = ap.text.TextState()
                cell_text_state.foreground_color = ap.Color.dark_blue
                cell_text_state.font_size = 7.5
                cell_text_state.font_style = ap.text.FontStyles.BOLD
                cell_text_state.font = ap.text.FontRepository.find_font("Arial")
                td_element.default_cell_text_state = cell_text_state

                td_element.is_word_wrapped = True
                td_element.vertical_alignment = ap.VerticalAlignment.CENTER

                td_element.col_span = col_span
                td_element.row_span = row_span

        foot_tr_element = table_t_foot_element.create_tr()
        foot_tr_element.alternative_text = "Foot Row"

        for col_index in range(col_count):
            td_element = foot_tr_element.create_td()
            td_element.set_text("Foot {}".format(col_index))

        # Save Tagged PDF Document
        document.save(outfile)

def adjust_table_position(outfile):

    # Create PDF document
    with ap.Document() as document:
        # Create tagged content
        tagged_content = document.tagged_content
        tagged_content.set_title("Example table cell style")
        tagged_content.set_language("en-US")

        # Get root structure element
        root_element = tagged_content.root_element

        # Create table structure element
        table_element = tagged_content.create_table_element()
        root_element.append_child(table_element, True)

        # Create position settings
        position_settings = ap.tagged.PositionSettings()
        position_settings.horizontal_alignment = ap.HorizontalAlignment.NONE
        position_settings.margin = ap.MarginInfo(left=20, right=0, top=0, bottom=0)
        position_settings.vertical_alignment = ap.VerticalAlignment.NONE
        position_settings.is_first_paragraph_in_column = False
        position_settings.is_kept_with_next = False
        position_settings.is_in_new_page = False
        position_settings.is_in_line_paragraph = False

        # Adjust table position
        table_element.adjust_position(position_settings)

        table_t_head_element = table_element.create_t_head()
        table_t_body_element = table_element.create_t_body()
        table_t_foot_element = table_element.create_t_foot()
        row_count = 4
        col_count = 4

        head_tr_element = table_t_head_element.create_tr()
        head_tr_element.alternative_text = "Head Row"

        for col_index in range(col_count):
            th_element = head_tr_element.create_th()
            th_element.set_text(f"Head {col_index}")

            th_element.background_color = ap.Color.green_yellow
            th_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)

            th_element.is_no_border = True
            th_element.margin = ap.MarginInfo(16.0, 2.0, 8.0, 2.0)

            th_element.alignment = ap.HorizontalAlignment.RIGHT

        for row_index in range(row_count):
            tr_element = table_t_body_element.create_tr()
            tr_element.alternative_text = f"Row {row_index}"

            for col_index in range(col_count):
                col_span = 1
                row_span = 1

                if col_index == 1 and row_index == 1:
                    col_span = 2
                    row_span = 2
                elif col_index == 2 and (row_index == 1 or row_index == 2):
                    continue
                elif row_index == 2 and (col_index == 1 or col_index == 2):
                    continue

                td_element = tr_element.create_td()
                td_element.set_text(f"Cell [{row_index}, {col_index}]")

                td_element.background_color = ap.Color.yellow
                td_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)

                td_element.is_no_border = False
                td_element.margin = ap.MarginInfo(8.0, 2.0, 8.0, 2.0)

                td_element.alignment = ap.HorizontalAlignment.CENTER

                cell_text_state = ap.text.TextState()
                cell_text_state.foreground_color = ap.Color.dark_blue
                cell_text_state.font_size = 7.5
                cell_text_state.font_style = ap.text.FontStyles.BOLD
                cell_text_state.font = ap.text.FontRepository.find_font("Arial")
                td_element.default_cell_text_state = cell_text_state

                td_element.is_word_wrapped = True
                td_element.vertical_alignment = ap.VerticalAlignment.CENTER

                td_element.col_span = col_span
                td_element.row_span = row_span

        foot_tr_element = table_t_foot_element.create_tr()
        foot_tr_element.alternative_text = "Foot Row"

        for col_index in range(col_count):
            td_element = foot_tr_element.create_td()
            td_element.set_text(f"Foot {col_index}")

        # Save Tagged PDF Document
        document.save(outfile)


# endregion


def run_all_examples(data_dir=None, license_path=None):
    """Run Tagged Table examples and report status.
    Args:
        data_dir (str, optional): Input/output directory override.
        license_path (str, optional): Path to Aspose.PDF license file.
    Returns:
        None
    """

    set_license(license_path)
    _, output_dir = initialize_data_dir(data_dir)

    examples = [
        (
            "Create Table",
            create_table,
            "create_table.pdf",
        ),
        (
            "Style Table",
            style_table,
            "style_table.pdf",
        ),
        (
            "Style Table Row",
            style_table_row,
            "style_table_row.pdf",
        ),
        (
            "Style Table Cell",
            style_table_cell,
            "style_table_cell.pdf",
        ),
        (
            "Adjust Table Position",
            adjust_table_position,
            "adjust_table_position.pdf",
        ),
    ]

    for name, func, args in examples:
        try:
            output_file_name = path.join(output_dir, args)
            func(output_file_name)
            print(f"✅ Success: {name} completed.")
        except Exception as e:
            print(f"❌ Failed: {name} - {e}")

    print(f"\nAll Tagged Table examples finished. Check output in {output_dir}")


if __name__ == "__main__":
    run_all_examples()
