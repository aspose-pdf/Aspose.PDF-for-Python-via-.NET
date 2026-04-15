
# Python API to Process & Manipulate PDF Files

[Aspose.PDF for Python via .NET](https://products.aspose.com/pdf/python-net) is a Python wrapper that enables the developers to add PDF processing capabilities to their applications. It can be used to generate or read, convert and manipulate PDF files without the use of Adobe Acrobat.

Directory | Description
--------- | -----------
[examples](examples) | A collection of Python examples that help you learn the product features.
[sample_data](sample_data) | A collection of test data for running Python examples.

<p align="center">
  <a title="Download Examples ZIP" href="https://github.com/aspose-pdf/Aspose.PDF-for-Python-via-.NET/archive/master.zip">
	<img src="https://raw.github.com/AsposeExamples/java-examples-dashboard/master/images/downloadZip-Button-Large.png" />
  </a>
</p>


## General PDF Features

- Supports most established PDF standards and PDF specifications.
- Ability to read & export PDFs in multiple image formats including BMP, GIF, JPEG & PNG.
- Set basic information (e.g. author, creator) of the PDF document.
- Configure PDF Page properties (e.g. width, height, cropbox, bleedbox etc.).
- Set page numbering, bookmark level, page sizes etc.
- Ability to work with text, paragraphs, headings, hyperlinks, graphs, attachments etc.

## Conversion Features

**Aspose.PDF for Python via .NET** library allows you to successfully, quickly and easily convert your PDF documents to the most popular formats and vice versa.

- Convert PDF to Word, Excel, and PowerPoint.
- Convert PDF to Images formats.
- Convert PDF file to HTML format and vice versa.
- Convert PDF to EPUB, Text, XPS, etc.
- Convert EPUB, Markdown, Text, XPS, PostScript, XML, LaTex to PDF.

## Package Features

- Add, search, extract and replace text in PDF files.
- Add/delete, extract and replace images.
- Insert, delete, split PDF pages.
- Set and get XMP metadata.
- Validate (PDF/A-1a, PDF/A-1b).
- Work with bookmarks, annotations, PDF forms, stamps, watermarks and more.

## Read & Write PDF & Other Formats

**Fixed Layout:** PDF, PDF/A, PDF/UA, XPS\
**Books:** EPUB\
**Web:** HTML, MHTML\
**Other:** TEX, CGM, XSLFO, XML, PCL, SVG

## Save PDF Documents As

**Microsoft Office:** DOC, DOCX, XLS, XLSX, PPTX\
**Images:** JPEG, PNG, BMP, TIFF, EMF\
**Other:** MobiXML, XML

## Platform Independence

**Aspose.PDF for Python via .NET** can be used to develop 32-bit and 64-bit Python applications for different operating systems (such as Windows, Linux, macOS) where Python 3.9 or later is installed.

## Get Started with for Python via .NET


Run ```pip install aspose-pdf``` to fetch the package. If you already have **Aspose.PDF for Python via .NET** and want to get the latest version, please run ```pip install --upgrade aspose-pdf```.
To learn more about **Aspose.PDF for Python via .NET** and explore the basic requirements and features of the library, check out the following [Aspose.PDF for Python via .NET Documentation](https://docs.aspose.com/pdf/python-net/) pages for other use cases.


## Example of converting HTML to PDF

**Aspose.PDF for Python via .NET** is a PDF manipulation API that lets you convert any existing HTML documents to PDF format. The process of converting HTML to PDF can be flexibly customized.

Below code snippet follows these steps:

1. Create an instance of the HtmlLoadOptions object.
1. Initialize Document object.
1. Save output PDF document by calling Document.save() method.

```python
import aspose.pdf as ap
# Instantiate an object of HtmlLoadOptions
options = ap.HtmlLoadOptions()
# Convert HTML to PDF
document = ap.Document("input.html", options)
# Save PDF
document.save("output.pdf")
```

[Product Page](https://products.aspose.com/pdf/python-net/) | [Documentation](https://docs.aspose.com/pdf/python-net/) | [Demos](https://products.aspose.app/pdf/family) | [Blog](https://blog.aspose.com/categories/aspose.pdf-product-family/) | [API Reference](https://reference.aspose.com/pdf/python-net/) | [Examples](https://github.com/aspose-pdf/Aspose.PDF-for-Python-via-.NET) | [Search](https://search.aspose.com/) | [Free Support](https://forum.aspose.com/c/pdf) | [Temporary License](https://purchase.aspose.com/temporary-license)