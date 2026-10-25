from textnode import TextNode, TextType
from extract_links import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.PLAIN and delimiter in node.text:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError(f"Unmatched delimiter '{delimiter}' in text: {node.text}")
            for i, part in enumerate(parts):
                # in the case of a start and immediate end delimiter, we skip the empty part
                # NOTE: this will not work for cases where one delimiter is a repeat of another, e.g. "**" and "*", but that is not a supported case for now
                # OR you can call it first with the repeat delimiter, then with the single delimiter, but that ordering has to be done outside this method with full knowledge of the delimiters being used
                if not part:
                    continue
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, text_type=TextType.PLAIN, url=node.url))
                else:
                    new_nodes.append(TextNode(part, text_type=text_type, url=node.url))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        text = node.text
        if node.text_type == TextType.PLAIN and (images := extract_markdown_images(text)):
            last_index = 0
            for alt_text, url in images:
                full_image = f"![{alt_text}]({url})"
                start_index = text.find(full_image, last_index)
                if start_index > last_index:
                    new_nodes.append(TextNode(text[last_index:start_index], text_type=TextType.PLAIN, url=node.url))
                new_nodes.append(TextNode(alt_text, text_type=TextType.IMAGE, url=url))
                last_index = start_index + len(full_image)
            if last_index < len(text):
                new_nodes.append(TextNode(text[last_index:], text_type=TextType.PLAIN, url=node.url))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        text = node.text
        if node.text_type == TextType.PLAIN and (links := extract_markdown_links(text)):
            last_index = 0
            for link_text, url in links:
                full_link = f"[{link_text}]({url})"
                start_index = text.find(full_link, last_index)
                if start_index > last_index:
                    new_nodes.append(TextNode(text[last_index:start_index], text_type=TextType.PLAIN, url=node.url))
                new_nodes.append(TextNode(link_text, text_type=TextType.LINK, url=url))
                last_index = start_index + len(full_link)
            if last_index < len(text):
                new_nodes.append(TextNode(text[last_index:], text_type=TextType.PLAIN, url=node.url))
        else:
            new_nodes.append(node)
    return new_nodes
