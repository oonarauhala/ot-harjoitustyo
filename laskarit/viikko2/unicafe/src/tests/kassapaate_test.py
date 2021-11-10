import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_rahamaara_oikein_myynnin_jalkeen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100880)

    def test_maukkaat_maara_oikein_myynnin_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_maara_oikein_myynnin_jalkeen(self):
        self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaat_maara_oikein_epaonnistunut_myynti(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edulliset_maara_oikein_epaonnistunut_myynti(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_vaihtoraha_oikea_edulliset(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(vaihtoraha, 10)

    def test_vaihtoraha_oikea_maukkaat(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(440)
        self.assertEqual(vaihtoraha, 40)

    def test_rahamaara_epaonnistunut_myynti_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahamaara_epaonnistunut_myynti_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_vaihtoraha_epaonnistunut_maksu_edulliset(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_vaihtoraha_epaonnistunut_maksu_maukkaat(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_korttimaksu_oikea_valoitus_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 760)

    def test_korttimaksu_oikea_veloitus_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 600)

    def test_korttimaksu_oikea_palautus_edulliset(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti))

    def test_korttimaksu_oikea_palautus_maukkaat(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))

    def test_korttimaksu_maukkaat_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttimaksu_edulliset_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_fail_korttimaksu_edulliet_rahamaara(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 100)

    def test_fail_korttimaksu_maukkaat_rahamaara(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 100)

    def test_fail_korttimaksu_edulliset_maara(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_fail_korttimaksu_maukkaat_maara(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_fail_korttimaksu_maukkaat_palautus(self):
        self.kortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))

    def test_fail_korttimaksu_edulliset_palautus(self):
        self.kortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.kortti))

    def test_kassan_rahamaara_oikein_korttimaksun_jalkeen(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataus_saldo_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo, 2000)

    def test_kortin_lataus_kassapaatteen_saldo_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_lataa_negatiivinen_summa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -300)
        self.assertEqual(self.kortti.saldo, 1000)
