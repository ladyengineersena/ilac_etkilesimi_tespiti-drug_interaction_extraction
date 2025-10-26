# -*- coding: utf-8 -*-
"""
Ä°laÃ§ EtkileÅŸimi Tespiti - Ã–rnek KullanÄ±m
"""

from ilac_etkilesimi import IlacEtkilesimTespiti
from ilac_etkilesimi.veri_islem import VeriIslem


def ornek_1_basit_kullanim():
    """Basit kullanÄ±m Ã¶rneÄŸi"""
    print("=" * 60)
    print("Ã–rnek 1: Basit KullanÄ±m")
    print("=" * 60)
    
    tespit = IlacEtkilesimTespiti()
    
    metin = "Aspirin ve warfarin birlikte kullanÄ±ldÄ±ÄŸÄ±nda kanama riski artar."
    sonuc = tespit.analiz_et(metin)
    
    print(f"Metin: {metin}")
    print(f"\nTespit Edilen EtkileÅŸimler:")
    for etkilesim in sonuc:
        print(f"  - Ä°laÃ§lar: {', '.join(etkilesim['ilaclar'])}")
        print(f"  - TÃ¼rÃ¼: {etkilesim['turu']}")
        print(f"  - Seviye: {etkilesim['seviye']}")
    print()


def ornek_2_toplu_islem():
    """Toplu iÅŸlem Ã¶rneÄŸi"""
    print("=" * 60)
    print("Ã–rnek 2: Toplu Ä°ÅŸlem")
    print("=" * 60)
    
    tespit = IlacEtkilesimTespiti()
    
    metinler = [
        "Aspirin ile ibuprofen birlikte alÄ±nmamalÄ±dÄ±r.",
        "Paracetamol genellikle gÃ¼venlidir ve diÄŸer ilaÃ§larla etkileÅŸime girmez.",
        "Warfarin ve aspirin kombinasyonu tehlikelidir.",
        "Metformin ve insÃ¼lin birlikte kullanÄ±labilir ancak doktor kontrolÃ¼ ÅŸarttÄ±r.",
    ]
    
    sonuclar = tespit.toplu_analiz(metinler)
    
    for sonuc in sonuclar:
        print(f"\nMetin {sonuc['metin_id']}: {sonuc['metin']}")
        print(f"EtkileÅŸim SayÄ±sÄ±: {sonuc['etkilesim_sayisi']}")
        for etkilesim in sonuc['etkilesimler']:
            print(f"  -> Ä°laÃ§lar: {', '.join(etkilesim['ilaclar'])}")
            print(f"     CÃ¼mle: {etkilesim['cumle']}")
    print()


def ornek_3_dosyadan_okuma():
    """Dosyadan okuma Ã¶rneÄŸi"""
    print("=" * 60)
    print("Ã–rnek 3: Dosyadan Okuma")
    print("=" * 60)
    
    veri_islem = VeriIslem()
    
    # Ã–rnek metinler
    ornek_metin = """Aspirin ve warfarin birlikte kullanÄ±ldÄ±ÄŸÄ±nda kanama riski artar.
Paracetamol genellikle gÃ¼venlidir.
Ibuprofen ile aspirin aynÄ± anda alÄ±nmamalÄ±dÄ±r.
Metformin genellikle gÃ¼venli bir ilaÃ§tÄ±r."""
    
    # Dosyaya yaz
    with open('data/ornek_metinler.txt', 'w', encoding='utf-8') as f:
        f.write(ornek_metin)
    
    # Dosyadan oku
    metinler = veri_islem.metinleri_dosyadan_yukle('data/ornek_metinler.txt')
    
    tespit = IlacEtkilesimTespiti()
    sonuclar = tespit.toplu_analiz(metinler)
    
    # SonuÃ§larÄ± kaydet
    veri_islem.sonuclari_kaydet(sonuclar, 'data/sonuclar.json')
    print("SonuÃ§lar 'data/sonuclar.json' dosyasÄ±na kaydedildi.")
    print()


if __name__ == "__main__":
    # Ã–rnekleri Ã§alÄ±ÅŸtÄ±r
    ornek_1_basit_kullanim()
    ornek_2_toplu_islem()
    ornek_3_dosyadan_okuma()
    
    print("=" * 60)
    print("TÃ¼m Ã¶rnekler baÅŸarÄ±yla tamamlandÄ±!")
    print("=" * 60)
