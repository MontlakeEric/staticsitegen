from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    # per spec, all leading and trailing whitespace were already stripped (in markdown_to_blocks)

    # Headings start with 1-6 # characters, followed by a space and then the heading text.
    if re.search(r"^#{1,6} ", block):
        return BlockType.HEADING

    # Multiline Code blocks must start with 3 backticks and a newline, then end with 3 backticks.
    if re.search(r"^```\n.*\n```$", block):
        return BlockType.CODE

    lines = block.split("\n")

    # whitespace has been stripped, but just making absolutely sure that it wasn't all whitespace or even an empty string
    if len(lines) == 0:
        return BlockType.PARAGRAPH

    # Every line in a quote block must start with a "greater-than" character: > followed by the quote text. A space after > is allowed but not required.
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Every line in an unordered list block must start with a - character, followed by a space.
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
    if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST

    # If none of the above conditions are met, the block is a normal paragraph.
    return BlockType.PARAGRAPH
