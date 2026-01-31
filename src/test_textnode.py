import unittest

from textnode import TextNode, TextType

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
        
if __name__ == "__main__":
    unittest.main()