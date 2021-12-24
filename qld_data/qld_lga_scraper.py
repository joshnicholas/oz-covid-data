import requests
import pandas as pd 

import datetime 
import pytz
import time

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
today = utc_now.astimezone(pytz.timezone("Australia/Brisbane"))
today = today.strftime('%Y-%m-%d')

me = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
linko = 'https://www.qld.gov.au/health/conditions/health-alerts/coronavirus-covid-19/current-status/statistics#casebylga'

r = requests.get(linko, headers=me)

page = r.text

table = pd.read_html(page, attrs={'id':'LGA'})[0]
table['Date'] = today

with open(f'qld_data/data/{today}_qld_lga.csv', 'w') as f:
    table.to_csv(f, index=False, header=True)


print(table)
print(table.columns)