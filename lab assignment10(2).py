import pandas as pd

data = {
    'State': ['State1', 'State2', 'State3', 'State4', 'State5'],
    'Area': [150000, 200000, 180000, 120000, 250000],
    'Population': [5000000, 7000000, 6500000, 4000000, 8000000]
}

df = pd.DataFrame(data)

print(df)

largest_area = df.loc[df['Area'].idxmax()]
print(largest_area['State'])

largest_pop = df.loc[df['Population'].idxmax()]
print(largest_pop['State'])

df['Density'] = df['Population'] / df['Area']
print(df)

highest_density = df.loc[df['Density'].idxmax()]
print(highest_density['State'])
