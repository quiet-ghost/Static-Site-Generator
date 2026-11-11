import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, url="This is a text node")
        node2 = TextNode(
            "This is a text node", TextType.BOLD, url="This another is a text node"
        )
        self.assertNotEqual(node.url, node2.url)

    def test_TextNode(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This a second is a text node", TextType.CODE)
        self.assertNotEqual(node.text, node2.text)
        self.assertNotEqual(node.text_type, node2.text_type)
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()
