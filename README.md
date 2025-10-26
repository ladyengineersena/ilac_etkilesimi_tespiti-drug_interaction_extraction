# Ä°laÃ§ EtkileÅŸimi Tespiti (Drug Interaction Extraction)

Bu proje, doÄŸal dil iÅŸleme (NLP) teknikleri kullanarak metinlerden ilaÃ§ etkileÅŸimlerini tespit etmeyi ve Ã§Ä±karmayÄ± amaÃ§lamaktadÄ±r.

## Ã–zellikler

- TÃ¼rkÃ§e metin desteÄŸi
- UTF-8 karakter encoding desteÄŸi
- Named Entity Recognition (NER) ile ilaÃ§ isimlerini bulma
- Ä°liÅŸki Ã§Ä±karÄ±mÄ± (relationship extraction) ile ilaÃ§ etkileÅŸimlerini tespit etme
- Risk seviyesi belirleme
- Makine Ã¶ÄŸrenmesi tabanlÄ± sÄ±nÄ±flandÄ±rma

## Kurulum

### Gereksinimler

- Python 3.8+
- pip

### AdÄ±mlar

1. Repository'yi klonlayÄ±n:
```bash
git clone https://github.com/ladyengineersena/ilac_etkilesimi_tespiti-drug_interaction_extraction.git
cd ilac_etkilesimi_tespiti-drug_interaction_extraction
```

2. Sanal ortam oluÅŸturun (Ã¶nerilir):
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

3. Gerekli paketleri yÃ¼kleyin:
```bash
pip install -r requirements.txt
```

## KullanÄ±m

### Temel KullanÄ±m

```python
from ilac_etkilesimi import IlacEtkilesimTespiti

# Modeli baÅŸlat
tespit = IlacEtkilesimTespiti()

# Metindeki ilaÃ§ etkileÅŸimlerini bul
metin = "Aspirin ve warfarin birlikte kullanÄ±ldÄ±ÄŸÄ±nda kanama riski artar."
etkilesimler = tespit.analiz_et(metin)

print(etkilesimler)
```

### Toplu Ä°ÅŸleme

```python
# Birden fazla metin iÃ§in iÅŸlem
metinler = [
    "Aspirin ile ibuprofen birlikte alÄ±nmamalÄ±dÄ±r.",
    "Paracetamol genellikle gÃ¼venlidir."
]

sonuclar = tespit.toplu_analiz(metinler)
```

## Proje YapÄ±sÄ±

```
ilac-etkilesimi-tespiti/
â”œâ”€â”€ ilac_etkilesimi/
â”‚   â”œâ”€â”€ __init__.py
â”‚   â”œâ”€â”€ nlp_model.py         # NLP model ve iÅŸleme
â”‚   â”œâ”€â”€ iliski_ciikarim.py    # Ä°liÅŸki Ã§Ä±karÄ±mÄ± algoritmasÄ±
â”‚   â””â”€â”€ veri_islem.py         # Veri iÅŸleme yardÄ±mcÄ±larÄ±
â”œâ”€â”€ data/
â”‚   â””â”€â”€ ornek_metinler.txt
â”œâ”€â”€ examples/
â”‚   â””â”€â”€ ornek_kullanim.py
â”œâ”€â”€ tests/
â”‚   â””â”€â”€ test_ilac_etkilesimi.py
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ setup.py
â”œâ”€â”€ .gitignore
â””â”€â”€ README.md
```

## KatkÄ±da Bulunma

1. Bu repository'yi fork edin
2. Bir feature branch oluÅŸturun (git checkout -b feature/YeniOzellik)
3. DeÄŸiÅŸikliklerinizi commit edin (git commit -m "Yeni Ã¶zellik eklendi")
4. Branch'inizi push edin (git push origin feature/YeniOzellik)
5. Bir Pull Request oluÅŸturun

## Lisans

Bu proje MIT lisansÄ± altÄ±nda lisanslanmÄ±ÅŸtÄ±r.

## Ä°letiÅŸim

SorularÄ±nÄ±z iÃ§in issue aÃ§abilirsiniz.

## TeÅŸekkÃ¼rler

- NLTK
- spaCy
- scikit-learn
