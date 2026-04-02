import pandas as pd

def scrape_population(excel_file):
    sheet_file = pd.ExcelFile(excel_file)
    sheet_names = sheet_file.sheet_names

    all_data = []

    for sheet_name in sheet_names:

        sheets = pd.read_excel(excel_file, sheet_name=sheet_name, usecols='A, F')
        sheets.columns = ['AREA', 'POPULATION']
        sheets = sheets.dropna().reset_index(drop=True)

        all_data.append(sheets)

    final_df = pd.concat(all_data, ignore_index=True)

    final_df['ID'] = final_df.index

    final_df = final_df[['ID', 'AREA', 'POPULATION']]

    return final_df

def run_excel_scraper(excel_file):
    print('Scraping population...')
    population_df = scrape_population(excel_file)
    print('Population done!')

    return population_df