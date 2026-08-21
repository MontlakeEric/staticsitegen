import textnode

def main():
    node1 = textnode.TextNode("Hello, World!", textnode.TextType.BOLD)
    print(repr(node1))
    node2 = textnode.TextNode("Click here", textnode.TextType.LINK, url="https://example.com")
    print(repr(node2))

main()
