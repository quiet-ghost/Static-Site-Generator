import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links


class test_extract_markdown_images(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_with_alt_text(self):
        matches = extract_markdown_images(
            "This is text with an ![alt text](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("alt text", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_with_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image1](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [
                ("image1", "https://i.imgur.com/zjjcJKZ.png"),
                ("image2", "https://i.imgur.com/zjjcJKZ.png"),
            ],
            matches,
        )


class test_extract_markdown_links(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.example.com)"
        )
        self.assertListEqual([("link", "https://www.example.com")], matches)

    def test_extract_markdown_links_with_multiple_links(self):
        matches = extract_markdown_links(
            "This is text with a [link1](https://www.example.com) and another [link2](https://www.example2.com)"
        )
        self.assertListEqual(
            [
                ("link1", "https://www.example.com"),
                ("link2", "https://www.example2.com"),
            ],
            matches,
        )
