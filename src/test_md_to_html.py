import unittest
from md_to_html import markdown_to_html_node


class TestMdToHtml(unittest.TestCase):

    # Helper: markdown in, HTML string out
    def html(self, md):
        return markdown_to_html_node(md).to_html()

    # Paragraphs

    def test_paragraphs(self):
        md = (
            "This is **bolded** paragraph\ntext in a p\ntag here\n\n"
            "This is another paragraph with _italic_ text and `code` here"
        )
        self.assertEqual(
            self.html(md),
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    # Headings

    def test_headings_all_levels(self):
        md = "# H1\n\n## H2\n\n### H3\n\n#### H4\n\n##### H5\n\n###### H6"
        self.assertEqual(
            self.html(md),
            "<div><h1>H1</h1><h2>H2</h2><h3>H3</h3><h4>H4</h4><h5>H5</h5><h6>H6</h6></div>",
        )

    def test_heading_with_inline(self):
        md = "## A **bold** and _italic_ title"
        self.assertEqual(self.html(md), "<div><h2>A <b>bold</b> and <i>italic</i> title</h2></div>")

    def test_heading_multiline(self):
        # spec: a heading only has to *start* with #s; later lines join with a space
        md = "# Title\nsecond line"
        self.assertEqual(self.html(md), "<div><h1>Title second line</h1></div>")

    def test_seven_hashes_is_paragraph(self):
        md = "####### Not a heading"
        self.assertEqual(self.html(md), "<div><p>####### Not a heading</p></div>")

    # Code blocks

    def test_codeblock(self):
        md = "```\nThis is text that _should_ remain\nthe **same** even with inline stuff\n```"
        self.assertEqual(
            self.html(md),
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_codeblock_keeps_first_character(self):
        md = "```\nprint(1)\n```"
        self.assertEqual(self.html(md), "<div><pre><code>print(1)\n</code></pre></div>")

    def test_codeblock_keeps_indentation(self):
        md = "```\ndef f():\n    return 1\n```"
        self.assertEqual(self.html(md), "<div><pre><code>def f():\n    return 1\n</code></pre></div>")

    # Quotes

    def test_quote_multiline_with_inline(self):
        md = "> This is a\n> quote with **bold**"
        self.assertEqual(self.html(md), "<div><blockquote>This is a quote with <b>bold</b></blockquote></div>")

    def test_quote_space_after_marker_optional(self):
        md = "> with space\n>without space"
        self.assertEqual(self.html(md), "<div><blockquote>with space without space</blockquote></div>")

    # Lists

    def test_unordered_list_with_inline(self):
        md = "- plain\n- **bold**\n- `code`"
        self.assertEqual(
            self.html(md),
            "<div><ul><li>plain</li><li><b>bold</b></li><li><code>code</code></li></ul></div>",
        )

    def test_ordered_list(self):
        md = "1. first\n2. _second_\n3. third"
        self.assertEqual(
            self.html(md),
            "<div><ol><li>first</li><li><i>second</i></li><li>third</li></ol></div>",
        )

    def test_ordered_list_double_digits(self):
        md = "\n".join(f"{i}. item {i}" for i in range(1, 12))
        expected_items = "".join(f"<li>item {i}</li>" for i in range(1, 12))
        self.assertEqual(self.html(md), f"<div><ol>{expected_items}</ol></div>")

    def test_ordered_list_non_sequential_is_paragraph(self):
        md = "1. one\n3. three"
        self.assertEqual(self.html(md), "<div><p>1. one 3. three</p></div>")

    # Inline links

    def test_paragraph_with_link(self):
        md = "Go to [Boot.dev](https://www.boot.dev) now"
        self.assertEqual(
            self.html(md),
            '<div><p>Go to <a href="https://www.boot.dev">Boot.dev</a> now</p></div>',
        )

    # Whole documents

    def test_mixed_document_keeps_block_order(self):
        md = """
# Title

Intro with **bold**.

- item one
- item two

```
code here
```

> a quote
"""
        self.assertEqual(
            self.html(md),
            "<div><h1>Title</h1><p>Intro with <b>bold</b>.</p>"
            "<ul><li>item one</li><li>item two</li></ul>"
            "<pre><code>code here\n</code></pre>"
            "<blockquote>a quote</blockquote></div>",
        )

    def test_extra_blank_lines_between_blocks(self):
        md = "\n\n\n# Title\n\n\n\n\nParagraph\n\n\n"
        self.assertEqual(self.html(md), "<div><h1>Title</h1><p>Paragraph</p></div>")

if __name__ == "__main__":
    unittest.main()