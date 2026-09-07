import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

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

    def test_plain(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link(self):
        node = TextNode("This is a link text node", TextType.LINK, url="https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_image(self):
        node = TextNode("This is an image text node", TextType.IMAGE, url="https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://example.com/image.png", "alt": "This is an image text node"})

    def test_link_without_url(self):
        node = TextNode("This is a link text node", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_image_without_url(self):
        node = TextNode("This is an image text node", TextType.IMAGE)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_unsupported_text_type(self):
        node = TextNode("This is a text node", "unsupported")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_text_node_to_html_node_with_invalid_type(self):
        node = TextNode("This is a text node", "invalid")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_text_node_to_html_node_with_none_type(self):
        node = TextNode("This is a text node", None)
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    def test_text_node_to_html_node_with_empty_text(self):
        node = TextNode("", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "")

    def test_text_node_to_html_node_with_empty_text_and_bold(self):
        node = TextNode("", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "")

    def test_text_node_to_html_node_with_empty_text_and_italic(self):
        node = TextNode("", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "")

    def test_text_node_to_html_node_with_empty_text_and_code(self):
        node = TextNode("", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "")
    
if __name__ == "__main__":
    unittest.main()