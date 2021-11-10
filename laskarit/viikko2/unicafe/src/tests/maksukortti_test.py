import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_lataa_rahaa_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_maksu_kun_rahaa_on_tarpeeksi(self):
        self.assertTrue(self.maksukortti.ota_rahaa(3))

    def test_maksu_kun_rahaa_ei_ole_tarpeeksi(self):
        self.assertFalse(self.maksukortti.ota_rahaa(11))
