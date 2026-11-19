def markdown_to_blocks(markdown):
    # updated after more recent learning, to use map() and filter() instead of a list comprehension
    # comprehensions not needed for these simplified cases with an already-defined map function (str.strip) and the "None" shortcut for filtering out empty strings
    return list(filter(None, map(str.strip, markdown.split("\n\n"))))
