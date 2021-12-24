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
# chrome_options.add_argument("--headless")

driver = webdriver.Firefox(options=chrome_options)


start_url = 'https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/coronavirus-covid-19-case-numbers-and-statistics'


#%%
driver.get(start_url)
# driver.implicitly_wait(35)
time.sleep(10)

#%%

tables = pd.read_html(driver.page_source.encode("utf-8"))

i = 0

## Need to wait while all the tables load
while len(tables) < 9:
    print(i, len(tables))
    # driver.implicitly_wait(10)
    time.sleep(1)
    tables = pd.read_html(driver.page_source.encode("utf-8"))
    i += 1

    if i > 600:
        print("Break")
        driver.close()
        break

names = {0:"recent_cases", 1:"total_cases", 2:"cases_age_sex",
 3:"deaths_age_sex", 4:"tests", 5:"hospitalisations", 6:"ndis",
  7:"aged_care_resi", 8:"aged_care_home", 9:"oecd_mortality"}

if len(tables) >= 9:


    i = 0
    for table in tables:
        # print(i)
        # print(table)
        # print(table.columns)
        table['Date'] = today
        title = f"{today}_{names[i]}"

        print(table)

        ## Dump individual file

        # with open(f"data/{title}.csv", "w") as f:
        #     table.to_csv(f, index=False, header=True)

        # ## Add data to the output files

        # old = pd.read_csv(f'output/{names[i]}.csv')
        # # print(names[i])
        # # print(old.shape)
        # combo = old.append(table)
        # # print(combo.shape)
        # combo = combo.drop_duplicates(keep='last')
        # # print("Dropped", combo.shape)

        # with open(f'output/{names[i]}.csv', 'w') as f:
        #     combo.to_csv(f, index=False, header=True)


        i += 1

# driver.close()