import unittest
from kassapaate import Kassapaate

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
    
        kassa = Kassapaate()
        self.maksu = 10000

    def test_myytyjen_edullisten_maara(self):

        x = 10
        i = 0

        while i < x:
            self.kassa.syo_edullisesti_kateisella(self.maksu)

        assertNotEqual(x, self.kassa.edulliset)

            
