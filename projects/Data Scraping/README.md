# 🇵🇭 Philippine Government Data Scraper

A collection of Python scripts that extract publicly available government 
data from Philippine government websites and reports. Built to support 
data analysis workflows — originally developed for internal reporting 
at Unilever Philippines.

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

**Run individual scrapers:**
```
python cmci/cmci_scraper.py
python revenue/revenue_scraper.py
python population/population_scraper.py
```

---

## 📝 Notes

- All data sources are publicly released by Philippine government agencies
- No confidential or proprietary data is included
- Scripts were built for legitimate data analysis purposes

- To reproduce the outputs, you will need to reconfigure the scripts to match 
your local setup. This includes:
- Updating file paths to match your directory structure
- Installing the required dependencies
- Setting up Playwright for your environment

The scripts were built and tested on a specific local machine setup 
and may require adjustments before running on a different system.

---
