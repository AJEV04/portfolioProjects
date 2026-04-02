import pdfplumber
import re
import pandas as pd

def scrape_revenue(pdf_file, pages, label):
  with pdfplumber.open(pdf_file) as pdf:
    all_records = []
    current_region = None # carries region name across pages
    skip_component = False

    for page in pages:
      # print("Currently on page:", page.page_number)

      table = page.extract_tables()

      for j in range(len(table[0])):
        row = table[0][j]
        # skips rows where first cell is none
        if row[0] is None:
          continue

        first_cell = row[0].strip()
        # skips rows we don't need
        if first_cell == 'Cities':
          continue
        if first_cell == 'Municipalities':
          continue
        if 'Regional Total' in first_cell:
          continue
        if 'GRAND TOTAL' in first_cell:
          continue

        # split the cell by newline
        lines = first_cell.split('\n')

        clean_cities = []
        skip_indices = [] # tracks which positions to skip
        component_index = 0 # tracks current position
        
        for line in lines:
          line = line.strip()

          if line == '':
            continue
          if 'Component' in line:
            skip_component = True
            continue
          if line[0].isdigit():
            if skip_component:
              skip_indices.append(component_index)  # remembers this position
              component_index += 1
              continue
            clean_city = re.sub(r'\d+', '', line)
            clean_city = clean_city.strip()
            clean_cities.append(clean_city)
            component_index += 1
          else:
              current_region = line
              skip_component = False

        # print('Region:', current_region)
        # print('Cities:', clean_cities)
        # print('------')

        revenues_raw = row[4]

        revenue_list = []

        if revenues_raw is not None:
          revenues = revenues_raw.split('\n')

          clean_revenues = []
          for revenue in revenues:
            stripped = revenue.strip()
            if stripped:
              # fix spaces inside numbers
              stripped = re.sub(r'(\d)\s+(\d)', r'\1\2', stripped)
              # fix negative numbers, instead of parenthesis it uses negative
              stripped = re.sub(r'\(\s*([\d,]+)\s*\)', r'-\1', stripped)
              # remove commas
              stripped = stripped.replace(',', '')
              clean_revenues.append(stripped)
          # now skips the positions that belong to component units
          for idx in range(len(clean_revenues)):
            if idx not in skip_indices:
              revenue_list.append(clean_revenues[idx])

        # print('Region:', current_region)
        # print('Cities:', clean_cities)
        # print('Revenues:', revenue_list)
        # print('------')
        # print(len(clean_cities) == len(revenue_list))

        for i in range(len(clean_cities)):
          record = {}
          record['REGION'] = current_region
          record[label] = clean_cities[i]
          record['REVENUE'] = revenue_list[i]
          all_records.append(record)
  df = pd.DataFrame(all_records)
  return df

def run_pdf_scraper(pdf_file):
  with pdfplumber.open(pdf_file) as pdf:
    print('Scraping cities...')
    cities_df = scrape_revenue(pdf_file, list(pdf.pages[178:184]), 'CITIES') # 2024(178:184) 2023(172:178)
    print('Cities done!')

    print('Scraping municipalities...')
    municipalities_df = scrape_revenue(pdf_file, list(pdf.pages[185:234]), 'MUNICIPALITIES') # 2024(185:234) 2023(179:228)
    print('Municipalities done!')

    return cities_df, municipalities_df