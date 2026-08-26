from htmlnode import HTMLNode

class ParentNode(HTMLNode): 
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("ParentNode must have a tag to render")
        if not self.children:
            raise ValueError("ParentNode must have children to render") 
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag!r}, {self.props!r}, {self.children!r})"