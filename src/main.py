from textnode import TextNode, TextType
from htmlnode import LeafNode


def main():
    
    node = TextNode("This is some anchor text", TextType.TEXT, "https://www.boot.dev")
    print(node)

main()