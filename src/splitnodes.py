from textnode import TextNode, TextType

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
