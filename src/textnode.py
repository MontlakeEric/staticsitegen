from enum import Enum

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType = TextType.PLAIN, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type.value}, {self.url!r})"

    def render(self) -> str:
        if self.text_type == TextType.PLAIN:
            return self.text
        elif self.text_type == TextType.BOLD:
            return f"<strong>{self.text}</strong>"
        elif self.text_type == TextType.ITALIC:
            return f"<em>{self.text}</em>"
        elif self.text_type == TextType.CODE:
            return f"<code>{self.text}</code>"
        elif self.text_type == TextType.LINK:
            return f'<a href="{self.url}">{self.text}</a>'
        elif self.text_type == TextType.IMAGE:
            return f'<img src="{self.url}" alt="{self.text}" />'
        else:
            raise ValueError(f"Unsupported text type: {self.text_type}")