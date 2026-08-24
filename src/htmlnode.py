class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self) -> str:
        raise NotImplementedError("to_html method should be implemented in subclasses")

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        return ' ' + ' '.join(f'{key}="{value}"' for key, value in self.props.items())

    def __eq__(self, other):
        return (
            isinstance(other, HTMLNode) and
            self.tag == other.tag and
            self.value == other.value and
            self.props == other.props and
            self.children == other.children
        )

    def __repr__(self):
        return f"HTMLNode({self.tag!r}, {self.value!r}, {self.props!r}, {self.children!r})"