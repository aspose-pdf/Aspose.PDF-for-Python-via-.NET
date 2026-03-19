import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

class ViewerPreference(IntFlag):
	"""Bit flags for PDF viewer preferences."""

	PAGE_LAYOUT_SINGLE_PAGE = 1
	PAGE_LAYOUT_ONE_COLUMN = 2
	PAGE_LAYOUT_TWO_COLUMN_LEFT = 4
	PAGE_LAYOUT_TWO_COLUMN_RIGHT = 8

	PAGE_MODE_USE_NONE = 16
	PAGE_MODE_USE_OUTLINES = 32
	PAGE_MODE_USE_THUMBS = 64
	PAGE_MODE_FULL_SCREEN = 128

	HIDE_TOOLBAR = 256
	HIDE_MENUBAR = 512
	HIDE_WINDOW_UI = 1024
	FIT_WINDOW = 2048
	CENTER_WINDOW = 4096

	NON_FULL_SCREEN_PAGE_MODE_USE_NONE = 8192
	NON_FULL_SCREEN_PAGE_MODE_USE_OUTLINES = 16384
	NON_FULL_SCREEN_PAGE_MODE_USE_THUMBS = 32768

	DIRECTION_L2R = 65536
	DIRECTION_R2L = 131072

	DISPLAY_DOC_TITLE = 262144
	NON_FULL_SCREEN_PAGE_MODE_USE_OC = 524288	
	PAGE_MODE_USE_OC = 1048576
	PAGE_MODE_USE_ATTACHMENT = 2097152

	SIMPLEX = 4194304
	DUPLEX_FLIP_SHORT_EDGE = 8388608
	DUPLEX_FLIP_LONG_EDGE = 16777216
	PRINT_SCALING_APP_DEFAULT = 1 << 25
	PRINT_SCALING_NONE = 1 << 26
	PICK_TRAY_BY_PDF_SIZE = 1 << 27



def get_viewer_preferences(infile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)
	# Read current viewer preference flags
	viewer_preference = ViewerPreference(content_editor.get_viewer_preference())
	if viewer_preference & ViewerPreference.PAGE_MODE_USE_OUTLINES:
		print("PageModeUseOutlines is enabled")
	print(f"Current viewer preference: {viewer_preference}")


def change_viewer_preferences(infile, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)

	current_preference = ViewerPreference(content_editor.get_viewer_preference())
	# Toggle one low-order flag to demonstrate viewer preference update
	updated_preference = current_preference | ViewerPreference.PAGE_LAYOUT_SINGLE_PAGE
	content_editor.change_viewer_preference(int(updated_preference))

	# Save updated document
	content_editor.save(outfile)


def run_all_examples(data_dir=None, license_path=None):
	"""Run all viewer preference examples and report status."""
	set_license(license_path)
	input_dir, output_dir = initialize_data_dir(data_dir)

	examples = [
		("Get Viewer Preferences", get_viewer_preferences),
		("Change Viewer Preferences", change_viewer_preferences),
	]

	for name, func in examples:
		try:
			if func.__name__ == "get_viewer_preferences":
				func(path.join(input_dir, f"{func.__name__}.pdf"))
			else:
				func(path.join(input_dir, f"{func.__name__}.pdf"),
					 path.join(output_dir, f"{func.__name__}.pdf"))
			print(f"✅ Success: {name}")
		except Exception as e:
			print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
	run_all_examples()