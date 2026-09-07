import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter


class TestSplitNodes(unittest.TestCase):

    def test_split_nodes_delimiter(self):
        old_nodes = [
            TextNode("This is a **bold** text node", TextType.PLAIN),
            TextNode("This is another text node", TextType.PLAIN)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is a ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" text node", TextType.PLAIN),
            TextNode("This is another text node", TextType.PLAIN)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_with_unmatched_delimiter(self):
        old_nodes = [
            TextNode("This is a **bold text node", TextType.PLAIN)
        ]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

    def test_split_nodes_delimiter_with_no_delimiter(self):
        old_nodes = [
            TextNode("This is a text node", TextType.PLAIN)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, old_nodes)

    def test_split_nodes_delimiter_with_non_plain_text_type(self):
        old_nodes = [
            TextNode("This is a **bold** text node", TextType.BOLD)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, old_nodes)

    def test_split_nodes_delimiter_with_url(self):
        old_nodes = [
            TextNode("This is a **bold** text node", TextType.PLAIN, url="https://example.com")
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is a ", TextType.PLAIN, url="https://example.com"),
            TextNode("bold", TextType.BOLD, url="https://example.com"),
            TextNode(" text node", TextType.PLAIN, url="https://example.com")
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_with_multiple_delimiters(self):
        old_nodes = [
            TextNode("This is a **bold** and **another bold** text node", TextType.PLAIN)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is a ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.PLAIN),
            TextNode("another bold", TextType.BOLD),
            TextNode(" text node", TextType.PLAIN)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_with_empty_parts(self):
        old_nodes = [
            TextNode("**bold**", TextType.PLAIN)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("bold", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_with_consecutive_delimiters(self):
        old_nodes = [
            TextNode("This is a ****bold**** text node", TextType.PLAIN)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is a ", TextType.PLAIN),
            TextNode("bold", TextType.PLAIN),
            TextNode(" text node", TextType.PLAIN)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_with_delimiter_at_start_and_end(self):
        old_nodes = [
            TextNode("**bold**", TextType.PLAIN)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("bold", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected_nodes) 

    def test_split_nodes_delimiter_with_delimiter_only(self):
        old_nodes = [
            TextNode("****", TextType.PLAIN)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_with_non_plain_text_type_italic(self):
        old_nodes = [
            TextNode("This is a _italic_ text node", TextType.ITALIC)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes, old_nodes)

    def test_split_nodes_delimiter_with_non_plain_text_type_code(self):
        old_nodes = [
            TextNode("This is a `code` text node", TextType.CODE)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, old_nodes)

    def test_split_nodes_delimiter_with_all_three(self):
        old_nodes = [
            TextNode("This is a _italic_, **bold**, and `code` text node", TextType.PLAIN)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is a ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(", ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(", and ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" text node", TextType.PLAIN)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_leave_other_types_alone(self):
        old_nodes = [
            TextNode("This is a **bold** text node", TextType.BOLD),
            TextNode("This is an _italic_ text node", TextType.ITALIC),
            TextNode("This is a `code` text node", TextType.CODE)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, old_nodes)

if __name__ == "__main__":
    unittest.main()