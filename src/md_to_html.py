from extract_blocks import markdown_to_blocks
from block_types import BlockType, block_to_block_type
from splitnodes import text_to_textnodes
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
import re


def markdown_to_html_node(markdown):
    # going from markdown to ParentNode with many children
    blocks = markdown_to_blocks(markdown)
    children = list(map(block_to_node, blocks))
    return ParentNode(tag="div", children=children)

def block_to_node(block):
    return BLOCK_TYPE_TO_NODE[block_to_block_type(block)](block)

def text_to_html_nodes(text):
    # replace newlines with spaces to pass unit tests they provided
    text = text.replace("\n", " ")
    return list(map(text_node_to_html_node, text_to_textnodes(text))) 

def block_to_html_node_paragraph(block):
    return ParentNode(tag="p", children=text_to_html_nodes(block))

# the functions below all assume block_to_block_type has already been called
# ensuring the regex and removeprefix will succeed

def block_to_html_node_heading(block):
    hashes, _, text = block.partition(" ")
    return ParentNode(tag=f"h{len(hashes)}", children=text_to_html_nodes(text))
    
def block_to_html_node_code(block):
    text = block.removeprefix("```\n").removesuffix("```")
    children = [text_node_to_html_node(TextNode(text, text_type=TextType.CODE))]
    return ParentNode(tag="pre", children=children)

def block_to_html_node_quote(block):
    lines = [line.removeprefix(">").removeprefix(" ") for line in block.split("\n")]
    text = " ".join(lines)
    return ParentNode(tag="blockquote", children=text_to_html_nodes(text))

def block_to_html_node_unordered_list(block):
    lines = [line.removeprefix("- ") for line in block.split("\n")]
    children = [ParentNode(tag="li", children=text_to_html_nodes(line)) for line in lines]
    return ParentNode(tag="ul", children=children)

def block_to_html_node_ordered_list(block):
    lines = [line.removeprefix(f"{i}. ") for i, line in enumerate(block.split("\n"), start=1)]
    children = [ParentNode(tag="li", children=text_to_html_nodes(line)) for line in lines]
    return ParentNode(tag="ol", children=children)

BLOCK_TYPE_TO_NODE = {
    BlockType.PARAGRAPH: block_to_html_node_paragraph,
    BlockType.HEADING: block_to_html_node_heading,
    BlockType.CODE: block_to_html_node_code,
    BlockType.QUOTE: block_to_html_node_quote,
    BlockType.UNORDERED_LIST: block_to_html_node_unordered_list,
    BlockType.ORDERED_LIST: block_to_html_node_ordered_list,
}
