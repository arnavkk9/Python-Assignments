import pandas as pd

df = pd.read_csv("books.csv")

print(df)

author_name = input()
print(df[df['author'] == author_name])

publisher_name = input()
print(df[df['publisher'] == publisher_name])

cheapest = df.loc[df['price'].idxmin()]
costliest = df.loc[df['price'].idxmax()]

print(cheapest['title'])
print(costliest['title'])

sorted_df = df.sort_values(by='year')
print(sorted_df)
