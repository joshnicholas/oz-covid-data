#%%
import requests
import pandas as pd
import numpy as np
import datetime
pd.set_option("display.max_rows", 100)


# %%
# Read in Anthony's data
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get('https://covidlive.com.au/covid-live.json', headers=headers)

data = r.json()
df = pd.read_json(r.text)
df = df.sort_values(by='REPORT_DATE', ascending=True)

with open("Anthony_feed.csv", "w") as f:
    df.to_csv(f, index=False, header=True)
