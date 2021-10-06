#%%

import pandas as pd 
from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
import datetime 

today = datetime.datetime.today()
today = datetime.datetime.strftime(today, "%Y-%m-%d")


chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Firefox(options=chrome_options)
driver.implicitly_wait(10)

start_url = 'https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/coronavirus-covid-19-case-numbers-and-statistics'


#%%
driver.get(start_url)

#%%

tables = pd.read_html(driver.page_source.encode("utf-8"))

i = 0

## Need to wait while all the tables load
while len(tables) < 10:
    driver.implicitly_wait(10)
    tables = pd.read_html(driver.page_source.encode("utf-8"))
    i += 1

    if i > 500:
        print("Break")
        break

names = {0:"recent_cases", 1:"total_cases", 2:"cases_age_sex",
 3:"deaths_age_sex", 4:"tests", 5:"hospitalisations", 6:"ndis",
  7:"aged_care_resi", 8:"aged_care_home", 9:"oecd_mortality"}

if len(tables) >= 10:


    i = 0
    for table in tables:
        print(i)
        i += 1
        print(table)
        print(table.columns)
        table['Date'] = today
        title = f"{today}_{names[i]}"
        with open(f"covid-summary-stats/data/{title}.csv", "w") as f:
            table.to_csv(f, index=False, header=True)
    

