import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_rubber_stamp(infile, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)
	
	for i in range(1, 5):
		content_editor.create_rubber_stamp(
			i,
			apd.Rectangle(120, 450, 180, 60),
			"Approved",
			"Approved by reviewer",
			apd.Color.green,
		)
	# Save updated document
	content_editor.save(outfile)


def delete_stamp_by_index(infile, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)
	content_editor.delete_stamp(1, [2,3])
	# Save updated document
	content_editor.save(outfile)


def manage_stamp_by_id(infile, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)

	content_editor.create_rubber_stamp(
		1,
		apd.Rectangle(200, 380, 180, 60),
		"Draft",
		"Draft stamp for ID-based operations",
		apd.Color.orange,
	)

	content_editor.create_rubber_stamp(
		2,
		apd.Rectangle(200, 480, 180, 60),
		"Draft",
		"Draft stamp for ID-based operations",
		apd.Color.orange,
	)

	# Apply ID-based stamp operations
	content_editor.hide_stamp_by_id(1, 1)
	content_editor.show_stamp_by_id(1, 2)
	
	# Save updated document
	content_editor.save(outfile)


def delete_stamp_by_ids_examples(infile, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)

	# Create two stamps on page 1 so they can be deleted by ID
	content_editor.create_rubber_stamp(
		1,
		apd.Rectangle(120, 320, 180, 60),
		"Draft",
		"Delete by single ID",
		apd.Color.orange,
	)
	content_editor.create_rubber_stamp(
		1,
		apd.Rectangle(120, 250, 180, 60),
		"Draft",
		"Delete by multiple IDs",
		apd.Color.orange,
	)

	# Delete by single ID overload and by IDs overload
	content_editor.delete_stamp_by_id(1, 1)
	content_editor.delete_stamp_by_ids(1, [2])

	# Save updated document
	content_editor.save(outfile)


def move_stamp_by_index(infile, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)

	content_editor.create_rubber_stamp(
		2,
		apd.Rectangle(200, 380, 180, 60),
		"Draft",
		"Draft stamp for ID-based operations",
		apd.Color.orange,
	)

	content_editor.create_rubber_stamp(
		2,
		apd.Rectangle(200, 480, 180, 60),
		"Draft",
		"Draft stamp for ID-based operations",
		apd.Color.orange,
	)
	content_editor.save(outfile)

	# Move first stamp on page 1 by index
	# content_editor.move_stamp(1, 1, 10, 10)
	# Save updated document
	content_editor.save(outfile)


def move_stamp_by_id_example(infile, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)

	content_editor.create_rubber_stamp(
		1,
		apd.Rectangle(300, 420, 180, 60),
		"Approved",
		"Move this stamp by ID",
		apd.Color.green,
	)

	# Move stamp by ID overload
	content_editor.move_stamp_by_id(1, 1, 240, 360)

	# Save updated document
	content_editor.save(outfile)


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)
	# Create rubber stamp using appearance_file overload (image path)
	content_editor.create_rubber_stamp(
		1,
		apd.Rectangle(100, 400, 200, 60),
		"Stamp with custom appearance",
		apd.Color.dark_green,
		image_file,
	)
	# Save updated document
	content_editor.save(outfile)


def create_rubber_stamp_with_appearance_stream(infile, image_file, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)
	# Read image into an in-memory stream
	with open(image_file, "rb") as src:
		appearance_stream = BytesIO(src.read())
	# Create rubber stamp using appearance_stream overload
	content_editor.create_rubber_stamp(
		1,
		apd.Rectangle(100, 320, 200, 60),
		"Stamp with appearance stream",
		apd.Color.dark_green,
		appearance_stream,
	)
	# Save updated document
	content_editor.save(outfile)


def delete_stamps_globally(infile, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)

	# Add stamps across multiple pages so global deletion is meaningful
	for page in range(1, 5):
		content_editor.create_rubber_stamp(
			page,
			apd.Rectangle(120, 500, 180, 60),
			"Draft",
			"Stamp for global deletion",
			apd.Color.gray,
		)

	# delete_stamp_by_id without page number removes stamp ID from all pages
	content_editor.delete_stamp_by_id(1)
	# delete_stamp_by_ids without page number removes a list of IDs from all pages
	content_editor.delete_stamp_by_ids([2, 3])

	# Save updated document
	content_editor.save(outfile)


def list_stamps(infile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)
	# List all stamps on page 1
	stamps = content_editor.get_stamps(1)

	count = 0
	for stamp in stamps:
		count += 1
		print(f"Stamp {count}: {stamp}")

	if count == 0:
		print("No stamps found")


def run_all_examples(data_dir=None, license_path=None):
	"""Run all stamp examples and report status."""
	set_license(license_path)
	input_dir, output_dir = initialize_data_dir(data_dir)

	examples = [
		("Add Rubber Stamp", add_rubber_stamp),
		("Delete Stamp By Index", delete_stamp_by_index),
		("Manage Stamp By ID", manage_stamp_by_id),
		("Delete Stamp By IDs", delete_stamp_by_ids_examples),
		("Move Stamp By Index", move_stamp_by_index),
		("Move Stamp By ID", move_stamp_by_id_example),
		("Create Rubber Stamp With Appearance File", create_rubber_stamp_with_appearance_file),
		("Create Rubber Stamp With Appearance Stream", create_rubber_stamp_with_appearance_stream),
		("Delete Stamps Globally", delete_stamps_globally),
		("List Stamps", list_stamps),
	]

	image_file = path.join(input_dir, "replacement_image.jpg")

	for name, func in examples:
		try:
			if func.__name__ == "list_stamps":
				func(path.join(input_dir, f"{func.__name__}.pdf"))
			elif func.__name__ in (
				"create_rubber_stamp_with_appearance_file",
				"create_rubber_stamp_with_appearance_stream",
			):
				func(
					path.join(input_dir, "sample4pages.pdf"),
					image_file,
					path.join(output_dir, f"{func.__name__}.pdf"),
				)
			else:
				func(path.join(input_dir, f"sample4pages.pdf"),
					 path.join(output_dir, f"{func.__name__}.pdf"))
			print(f"✅ Success: {name}")
		except Exception as e:
			print(f"❌ Failed: {name} - {str(e)}")


if __name__ == "__main__":
	run_all_examples()
