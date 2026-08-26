import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_repr(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={"class": "container"})
        self.assertEqual(
            repr(parent_node),
            "ParentNode('div', {'class': 'container'}, [LeafNode('span', 'child', {})])",
        )

    def test_eq(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "child")
        parent_node2 = ParentNode("div", [child_node2], props={"class": "container"})

        self.assertEqual(parent_node1, parent_node2)

    def test_eq_different_tag(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "child")
        parent_node2 = ParentNode("p", [child_node2], props={"class": "container"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_different_children(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "different_child")
        parent_node2 = ParentNode("div", [child_node2], props={"class": "container"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_different_props(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "child")
        parent_node2 = ParentNode("div", [child_node2], props={"id": "main"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_different_types(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={"class": "container"})

        self.assertNotEqual(parent_node, "This is a string, not a ParentNode")

    def test_eq_with_none_props(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props=None)

        child_node2 = LeafNode("span", "child")
        parent_node2 = ParentNode("div", [child_node2], props={"class": "container"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_with_none_children(self):
        parent_node1 = ParentNode("div", [], props={"class": "container"})
        parent_node2 = ParentNode("div", [LeafNode("span", "child")], props={"class": "container"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_with_both_none_children(self):
        parent_node1 = ParentNode("div", [], props={"class": "container"})
        parent_node2 = ParentNode("div", [], props={"class": "container"})

        self.assertEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_and_children(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "child")
        parent_node2 = ParentNode("p", [child_node2], props={"class": "container"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_and_props(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "child")
        parent_node2 = ParentNode("p", [child_node2], props={"class": "container"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_with_different_children_and_props(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "different_child")
        parent_node2 = ParentNode("div", [child_node2], props={"id": "main"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "different_child")
        parent_node2 = ParentNode("p", [child_node2], props={"id": "main"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "different_child")
        parent_node2 = ParentNode("p", [child_node2], props={"id": "main"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order_same(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "child")
        parent_node2 = ParentNode("div", [child_node2], props={"class": "container"})

        self.assertEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order_different(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "different_child")
        parent_node2 = ParentNode("p", [child_node2], props={"id": "main"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order_same_different(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "child")
        parent_node2 = ParentNode("div", [child_node2], props={"class": "container"})

        self.assertEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order_different_same(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "different_child")
        parent_node2 = ParentNode("p", [child_node2], props={"id": "main"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order_same_different_same(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "child")
        parent_node2 = ParentNode("div", [child_node2], props={"class": "container"})

        self.assertEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order_different_same_different(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "different_child")
        parent_node2 = ParentNode("p", [child_node2], props={"id": "main"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order_same_different_same_different(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "child")
        parent_node2 = ParentNode("div", [child_node2], props={"class": "container"})

        self.assertEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order_different_same_different_same(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "different_child")
        parent_node2 = ParentNode("p", [child_node2], props={"id": "main"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order_same_different_same_different_same(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "child")
        parent_node2 = ParentNode("div", [child_node2], props={"class": "container"})

        self.assertEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order_different_same_different_same_different(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "different_child")
        parent_node2 = ParentNode("p", [child_node2], props={"id": "main"})

        self.assertNotEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order_same_different_same_different_same_different(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "child")
        parent_node2 = ParentNode("div", [child_node2], props={"class": "container"})

        self.assertEqual(parent_node1, parent_node2)

    def test_eq_with_different_tag_children_and_props_order_different_same_different_same_different_same(self):
        child_node1 = LeafNode("span", "child")
        parent_node1 = ParentNode("div", [child_node1], props={"class": "container"})

        child_node2 = LeafNode("span", "different_child")
        parent_node2 = ParentNode("p", [child_node2], props={"id": "main"})

        self.assertNotEqual(parent_node1, parent_node2)
    
if __name__ == "__main__":
    unittest.main()