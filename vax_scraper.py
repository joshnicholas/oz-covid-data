#%%

import pandas as pd 
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
import datetime 
import pytz
import time

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
today = utc_now.astimezone(pytz.timezone("Australia/Brisbane"))
today = today.strftime('%Y-%m-%d')

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Firefox(options=chrome_options)

start_url = 'https://www.health.gov.au/initiatives-and-programs/covid-19-vaccines/numbers-statistics'

#%%
driver.get(start_url)
driver.implicitly_wait(15)
time.sleep(15)

#%%

tables = pd.read_html(driver.page_source.encode("utf-8"))

print(len(tables))

out_path = 'vax_data'

for i in range(0,len(tables)):
  inter = tables[i]
  inter['Date'] = today
  title = f"{today}_{i}"

  with open(f"{out_path}/{title}.csv", 'w') as f:
    inter.to_csv(f, index=False, header=True)

  p = inter

  print(p)
  print(p.columns.tolist())




# print(tables)
# %%
