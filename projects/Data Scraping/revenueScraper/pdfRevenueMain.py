def revenue_function():
  import pandas as pd
  import sys
  import os
  import re

  sys.path.append('C:/Users/Admin/Music/hotdiggydidog/coding/python')
  from platformUpdateAutomation.revenue.pdfScraper.pdfRevenueScraper import run_pdf_scraper

  pdf_file = "C:/Users/Admin/OneDrive - IT-Prime Solutions Provider/workFiles/workLoad/projectHamm/forPlatformUpdate/revenue/2024-Annual-Financial-Report-for-the-Local-Government-Including-Bangsamoro-Government-Volume-I.pdf"

  # extract year
  year = re.search(r'\d{4}', os.path.basename(pdf_file))
  year = year.group()
  print(f'Year detected: {year}')

  print("--------------------")

  print('Starting PDF scraper...')
  cities_df, municipalities_df = run_pdf_scraper(pdf_file)
  print('PDF scraping done!')

  print("--------------------")

  # output folder
  output_folder = 'C:/Users/Admin/Music/hotdiggydidog/coding/python/platformUpdateAutomation/revenue/output'

  print('Saving to Excel...')
  cities_df.to_excel(f'{output_folder}/citiesRevenue{year}.xlsx', index=False)
  municipalities_df.to_excel(f'{output_folder}/municipalitiesRevenue{year}.xlsx', index=False)
  print('Saved to Excel!')

  print("--------------------")