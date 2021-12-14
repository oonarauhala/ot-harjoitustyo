import unittest
from pygame import Surface
from entities.image_loader import ImageLoader


class TestImageLoader(unittest.TestCase):
    def setUp(self):
        self.image_loader = ImageLoader()

    def test_view_1_image_load_returns_5_images(self):
        image_list = self.image_loader.load_view_images(1)
        self.assertEqual(len(image_list), 5)

    def test_view_2_image_load_returns_4_images(self):
        image_list = self.image_loader.load_view_images(2)
        self.assertEqual(len(image_list), 4)

    def test_load_background_returns_one_surface(self):
        surface = self.image_loader.load_background()
        self.assertIsInstance(surface, Surface)
