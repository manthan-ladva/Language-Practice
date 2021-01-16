import pandas as pd

data = pd.read_csv("countries-by-area.txt")
data['Density'] = data['population_2013'] / data['area_sqkm']
data = data.sort_values(by = 'Density', ascending = False)

for index, row in data[:5].iterrows():
    print(row["country"])
