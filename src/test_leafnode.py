import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_span_with_props(self):
        node = LeafNode("span", "Hello, world!", props={"class": "highlight"})
        self.assertEqual(node.to_html(), '<span class="highlight">Hello, world!</span>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_empty_value(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr(self):
        node = LeafNode("p", "Hello, world!", props={"class": "highlight"})
        self.assertEqual(repr(node), "LeafNode('p', 'Hello, world!', {'class': 'highlight'})")

    def test_eq(self):
        node1 = LeafNode("p", "Hello, world!", props={"class": "highlight"})
        node2 = LeafNode("p", "Hello, world!", props={"class": "highlight"})
        self.assertEqual(node1, node2)

    def test_eq_different_tag(self):
        node1 = LeafNode("p", "Hello, world!", props={"class": "highlight"})
        node2 = LeafNode("span", "Hello, world!", props={"class": "highlight"})
        self.assertNotEqual(node1, node2)

    def test_eq_different_value(self):
        node1 = LeafNode("p", "Hello, world!", props={"class": "highlight"})
        node2 = LeafNode("p", "Goodbye, world!", props={"class": "highlight"})
        self.assertNotEqual(node1, node2)

    def test_eq_different_props(self):
        node1 = LeafNode("p", "Hello, world!", props={"class": "highlight"})
        node2 = LeafNode("p", "Hello, world!", props={"id": "main"})
        self.assertNotEqual(node1, node2)

    def test_eq_different_types(self):
        node = LeafNode("p", "Hello, world!", props={"class": "highlight"})
        self.assertNotEqual(node, "Hello, world!")

    def test_eq_with_none_props(self):
        node1 = LeafNode("p", "Hello, world!", props=None)
        node2 = LeafNode("p", "Hello, world!", props={"class": "highlight"})
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()