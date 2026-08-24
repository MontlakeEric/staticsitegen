import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node = HTMLNode("div", "Hello", [{"tag": "span", "value": "World"}], {"class": "container"})
        node2 = HTMLNode("div", "Hello", [{"tag": "span", "value": "World"}], {"class": "container"})
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("div", "Hello", [{"tag": "span", "value": "World"}], {"class": "container"})
        self.assertEqual(repr(node), "HTMLNode('div', 'Hello', {'class': 'container'}, [{'tag': 'span', 'value': 'World'}])")

    def test_props_to_html(self):
        node = HTMLNode("div", props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="container" id="main"')

    def test_props_to_html_empty(self):
        node = HTMLNode("div")
        self.assertEqual(node.props_to_html(), "")

    def test_eq_with_different_types(self):
        node = HTMLNode("div", "Hello")
        self.assertNotEqual(node, "Hello")

    def test_eq_with_different_tag(self):
        node = HTMLNode("div", "Hello")
        node2 = HTMLNode("p", "Hello")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_value(self):
        node = HTMLNode("div", "Hello")
        node2 = HTMLNode("div", "World")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_props(self):
        node = HTMLNode("div", "Hello", props={"class": "container"})
        node2 = HTMLNode("div", "Hello", props={"id": "main"})
        self.assertNotEqual(node, node2)

    def test_eq_with_different_children(self):
        node = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")])
        node2 = HTMLNode("div", "Hello", children=[HTMLNode("p", "World")])
        self.assertNotEqual(node, node2)

    def test_eq_with_different_children_count(self):
        node = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")])
        node2 = HTMLNode("div", "Hello", children=[HTMLNode("span", "World"), HTMLNode("p", "Extra")])
        self.assertNotEqual(node, node2)

    def test_eq_with_different_props_and_children(self):
        node = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"class": "container"})
        node2 = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"id": "main"})
        self.assertNotEqual(node, node2)

    def test_eq_with_different_tag_and_value(self):
        node = HTMLNode("div", "Hello")
        node2 = HTMLNode("p", "World")
        self.assertNotEqual(node, node2)

    def test_eq_with_different_tag_and_props(self):
        node = HTMLNode("div", "Hello", props={"class": "container"})
        node2 = HTMLNode("p", "Hello", props={"class": "container"})
        self.assertNotEqual(node, node2)

    def test_eq_with_different_tag_and_children(self):
        node = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")])
        node2 = HTMLNode("p", "Hello", children=[HTMLNode("span", "World")])
        self.assertNotEqual(node, node2)

    def test_eq_with_different_value_and_props(self):
        node = HTMLNode("div", "Hello", props={"class": "container"})
        node2 = HTMLNode("div", "World", props={"class": "container"})
        self.assertNotEqual(node, node2)

    def test_eq_with_different_value_and_children(self):
        node = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")])
        node2 = HTMLNode("div", "World", children=[HTMLNode("span", "World")])
        self.assertNotEqual(node, node2)

    def test_eq_with_different_props_and_children(self):
        node = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"class": "container"})
        node2 = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"id": "main"})
        self.assertNotEqual(node, node2)

    def test_eq_with_different_tag_value_props_children(self):
        node = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"class": "container"})
        node2 = HTMLNode("p", "World", children=[HTMLNode("p", "Extra")], props={"id": "main"})
        self.assertNotEqual(node, node2)

    def test_eq_with_different_tag_value_props_children_order(self):
        node = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"class": "container"})
        node2 = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"class": "container"})
        self.assertEqual(node, node2)

    def test_eq_with_different_tag_value_props_children_order_different(self):
        node = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"class": "container"})
        node2 = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"id": "main"})
        self.assertNotEqual(node, node2)

    def test_eq_with_different_tag_value_props_children_order_same(self):
        node = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"class": "container"})
        node2 = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"class": "container"})
        self.assertEqual(node, node2)

    def test_eq_with_different_tag_value_props_children_order_same_different(self):
        node = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"class": "container"})
        node2 = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"id": "main"})
        self.assertNotEqual(node, node2)

    def test_eq_with_different_tag_value_props_children_order_same_different_order(self):
        node = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"class": "container"})
        node2 = HTMLNode("div", "Hello", children=[HTMLNode("span", "World")], props={"class": "container"})
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()