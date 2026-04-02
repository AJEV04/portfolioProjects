def cmci_function():
  # main file
  import time
  import sys
  import os

  sys.path.append('C:/Users/Admin/Music/hotdiggydidog/coding/python')

  from platformUpdateAutomation.cmci.scraper.econInfraScraper import run_scraper
  from platformUpdateAutomation.cmci.saveToTemplate.econInfraTemplate import run_template

  start = time.time()

  # first run scraper
  print("Starting scraper...")
  run_scraper()
  print("Done scraping.")

  print("--------------------")

  # second run the template
  print("Saving to template...")
  run_template()
  print("All done.")
  
  print("--------------------")

  # calculates how long the script runs (run times differs from internet)
  end = time.time()
  elapsed = (end - start)

  minutes = elapsed // 60
  seconds = elapsed % 60


  print(f"Total time: {int(minutes)} minutes and {seconds:.2f} seconds")