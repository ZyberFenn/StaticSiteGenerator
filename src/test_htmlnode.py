import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
        
    def test_props_none_returns_empty_string(self):
        node = HTMLNode(tag="p", value="hello", props=None)
        assert node.props_to_html() == ""

    def test_props_empty_dict_returns_empty_string(self):
        node = HTMLNode(tag="p", value="hello", props={})
        assert node.props_to_html() == ""

    def test_single_prop_has_leading_space(self):
        node = HTMLNode(tag="a", value="click", props={"href": "https://www.google.com"})
        assert node.props_to_html() == ' href="https://www.google.com"'

    def test_multiple_props_formatting(self):
        node = HTMLNode(
            tag="a",
            value="click",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        result = node.props_to_html()
        # Order depends on dict insertion order (Python 3.7+ preserves it)
        assert result == ' href="https://www.google.com" target="_blank"'

    def test_props_with_non_string_values(self):
        node = HTMLNode(tag="div", props={"tabindex": 0, "download": True})
        assert node.props_to_html() == ' tabindex="0" download="True"'
        
if __name__ == "__main__":
    unittest.main()