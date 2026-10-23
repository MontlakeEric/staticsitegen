import unittest
from extract_links import extract_markdown_images, extract_markdown_links


class TestExtractLinks(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_markdown_links_with_image(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_markdown_links_with_multiple_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com) and another [link](https://example.org)"
        )
        self.assertListEqual(
            [
                ("link", "https://example.com"),
                ("link", "https://example.org"),
            ],
            matches,
        )

    def test_extract_markdown_links_with_no_links(self):
        matches = extract_markdown_links("This is text with no links")
        self.assertListEqual([], matches)

    def test_extract_markdown_images_with_no_images(self):
        matches = extract_markdown_images("This is text with no images")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_with_image_and_link(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_markdown_images_with_image_and_link(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://example.com)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_with_image_and_link_and_multiple_links(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org)"
        )
        self.assertListEqual(
            [
                ("link", "https://example.com"),
                ("link", "https://example.org"),
            ],
            matches,
        )

    def test_extract_markdown_images_with_image_and_link_and_multiple_links(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_with_image_and_link_and_multiple_links_and_no_links(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org), and no links"
        )
        self.assertListEqual(
            [
                ("link", "https://example.com"),
                ("link", "https://example.org"),
            ],
            matches,
        )

    def test_extract_markdown_images_with_image_and_link_and_multiple_links_and_no_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org), and no images"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_with_image_and_link_and_multiple_links_and_no_links_and_no_images(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org), and no links, and no images"
        )
        self.assertListEqual(
            [
                ("link", "https://example.com"),
                ("link", "https://example.org"),
            ],
            matches,
        )

    def test_extract_markdown_images_with_image_and_link_and_multiple_links_and_no_links_and_no_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org), and no links, and no images"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_with_image_and_link_and_multiple_links_and_no_links_and_no_images_and_no_links(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org), and no links, and no images, and no links"
        )
        self.assertListEqual(
            [
                ("link", "https://example.com"),
                ("link", "https://example.org"),
            ],
            matches,
        )

    def test_extract_markdown_images_with_image_and_link_and_multiple_links_and_no_links_and_no_images_and_no_links(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org), and no links, and no images, and no links"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_with_image_and_link_and_multiple_links_and_no_links_and_no_images_and_no_links_and_no_links(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org), and no links, and no images, and no links, and no links"
        )
        self.assertListEqual(
            [
                ("link", "https://example.com"),
                ("link", "https://example.org"),
            ],
            matches,
        )

    def test_extract_markdown_images_with_image_and_link_and_multiple_links_and_no_links_and_no_images_and_no_links_and_no_links(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org), and no links, and no images, and no links, and no links"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_with_image_and_link_and_multiple_links_and_no_links_and_no_images_and_no_links_and_no_links_and_no_links(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org), and no links, and no images, and no links, and no links, and no links"
        )
        self.assertListEqual(
            [
                ("link", "https://example.com"),
                ("link", "https://example.org"),
            ],
            matches,
        )

    def test_extract_markdown_images_with_image_and_link_and_multiple_links_and_no_links_and_no_images_and_no_links_and_no_links_and_no_links(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org), and no links, and no images, and no links, and no links, and no links"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_with_image_and_link_and_multiple_links_and_no_links_and_no_images_and_no_links_and_no_links_and_no_links_and_no_links(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org), and no links, and no images, and no links, and no links, and no links, and no links"
        )
        self.assertListEqual(
            [
                ("link", "https://example.com"),
                ("link", "https://example.org"),
            ],
            matches,
        )

    def test_extract_markdown_images_with_image_and_link_and_multiple_links_and_no_links_and_no_images_and_no_links_and_no_links_and_no_links_and_no_links(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), a [link](https://example.com), and another [link](https://example.org), and no links, and no images, and no links, and no links, and no links, and no links"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_with_link_at_beginning(self):
        matches = extract_markdown_images(
            "![image](https://i.imgur.com/zjjcJKZ.png) This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_with_link_at_beginning(self):
        matches = extract_markdown_images(
            "[link1](https://example.com) is a link.  Here is an image: ![image1](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image1", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_with_image_at_beginning(self):
        matches = extract_markdown_images(
            "![image1](https://i.imgur.com/zjjcJKZ.png) This is text with a [link1](https://example.com)"
        )
        self.assertListEqual([("image1", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_with_image_at_beginning_and_multiple_images_in_text(self):
        matches = extract_markdown_images(
            "![image1](https://i.imgur.com/zjjcJKZ.png) This is text with another ![image2](https://i.imgur.com/another.png)"
        )
        self.assertListEqual(
            [
                ("image1", "https://i.imgur.com/zjjcJKZ.png"),
                ("image2", "https://i.imgur.com/another.png"),
            ],
            matches,
        )

    def test_extract_markdown_links_with_link_at_beginning(self):
        matches = extract_markdown_links(
            "[link1](https://example.com) This is text with another [link2](https://example.org)"
        )
        self.assertListEqual(
            [
                ("link1", "https://example.com"),
                ("link2", "https://example.org"),
            ],
            matches,
        )

if __name__ == "__main__":
    unittest.main()