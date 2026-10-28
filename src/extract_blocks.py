def markdown_to_blocks(markdown):
    initial_list = markdown.split("\n\n")
    stripped_list = [block.strip() for block in initial_list]
    trimmed_list = [block for block in stripped_list if block]
    return trimmed_list
