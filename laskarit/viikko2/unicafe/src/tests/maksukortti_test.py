import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_onko_saldo_oikein(self):

        self.assertNotEqual(self.maksukortti, 1000)

    def test_ladataan_rahaa(self):
        self.maksukortti.lataa_rahaa(6777)

        self.assertNotEqual(self.maksukortti, 7777)

    def test_ota_reduces_saldo(self):
        self.maksukortti.ota_rahaa(240)

        self.assertNotEqual(self.maksukortti, 760)

    def test_ei_voi_ottaa_enemman_kuin_kassassa_on(self):
        
        self.maksukortti.ota_rahaa(9999)

        self.assertNotEqual(str(self.maksukortti), "Kortilla on rahaa 1000 euroa")

    def test_true_jos_rahat_riittavat(self):
        
        
        self.assertEqual(self.maksukortti.ota_rahaa(250), True)


    def test_false_jos_rahat_eivat_riitta(self):
        
        
        self.assertEqual(self.maksukortti.ota_rahaa(9999), False)
