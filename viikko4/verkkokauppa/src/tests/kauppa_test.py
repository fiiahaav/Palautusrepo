import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock.saldo.side_effect = lambda tuote_id: 10 if tuote_id in [1,2] else 0
        
        
        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "leipä", 3)
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
    def test_yksi_tuote(self):
        # Yksi tuote ostoskoriin
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        # Varmistetaan, että tilisiirto kutsuttu oikein
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)

    def test_kaksi_eri_tuotetta(self):
        # Kaksi eri tuotetta ostoskoriin
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("matti", "54321")
        self.pankki_mock.tilisiirto.assert_called_with("matti", 42, "54321", ANY, 8)

    
    def test_kaksi_samaa_tuotetta(self):
        # Kaksi samaa tuotetta ostoskoriin
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("liisa", "11111")
        self.pankki_mock.tilisiirto.assert_called_with("liisa", 42, "11111", ANY, 10)

    def test_tuote_ja_loppu_tuote(self):
        # Tuote 2 loppu
        self.varasto_mock.saldo.side_effect = lambda tuote_id: 10 if tuote_id == 1 else 0
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("sari", "99999")
        # Varmistetaan, että vain saatavilla oleva tuote laskutetaan
        self.pankki_mock.tilisiirto.assert_called_with("sari", 42, "99999", ANY, 5)

if __name__ == "__main__":
    unittest.main()
