import pandas as pd

# Load CSV file
df = pd.read_csv("books.csv")

# a) Print complete report
print("\n--- Complete Book Report ---")
print(df)

# b) Books of a given author
author_name = input("\nEnter author name: ")
print(df[df['author'] == author_name])

# c) Books of a given publisher
publisher_name = input("\nEnter publisher name: ")
print(df[df['publisher'] == publisher_name])

# d) Cheapest and costliest book
cheapest = df.loc[df['price'].idxmin()]
costliest = df.loc[df['price'].idxmax()]

print("\nCheapest Book:")
print(cheapest['title'])

print("\nCostliest Book:")
print(costliest['title'])

# e) Sort by year of publication
sorted_df = df.sort_values(by='year')
print("\n--- Books Sorted by Year ---")
print(sorted_df)
