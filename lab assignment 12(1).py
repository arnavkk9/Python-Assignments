import pandas as pd

data = pd.read_csv("diamonds.csv")

mean_price = data.groupby("cut")["price"].mean()
print(mean_price)

stats = data.groupby("cut")["price"].agg(["count", "min", "max"])
print(stats)

print(data["x"].mean())
print(data["y"].mean())
print(data["z"].mean())
