---
title: UnderlineAnnotation
second_title: Aspose.PDF for Python via .NET API Reference
description: Represents an underline annotation that appears as an underline in the text of the document.
type: docs
weight: 850
url: /python-net/aspose.pdf.annotations/underlineannotation/
---

## UnderlineAnnotation class

Represents an underline annotation that appears as an underline in the text of the document.

The UnderlineAnnotation type exposes the following members:
## Constructors
| Name | Description |
| :- | :- |
|UnderlineAnnotation(page, rect)|Initializes a new instance of the UnderlineAnnotation class|
## Properties
| Name | Description |
| :- | :- |
|vertical_alignment|None|
|horizontal_alignment|None|
|margin|None|
|is_first_paragraph_in_column|None|
|is_kept_with_next|None|
|is_in_new_page|None|
|is_in_line_paragraph|None|
|hyperlink|None|
|z_index|None|
|update_appearance_on_convert|None|
|use_font_subset|None|
|flags|None|
|annotation_type|Gets type of annotation.|
|width|None|
|actions|None|
|height|None|
|rect|None|
|contents|None|
|name|None|
|modified|None|
|color|None|
|border|None|
|active_state|None|
|characteristics|None|
|states|None|
|alignment|None|
|text_horizontal_alignment|None|
|full_name|None|
|appearance|None|
|page_index|None|
|title|Gets or sets a text that shall be displayed in title bar of annotation.|
|rich_text|Gets or sets a rich text string to be displayed in the pop-up window when the annotation is opened.|
|creation_date|Gets date and time when annotation was created.|
|subject|Gets text representing desciption of the object.|
|popup|Pop-up annotation for entering or editing the text associated with this annotation.|
|opacity|Gets or sets the constant opacity value to be used in painting the annotation.|
|in_reply_to|A reference to the annotation that this annotation is "in reply to".<br/>            Both annotations must be on the same page of the document.|
|reply_type|A string specifying the relationship (the "reply type") between this annotation<br/>            and one specified by InReplyTo.|
|quad_points|Gets or sets an array of points specifying the coordinates of n quadrilaterals. Each quadrilateral encompasses a word or group of contiguous words in the text underlying the annotation.|
## Methods
| Name | Description |
| :- | :- |
|clone()|None|
|get_rectangle(consider_rotation)|None|
|accept(visitor)|Accepts visitor object to process the annotation.|
|flatten()|None|
|change_after_resize(transform)|Updates the QuadPoints, according to the matrix transform.|
|get_marked_text()|Gets text under markup annotation as string.|
|get_marked_text_fragments()|Gets text under markup annotation as [TextFragmentCollection](/pdf/python-net/aspose.pdf.text/textfragmentcollection/).|

### See Also

* namespace [aspose.pdf.annotations](/pdf/python-net/aspose.pdf.annotations/)
* assembly [Aspose.PDF](/pdf/python-net/)

