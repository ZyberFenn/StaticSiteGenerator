import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq_different_text(self):
        node1 = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Hello!", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_not_eq_different_text_type(self):
        node1 = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Hello", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_eq_url_none_vs_value(self):
        node1 = TextNode("Boot.dev", TextType.LINK, None)
        node2 = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        self.assertNotEqual(node1, node2)

    def test_eq_same_url(self):
        node1 = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        node2 = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        self.assertEqual(node1, node2)

    def test_eq_explicit_none_url(self):
        node1 = TextNode("Text", TextType.BOLD)
        node2 = TextNode("Text", TextType.BOLD, None)
        self.assertEqual(node1, node2)

    def test_empty_text(self):
        node1 = TextNode("", TextType.TEXT)
        node2 = TextNode("", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold")

    def test_italic(self):
        node = TextNode("Italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic")

    def test_code(self):
        node = TextNode("print('hi')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hi')")

    def test_link(self):
        node = TextNode("Click me", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_image(self):
        node = TextNode("An image", TextType.IMAGE, "https://example.com/img.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://example.com/img.png", "alt": "An image"})

    def test_unknown_type_raises(self):
        # If it's hard to create an unknown enum in your project,
        # you can also pass a fake object or None.
        node = TextNode("X", None)
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
        
if __name__ == "__main__":
    unittest.main()