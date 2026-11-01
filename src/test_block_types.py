import unittest
from block_types import BlockType, block_to_block_type

class TestBlockTypes(unittest.TestCase):

    def test_block_to_block_type_heading(self):
        block = "# Heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = "> Quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        block = "- Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        block = "1. Item 1\n2. Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        block = "This is a paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_empty(self):
        block = ""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Test the negative cases - each case has reasons it won't proplerly match, so test those

    def test_block_to_block_type_with_too_long_heading(self):
        block = "####### Heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_with_heading_without_space(self):
        block = "###Heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_with_3_backticks_but_no_newline(self):
        block = "```code```"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Code block but not ending with 3 backticks
    def test_block_to_block_type_with_code_block_missing_ending_backticks(self):
        block = "```\ncode"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Code block but another character after the ending backticks
    def test_block_to_block_type_with_code_block_extra_characters(self):
        block = "```\ncode\n```extra"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Quote block with multiple lines and one does not have the '>' at the start
    def test_block_to_block_type_with_quote_block_missing_prefix(self):
        block = "> Quote\n> Another quote\nQuote without prefix"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Unordered list block with multiple lines and one does not have the '-' at the start
    def test_block_to_block_type_with_unordered_list_missing_prefix(self):
        block = "- Item 1\n- Item 2\nItem without prefix"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Unordered list block with multiple lines and one does not have a space after the leading dash
    def test_block_to_block_type_with_unordered_list_missing_space(self):
        block = "- Item 1\n- Item 2\n-Item 3 no space\n- Item 4"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Ordered list block with multiple lines and one does not have a number followed by a period at the start
    def test_block_to_block_type_with_ordered_list_missing_prefix(self):
        block = "1. Item 1\n2. Item 2\nItem without prefix"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Ordered list block with multiple lines and one has a number but not a period at the start
    def test_block_to_block_type_with_ordered_list_missing_period(self):
        block = "1 Item 1\n2. Item 2\n3. Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Ordered list block with multiple lines and one has a number and period but not a space at the start
    def test_block_to_block_type_with_ordered_list_missing_space(self):
        block = "1. Item 1\n2. Item 2\n3.Item 3 no space\n4. Item 4"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Ordered list formatted properly but the numbers are not sequential
    def test_block_to_block_type_with_ordered_list_non_sequential(self):
        block = "1. Item 1\n3. Item 3\n4. Item 4"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Ordered list formatted properly and sequential numbers but not starting at 1
    def test_block_to_block_type_with_ordered_list_not_starting_at_1(self):
        block = "2. Item 2\n3. Item 3\n4. Item 4"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()