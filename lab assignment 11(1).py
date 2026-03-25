import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales.csv")

months = data["Month"]
total_profit = data["Total_Profit"]

plt.plot(months, total_profit)
plt.title("Total Profit by Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

products = data.drop(columns=["Month", "Total_Profit"])

plt.plot(months, products)
plt.legend(products.columns)
plt.title("Product Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

facecream = data["FaceCream"]
facewash = data["FaceWash"]

plt.bar(months, facecream)
plt.bar(months, facewash)
plt.title("Face Cream vs Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

yearly_sales = products.sum()

plt.pie(yearly_sales, labels=yearly_sales.index, autopct="%1.1f%%")
plt.title("Yearly Sales Distribution")
plt.show()
