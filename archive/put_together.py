import pandas as pd 
import os 


names = ["recent_cases", "total_cases", "cases_age_sex",
 "deaths_age_sex", "tests", "hospitalisations", "ndis",
  "aged_care_resi", "aged_care_home", "oecd_mortality"]

for name in names:

    listo = []


    for file in os.listdir('data'):
        if name in file:
            inter = pd.read_csv(f'data/{file}', parse_dates=['Date'])
            # print(inter)
            # print(file)
            listo.append(inter)
            # print(inter.columns)


    final = pd.concat(listo)
    final = final.sort_values(by='Date', ascending=True)

    with open(f"output/{name}.csv", "w") as f:
        final.to_csv(f, index=False, header=True)

    # print(final.shape)
    # final.drop_duplicates(keep='last')
    # print(final.shape)


# print(final[['Jurisdiction',
#        'Total cases', 'Total deaths', 'Date']])