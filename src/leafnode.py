from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, children=[], props=props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError("LeafNode must have a value to render")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag!r}, {self.value!r}, {self.props!r})"