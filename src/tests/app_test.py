import unittest
from app import App


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_image_load_successful(self):
        images = ["src/media/dog1.png"]
        self.app.load_images(images)
        self.assertIsNot(self.app.images, [])
