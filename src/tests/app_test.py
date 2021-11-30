import unittest
from app import App


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_app_init(self):
        self.assertEqual(self.app.ui_sprites, [])
