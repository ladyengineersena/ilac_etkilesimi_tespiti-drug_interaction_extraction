# -*- coding: utf-8 -*-
"""
Veri Ä°ÅŸleme YardÄ±mcÄ± FonksiyonlarÄ±
"""

import re
import json
from typing import List, Dict, Any


class VeriIslem:
    """Veri iÅŸleme yardÄ±mcÄ± sÄ±nÄ±fÄ±"""
    
    @staticmethod
    def metni_temizle(metin: str) -> str:
        """Metni temizler ve normalize eder"""
        if not isinstance(metin, str):
            # UTF-8 encoding kontrolÃ¼
            try:
                metin = str(metin).encode('utf-8').decode('utf-8')
            except:
                metin = str(metin)
        
        # Fazla boÅŸluklarÄ± temizle
        metin = re.sub(r'\s+', ' ', metin)
        # BaÅŸ ve sondaki boÅŸluklarÄ± temizle
        return metin.strip()
    
    @staticmethod
    def sonuclari_kaydet(sonuclar: List[Dict], dosya_adi: str = 'sonuclar.json'):
        """SonuÃ§larÄ± JSON dosyasÄ±na kaydeder"""
        with open(dosya_adi, 'w', encoding='utf-8') as f:
            json.dump(sonuclar, f, ensure_ascii=False, indent=2)
    
    @staticmethod
    def sonuclari_yukle(dosya_adi: str) -> List[Dict]:
        """JSON dosyasÄ±ndan sonuÃ§larÄ± yÃ¼kler"""
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    @staticmethod
    def metinleri_dosyadan_yukle(dosya_adi: str) -> List[str]:
        """Metinleri dosyadan yÃ¼kler (her satÄ±r bir metin)"""
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            return [satir.strip() for satir in f if satir.strip()]
