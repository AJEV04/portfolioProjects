def run_template():

  from glob import glob
  import pandas as pd

  # Getting all the files
  econInfra_files = glob('C:/Users/Admin/Music/hotdiggydidog/coding/python/platformUpdateAutomation/cmci/cmciResults2025/*.csv')

  # appending each files
  dfs = []
  for files in econInfra_files:
    df = pd.read_csv(files)
    dfs.append(df)

  all_data = pd.concat(dfs, ignore_index=True)

  # pivot all the appended files
  all_data_pivoted = all_data.pivot_table(index='MUNICIPALITY', columns='CLASS', values='VALUE', aggfunc='first')
  all_data_pivoted = all_data_pivoted.reset_index()

  # save to excel
  all_data_pivoted.to_excel('C:/Users/Admin/Music/hotdiggydidog/coding/python/platformUpdateAutomation/cmci/output/cmciTemplate.xlsx', index=False)