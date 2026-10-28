import unittest
from extract_blocks import markdown_to_blocks

class TestExtractBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_basic_blocks(self):
        markdown = "This is a paragraph.\n\nThis is another paragraph."
        expected_blocks = ["This is a paragraph.", "This is another paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_empty_markdown(self):
        markdown = ""
        expected_blocks = []
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_only_whitespace(self):
        markdown = "   \n\n  "
        expected_blocks = []
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_multiple_newlines(self):
        markdown = "Paragraph one.\n\n\n\nParagraph two."
        expected_blocks = ["Paragraph one.", "Paragraph two."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_leading_and_trailing_whitespace(self):
        markdown = "   Paragraph with leading and trailing whitespace.   \n\n   Another paragraph.   "
        expected_blocks = ["Paragraph with leading and trailing whitespace.", "Another paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_only_newlines(self):
        markdown = "\n\n\n"
        expected_blocks = []
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_mixed_whitespace_and_newlines(self):
        markdown = "   \n\nParagraph after whitespace and newlines.\n\n   "
        expected_blocks = ["Paragraph after whitespace and newlines."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_trailing_newline(self):
        markdown = "Paragraph with trailing newline.\n"
        expected_blocks = ["Paragraph with trailing newline."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_leading_newline(self):
        markdown = "\nParagraph with leading newline."
        expected_blocks = ["Paragraph with leading newline."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_leading_and_trailing_newline(self):
        markdown = "\nParagraph with leading and trailing newline.\n"
        expected_blocks = ["Paragraph with leading and trailing newline."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_multiple_paragraphs_and_newlines(self):
        markdown = "Paragraph one.\n\nParagraph two.\n\nParagraph three."
        expected_blocks = ["Paragraph one.", "Paragraph two.", "Paragraph three."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_paragraphs_separated_by_multiple_newlines(self):
        markdown = "Paragraph one.\n\n\n\nParagraph two."
        expected_blocks = ["Paragraph one.", "Paragraph two."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_empty_string(self):
        markdown = ""
        expected_blocks = []
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_only_whitespace(self):
        markdown = "   \t  "
        expected_blocks = []
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_whitespace_around_paragraphs(self):
        markdown = "   Paragraph with leading and trailing whitespace.   "
        expected_blocks = ["Paragraph with leading and trailing whitespace."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

    def test_markdown_with_whitespace_around_multiple_paragraphs(self):
        markdown = "   Paragraph one.   \n\n   Paragraph two.   "
        expected_blocks = ["Paragraph one.", "Paragraph two."]
        self.assertEqual(markdown_to_blocks(markdown), expected_blocks)

if __name__ == "__main__":
    unittest.main()