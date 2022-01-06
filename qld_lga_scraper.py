import requests
import pandas as pd 
import os
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

with open(f'qld_lga_data/{today}_qld_lga.csv', 'w') as f:
    table.to_csv(f, index=False, header=True)


# old = pd.read_csv('output/qld_lgas.csv')

# final = old.append(table)

# final = final.drop_duplicates(subset=['Local Government Area', 'Date'], keep='last')
# final = final[['Local Government Area', 'Total', 'Date']]
# final.columns = ["LGA", 'Total cases', 'Date']
# with open('output/qld_lgas.csv', 'w') as f:
#     final.to_csv(f, index=False, header=True)

# p = final

# print(p)
# print(p.columns)

# # Process into one file

listo = []

for file in os.listdir('qld_lga_data'):

    inter = pd.read_csv(f'qld_lga_data/{file}', parse_dates=['Date'])
    inter = inter[['Local Government Area', 'Total', 'Date']]
    inter.columns = ["LGA", 'Total cases', 'Date']
    # print(inter)
    # # print(file)
    inter = inter.loc[inter['LGA'] !="Total"]


    listo.append(inter)
    # print(inter.columns.tolist())

qld = pd.concat(listo)
qld = qld.sort_values(by='Date', ascending=True)

qld['Date'] = pd.to_datetime(qld['Date'])

print(qld)

with open('output/qld_lgas.csv', 'w') as f:
    qld.to_csv(f, index=False, header=True)