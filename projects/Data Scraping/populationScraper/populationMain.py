def population_function():
  import pandas as pd
  import sys
  import os
  import re

  sys.path.append('C:/Users/Admin/Music/hotdiggydidog/coding/python')
  from platformUpdateAutomation.population.excelScraper.excelPopulationScraper import run_excel_scraper

  excel_file = 'C:/Users/Admin/OneDrive - IT-Prime Solutions Provider/workFiles/workLoad/projectHamm/forPlatformUpdate/psaPopulationCount2024/3_Table B - Population and Annual PGR by Province, City, and Municipality - By Region - rev_0.xlsx'

  print("--------------------")

  print('Starting Excel scraper...')
  population_df = run_excel_scraper(excel_file)
  print('Excel scraping done!')

  print("--------------------")

  # output folder
  output_folder = 'C:/Users/Admin/Music/hotdiggydidog/coding/python/platformUpdateAutomation/population/output'

  print('Saving to Excel...')
  population_df.to_excel(f'{output_folder}/population.xlsx', index=False)
  print('Saved to Excel!')

  print("--------------------")