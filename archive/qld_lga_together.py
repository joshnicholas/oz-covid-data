import pandas as pd 
import os 
pd.set_option("display.max_rows", 100)

listo = []

for file in os.listdir('qld_lga_data/'):
    # print(file)
    inter = pd.read_csv(f'qld_lga_data/{file}', parse_dates=['Date'])
    inter['Date'] = inter['Date'].dt.strftime("%Y-%m-%d")

    # fin.append(inter)
    listo.append(inter)

final = pd.concat(listo)

final = final.sort_values(by='Date', ascending=True)

final = final.drop_duplicates(subset=['Local Government Area', 'Date'])

p = final

with open('output/qld_lgas.csv', 'w') as f:
    final.to_csv(f, index=False, header=True)

print(p)
print(p.columns)