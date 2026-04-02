# 🇵🇭 Philippine Government Data Scraper

A collection of Python scripts that extract publicly available government 
data from Philippine government websites and reports. Built to support 
data analysis workflows — originally developed for internal reporting 
at Unilever Philippines.

---

## 📁 Project Structure
```
data-scraper/
├── main.py               # runs all scrapers at once
├── cmci/
│   ├── cmci_scraper.py   # scrapes CMCI competitiveness data
│   └── output/
├── revenue/
│   ├── revenue_scraper.py # extracts COA revenue data from PDFs
│   └── output/
└── population/
    ├── population_scraper.py # collects PSA population data
    └── output/
```

---

## 🛠️ Tools & Libraries

- **Python** — core language
- **Playwright** — web scraping and browser automation
- **pdfplumber** — extracting data from PDF reports
- **Pandas** — data cleaning and CSV export

---

## 📊 Data Sources

All data extracted is publicly available:

| Script | Source | Website |
|---|---|---|
| cmci_scraper.py | DTI Competitiveness Data | cmci.dti.gov.ph |
| revenue_scraper.py | COA Audit Reports | coa.gov.ph |
| population_scraper.py | PSA Population Data | psa.gov.ph |

---

## 🚀 How to Run

**Install dependencies:**
```
pip install playwright pdfplumber pandas
playwright install
```

**Run all scrapers at once:**
```
python main.py
```

**Run individual scrapers:**
```
python cmci/cmci_scraper.py
python revenue/revenue_scraper.py
python population/population_scraper.py
```

---

## 📂 Output

Each scraper saves a clean `.xlsx` file inside its `output/` folder:
- `cmci/output/cmci_data.csv`
- `revenue/output/revenue_data.csv`
- `population/output/population_data.csv`

---

## 📝 Notes

- All data sources are publicly released by Philippine government agencies
- No confidential or proprietary data is included
- Scripts were built for legitimate data analysis purposes

---
