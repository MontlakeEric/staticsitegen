import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_render_plain(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        self.assertEqual(node.render(), "This is a text node")

    def test_render_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.render(), "<strong>This is a text node</strong>")

    def test_render_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.render(), "<em>This is a text node</em>")

    def test_render_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node.render(), "<code>This is a text node</code>")

    def test_render_link(self):
        node = TextNode("This is a text node", TextType.LINK, url="https://example.com")
        self.assertEqual(node.render(), '<a href="https://example.com">This is a text node</a>')

    def test_render_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, url="https://example.com/image.png")
        self.assertEqual(node.render(), '<img src="https://example.com/image.png" alt="This is a text node" />')

    def test_render_unsupported_type(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        node.text_type = "unsupported"
        with self.assertRaises(ValueError):
            node.render()

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode('This is a text node', bold, None)")

    def test_repr_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, url="https://example.com")
        self.assertEqual(repr(node), "TextNode('This is a text node', link, 'https://example.com')")

    def test_repr_with_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, url="https://example.com/image.png")
        self.assertEqual(repr(node), "TextNode('This is a text node', image, 'https://example.com/image.png')")

    def test_repr_with_unsupported_type(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        node.text_type = "unsupported"
        with self.assertRaises(ValueError):
            repr(node)

    def test_eq_with_different_types(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, "This is a text node")

    def test_eq_with_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_with_different_url(self):
        node = TextNode("This is a text node", TextType.LINK, url="https://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, url="https://different.com")
        self.assertNotEqual(node, node2)

    def test_eq_with_none_url(self):
        node = TextNode("This is a text node", TextType.LINK, url=None)
        node2 = TextNode("This is a text node", TextType.LINK, url="https://example.com")
        self.assertNotEqual(node, node2)

    def test_eq_with_both_none_url(self):
        node = TextNode("This is a text node", TextType.LINK, url=None)
        node2 = TextNode("This is a text node", TextType.LINK, url=None)
        self.assertEqual(node, node2)

    def test_eq_with_different_text_and_url(self):
        node = TextNode("This is a text node", TextType.LINK, url="https://example.com")
        node2 = TextNode("This is a different text node", TextType.LINK, url="https://different.com")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text_type_and_url(self):
        node = TextNode("This is a text node", TextType.LINK, url="https://example.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, url="https://different.com")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text_type_and_none_url(self):
        node = TextNode("This is a text node", TextType.LINK, url=None)
        node2 = TextNode("This is a text node", TextType.ITALIC, url=None)
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text_and_none_url(self):
        node = TextNode("This is a text node", TextType.LINK, url=None)
        node2 = TextNode("This is a different text node", TextType.LINK, url=None)
        self.assertNotEqual(node, node2)

    def test_eq_with_different_text_type_and_different_url(self):
        node = TextNode("This is a text node", TextType.LINK, url="https://example.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, url="https://different.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()