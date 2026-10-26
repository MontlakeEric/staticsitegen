import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes


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

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [second link](https://example.org)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second link", TextType.LINK, "https://example.org"),
            ],
            new_nodes,
        )

    def test_split_images_and_links(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com) with text at the end",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        new_nodes = split_nodes_link(new_nodes)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" with text at the end", TextType.PLAIN),
            ],
            new_nodes,
        )

    def test_split_links_and_images(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        new_nodes = split_nodes_image(new_nodes)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_images_with_no_images(self):
        node = TextNode(
            "This is text with no images",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with no images", TextType.PLAIN),
            ],
            new_nodes,
        )

    def test_split_links_with_no_links(self):
        node = TextNode(
            "This is text with no links",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with no links", TextType.PLAIN),
            ],
            new_nodes,
        )

    def test_split_images_with_non_plain_text_type(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.IMAGE,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.IMAGE),
            ],
            new_nodes,
        )

    def test_split_links_with_non_plain_text_type(self):
        node = TextNode(
            "This is text with a [link](https://example.com)",
            TextType.LINK,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a [link](https://example.com)", TextType.LINK),
            ],
            new_nodes,
        )

    def test_split_images_with_url(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
            url="https://example.com",
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN, url="https://example.com"),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_links_with_url(self):
        node = TextNode(
            "This is text with a [link](https://example.com)",
            TextType.PLAIN,
            url="https://example.com",
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN, url="https://example.com"),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

    def test_split_images_with_multiple_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links_with_multiple_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [second link](https://example.org)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("second link", TextType.LINK, "https://example.org"),
            ],
            new_nodes,
        )

    def test_split_images_with_overlapping_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_links_with_overlapping_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [link](https://example.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

    def test_split_images_with_nested_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_links_with_nested_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com) and another [link](https://example.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

    def test_split_images_with_adjacent_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_links_with_adjacent_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com)[link](https://example.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

    def test_split_images_with_overlapping_and_adjacent_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_links_with_overlapping_and_adjacent_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com)[link](https://example.com) and another [link](https://example.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

    def test_split_images_with_overlapping_and_adjacent_and_nested_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_links_with_overlapping_and_adjacent_and_nested_links(self):
        node = TextNode(
            "This is text with a [link](https://example.com)[link](https://example.com) and another [link](https://example.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is a **bold** and _italic_ text with a [link](https://example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is a ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text with a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_with_no_formatting(self):
        text = "This is a plain text with no formatting"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is a plain text with no formatting", TextType.PLAIN),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_with_only_formatting(self):
        text = "**bold** _italic_ [link](https://example.com) ![image](https://i.imgur.com/zjjcJKZ.png)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("bold", TextType.BOLD),
            TextNode(" ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" ", TextType.PLAIN),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_textnodes_with_unmatched_delimiter(self):
        text = "This is a **bold and _italic_ text with a [link](https://example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
        with self.assertRaises(ValueError):
            text_to_textnodes(text)

    def test_text_to_textnodes_with_multiple_of_each(self):
        text = "This is a **bold** and _italic_ text with a [link](https://example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png) and another **bold** and _italic_ text with a [link](https://example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is a ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text with a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text with a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ]
        self.assertEqual(nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()