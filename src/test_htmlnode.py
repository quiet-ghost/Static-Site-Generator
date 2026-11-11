import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a text node", None, None)
        node2 = HTMLNode("p", "This is a text node", None, None)
        self.assertNotEqual(node, node2)

    def test_props(self):
        node = HTMLNode(
            "div", "This is a text node", None, {"href": "https://example.com"}
        )
        node2 = HTMLNode(
            "div", "This is a text node", None, {"href": "https://example.com"}
        )
        node3 = HTMLNode(
            "div", "This is a text node", None, {"href": "https://another.com"}
        )
        self.assertEqual(node.props, node2.props)
        self.assertNotEqual(node.props, node3.props)

    def test_repr(self):
        node = HTMLNode(
            "div", "This is a text node", None, {"href": "https://example.com"}
        )
        expected_repr = "HTMLNode(tag=div, value=This is a text node, children=None, props={'href': 'https://example.com'})"
        self.assertEqual(repr(node), expected_repr)
