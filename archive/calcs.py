import pandas as pd 
import os 


listo = []

for file in os.listdir('data'):
    # print(file)
    # if "aged_care_home" in file:
    if "total_cases" in file:
        inter = pd.read_csv(f'data/{file}', parse_dates=['Date'])
        print(inter)
        # print(file)
        listo.append(inter)


final = pd.concat(listo)
final = final.sort_values(by='Date', ascending=True)

# final.drop_duplicates()

print(final[['Jurisdiction',
       'Total cases', 'Total deaths', 'Date']])
# print(final.columns)
# print(final['Date'].max())