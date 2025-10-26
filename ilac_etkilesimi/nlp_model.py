# -*- coding: utf-8 -*-
"""
NLP Modeli - Ä°laÃ§ EtkileÅŸimi Tespiti
TÃ¼rkÃ§e karakter desteÄŸi ile UTF-8 encoding
"""

import re
import string
from typing import List, Dict, Tuple
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# TÃ¼rkÃ§e karakter kontrolÃ¼
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
except:
    pass


class IlacEtkilesimTespiti:
    """Ä°laÃ§ etkileÅŸimleri tespit eden NLP modeli"""
    
    def __init__(self):
        """Modeli baÅŸlat"""
        self.encoding = 'utf-8'
        self.ilac_etkilesim_kelimeleri = [
            'etkileÅŸim', 'etkileÅŸimi', 'etkileÅŸir', 'birlikte',
            'aynÄ± anda', 'karÄ±ÅŸÄ±m', 'Ã§akÄ±ÅŸma', 'uyumsuzluk',
            'rizkli', 'tehlikeli', 'kullanÄ±lmamalÄ±', 'kaÃ§Ä±n',
            'uzak dur', 'almayÄ±n', 'kullanmayÄ±n'
        ]
        
        # TÃ¼rkÃ§e stopwords
        try:
            self.stop_words = set(stopwords.words('turkish'))
        except:
            self.stop_words = set()
    
    def analiz_et(self, metin: str) -> List[Dict]:
        """
        Metindeki ilaÃ§ etkileÅŸimlerini analiz eder
        
        Args:
            metin: Analiz edilecek metin
            
        Returns:
            Ä°laÃ§ etkileÅŸimlerinin listesi
        """
        if not isinstance(metin, str):
            raise ValueError("Metin string olmalÄ±dÄ±r")
        
        # UTF-8 encoding kontrolÃ¼
        metin = metin.encode('utf-8').decode('utf-8')
        
        etkilesimler = []
        
        # Ä°laÃ§ isimleri bulma
        ilaclar = self._ilaclari_bul(metin)
        
        if len(ilaclar) < 2:
            return []
        
        # CÃ¼mlelere bÃ¶l
        cumleler = self._cumlelere_bol(metin)
        
        # Her cÃ¼mle iÃ§in etkileÅŸim kontrolÃ¼
        for cumle in cumleler:
            etkilesim = self._etkilesim_var_mi(cumle, ilaclar)
            if etkilesim:
                etkilesimler.append(etkilesim)
        
        return etkilesimler
    
    def _ilaclari_bul(self, metin: str) -> List[Dict]:
        """Metindeki olasÄ± ilaÃ§ isimlerini bulur"""
        ilaclar = []
        
        # BÃ¼yÃ¼k harfle baÅŸlayan kelimeler (ilaÃ§ isimleri genelde Ã¶zel isim)
        pattern = r'\b[A-ZÃ‡ÄÄ°Ã–ÅÃœ][a-zÃ§ÄŸÄ±Ã¶ÅŸÃ¼]+\b'
        bulunanlar = re.findall(pattern, metin)
        
        # Benzersiz ilaÃ§ isimleri
        benzersiz_ilaclar = list(set(bulunanlar))
        
        for idx, ilac in enumerate(benzersiz_ilaclar):
            # Stopword deÄŸilse ekle
            if ilac.lower() not in self.stop_words:
                # Ä°laÃ§ isminin pozisyonunu bul
                pozisyon = metin.find(ilac)
                ilaclar.append({
                    'isim': ilac,
                    'pozisyon': pozisyon,
                    'id': idx + 1
                })
        
        return ilaclar
    
    def _cumlelere_bol(self, metin: str) -> List[str]:
        """Metni cÃ¼mlelere bÃ¶ler"""
        # Basit cÃ¼mle ayÄ±rÄ±cÄ±
        cumleler = re.split(r'[.!?]+', metin)
        # BoÅŸ cÃ¼mleleri filtrele
        return [c.strip() for c in cumleler if c.strip()]
    
    def _etkilesim_var_mi(self, cumle: str, ilaclar: List[Dict]) -> Dict:
        """CÃ¼mlede ilaÃ§ etkileÅŸimi var mÄ± kontrol eder"""
        cumle_lower = cumle.lower()
        
        # EtkileÅŸim anahtar kelimelerini kontrol et
        etkilesim_kelimeleri_bulundu = any(
            kelime in cumle_lower 
            for kelime in self.ilac_etkilesim_kelimeleri
        )
        
        if not etkilesim_kelimeleri_bulundu:
            return None
        
        # CÃ¼mledeki ilaÃ§larÄ± bul
        cumle_ilaclari = []
        for ilac in ilaclar:
            if ilac['isim'].lower() in cumle_lower:
                cumle_ilaclari.append(ilac)
        
        if len(cumle_ilaclari) >= 2:
            return {
                'cumle': cumle,
                'ilaclar': [i['isim'] for i in cumle_ilaclari],
                'turu': self._etkilesim_turunu_belirle(cumle_lower),
                'seviye': self._risk_seviyesi_belirle(cumle_lower)
            }
        
        return None
    
    def _etkilesim_turunu_belirle(self, cumle: str) -> str:
        """EtkileÅŸim tÃ¼rÃ¼nÃ¼ belirler"""
        if 'tehlikeli' in cumle or 'risk' in cumle:
            return 'YÃ¼ksek Risk'
        elif 'kaÃ§Ä±n' in cumle or 'almayÄ±n' in cumle:
            return 'Ã–nerilmez'
        elif 'uygunsuz' in cumle or 'uyumsuz' in cumle:
            return 'Uyumsuzluk'
        else:
            return 'Dikkat Gerekli'
    
    def risk_seviyesi_belirle(self, cumle: str) -> str:
        """Risk seviyesini belirler"""
        if 'tehlikeli' in cumle or 'Ã¶lÃ¼m' in cumle:
            return 'Kritik'
        elif 'ciddi' in cumle or 'Ã¶nemli' in cumle:
            return 'YÃ¼ksek'
        elif 'dikkat' in cumle:
            return 'Orta'
        else:
            return 'DÃ¼ÅŸÃ¼k'
    
    def toplu_analiz(self, metinler: List[str]) -> List[Dict]:
        """Birden fazla metin iÃ§in toplu analiz"""
        sonuclar = []
        for idx, metin in enumerate(metinler):
            etkilesimler = self.analiz_et(metin)
            sonuclar.append({
                'metin_id': idx + 1,
                'metin': metin,
                'etkilesimler': etkilesimler,
                'etkilesim_sayisi': len(etkilesimler)
            })
        return sonuclar
    
    def _risk_seviyesi_belirle(self, cumle: str) -> str:
        """Risk seviyesini belirler (private helper)"""
        return self.risk_seviyesi_belirle(cumle)
