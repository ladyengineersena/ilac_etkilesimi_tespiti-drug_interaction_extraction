# -*- coding: utf-8 -*-
"""
Ä°laÃ§ EtkileÅŸimi Tespiti - Test DosyasÄ±
"""

import unittest
from ilac_etkilesimi import IlacEtkilesimTespiti
from ilac_etkilesimi.veri_islem import VeriIslem


class TestIlacEtkilesimi(unittest.TestCase):
    """Test sÄ±nÄ±fÄ±"""
    
    def setUp(self):
        """Her test Ã¶ncesi Ã§alÄ±ÅŸÄ±r"""
        self.tespit = IlacEtkilesimTespiti()
    
    def test_basit_etkilesim_bulma(self):
        """Basit etkileÅŸim bulma testi"""
        metin = "Aspirin ve warfarin birlikte kullanÄ±lmamalÄ±dÄ±r."
        sonuclar = self.tespit.analiz_et(metin)
        
        # En az bir etkileÅŸim bulunmalÄ±
        self.assertGreater(len(sonuclar), 0)
        
        if len(sonuclar) > 0:
            # Ä°laÃ§lar listesi olmalÄ±
            self.assertIn('ilaclar', sonuclar[0])
            self.assertIn('turu', sonuclar[0])
            self.assertIn('seviye', sonuclar[0])
    
    def test_utf8_encoding(self):
        """UTF-8 encoding testi"""
        # TÃ¼rkÃ§e karakterler iÃ§eren metin
        metin = "Aspirin ve ibuprofen birlikte kullanÄ±ldÄ±ÄŸÄ±nda mide problemleri oluÅŸabilir."
        sonuclar = self.tespit.analiz_et(metin)
        
        # Hata fÄ±rlatmamalÄ±
        self.assertIsInstance(sonuclar, list)
    
    def test_topl_analiz(self):
        """Toplu analiz testi"""
        metinler = [
            "Aspirin gÃ¼venli bir ilaÃ§tÄ±r.",
            "Warfarin ve aspirin birlikte kullanÄ±lmaz."
        ]
        
        sonuclar = self.tespit.toplu_analiz(metinler)
        
        # Ä°ki sonuÃ§ olmalÄ±
        self.assertEqual(len(sonuclar), 2)
        
        # Her sonuÃ§ metin_id iÃ§ermeli
        for sonuc in sonuclar:
            self.assertIn('metin_id', sonuc)
            self.assertIn('etkilesim_sayisi', sonuc)
            self.assertIn('etkilesimler', sonuc)
    
    def test_veri_temizleme(self):
        """Veri temizleme testi"""
        veri_islem = VeriIslem()
        
        kirli_metin = "  Aspirin   ve   warfarin  birlikte  kullanÄ±lÄ±r.  "
        temiz_metin = veri_islem.metni_temizle(kirli_metin)
        
        # Fazla boÅŸluklar temizlenmeli
        self.assertNotIn("  ", temiz_metin)
        self.assertEqual(temiz_metin[0], 'A')  # BaÅŸÄ±nda boÅŸluk olmamalÄ±


if __name__ == '__main__':
    unittest.main()
