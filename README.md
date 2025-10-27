# Drug Interaction Extraction

This project aims to detect and extract drug interactions from texts using Natural Language Processing (NLP) techniques.

## Features

- Turkish text support
- UTF-8 character encoding support
- Named Entity Recognition (NER) to identify drug names
- Relationship extraction to detect drug interactions
- Risk level assessment
- Machine learning-based classification

## Installation

### Requirements

- Python 3.8+
- pip

### Steps

1. Clone the repository:
```bash
git clone https://github.com/ladyengineersena/ilac_etkilesimi_tespiti-drug_interaction_extraction.git
cd ilac_etkilesimi_tespiti-drug_interaction_extraction
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from ilac_etkilesimi import IlacEtkilesimTespiti

# Initialize the model
tespit = IlacEtkilesimTespiti()

# Find drug interactions in text
metin = "Aspirin ve warfarin birlikte kullanildiginda kanama riski artar."
etkilesimler = tespit.analiz_et(metin)

print(etkilesimler)
```

### Batch Processing

```python
# Process multiple texts
metinler = [
    "Aspirin ile ibuprofen birlikte alinmamalidir.",
    "Paracetamol genellikle guvenlidir."
]

sonuclar = tespit.toplu_analiz(metinler)
```

## Project Structure

```
ilac-etkilesimi-tespiti/
â”œâ”€â”€ ilac_etkilesimi/
â”‚   â”œâ”€â”€ __init__.py
â”‚   â”œâ”€â”€ nlp_model.py         # NLP model and processing
â”‚   â”œâ”€â”€ iliski_ciikarim.py    # Relationship extraction algorithm
â”‚   â””â”€â”€ veri_islem.py         # Data processing helpers
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

## Contributing

1. Fork this repository
2. Create a feature branch (git checkout -b feature/NewFeature)
3. Commit your changes (git commit -m "Added new feature")
4. Push to your branch (git push origin feature/NewFeature)
5. Create a Pull Request

## License

This project is licensed under the MIT License.

## Contact

You can open an issue for questions.

## Acknowledgments

- NLTK
- spaCy
- scikit-learn
