# -*- coding: utf-8 -*-
"""
Ä°liÅŸki Ã‡Ä±karÄ±mÄ± ModÃ¼lÃ¼ - Pattern-based ve ML-based extraction
"""

import re
from typing import List, Dict
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


class IliskiCikarim:
    """Ä°laÃ§lar arasÄ± iliÅŸki Ã§Ä±karÄ±mÄ± yapan sÄ±nÄ±f"""
    
    def __init__(self):
        """Ä°liÅŸki Ã§Ä±karÄ±m modelini baÅŸlat"""
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()
        
        # Ã–rnek veri iÃ§in
        self.ornek_veri = [
            "Aspirin ve warfarin birlikte kullanÄ±lmamalÄ±dÄ±r.",
            "Paracetamol gÃ¼venle kullanÄ±labilir.",
            "Ibuprofen ile aspirin aynÄ± anda alÄ±nmaz.",
            "Metformin genellikle gÃ¼venlidir."
        ]
    
    def pattern_tabanli_cikarim(self, cumle: str) -> Dict:
        """Pattern-based iliÅŸki Ã§Ä±karÄ±mÄ±"""
        iliski_tipleri = {
            'birlikte_kullanim': r'birlikte|aynÄ± anda|beraber',
            'kontrendikasyon': r'kullanma|alma|almayÄ±n|uzak dur',
            'uyarÄ±m': r'dikkat|dikkatli|kontrol',
            'artirici': r'artÄ±rÄ±r|artÄ±rÄ±r|yÃ¼kseltir|artÄ±rma',
            'azaltici': r'azaltÄ±r|dÃ¼ÅŸÃ¼rÃ¼r|azaltma'
        }
        
        sonuc = {
            'cumle': cumle,
            'iliskiler': []
        }
        
        for tip, pattern in iliski_tipleri.items():
            if re.search(pattern, cumle.lower()):
                sonuc['iliskiler'].append(tip)
        
        return sonuc
    
    def ml_tabanli_cikarim(self, cumle: str) -> Dict:
        """Machine Learning tabanlÄ± iliÅŸki Ã§Ä±karÄ±mÄ±"""
        # Basit Ã¶rnek implementasyon
        ozellik_vector = self.vectorizer.fit_transform([cumle])
        tahmin = self.model.predict(ozellik_vector)
        
        return {
            'cumle': cumle,
            'tahmin': tahmin[0],
            'olasilik': 0.85  # Ã–rnek
        }
