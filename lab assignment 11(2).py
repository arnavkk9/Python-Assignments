import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("recruitment.csv")

companies = data["Company"]
hires = data["Hires"]

plt.bar(companies, hires)
plt.title("Recruitment Bar Chart")
plt.show()

plt.pie(hires, labels=companies, autopct="%1.1f%%")
plt.title("Recruitment Pie Chart")
plt.show()

colors = ["red", "blue", "green", "orange", "purple", "cyan"]

plt.pie(hires, labels=companies, colors=colors, autopct="%1.1f%%")
plt.title("Customized Pie Chart")
plt.show()

plt.pie(hires, labels=companies, autopct="%1.1f%%", wedgeprops={"width":0.4})
plt.title("Doughnut Chart")
plt.show()

ibm = data[data["Company"] == "IBM"]["Hires"].sum()
amdocs = data[data["Company"] == "Amdocs"]["Hires"].sum()

plt.bar(["IBM", "Amdocs"], [ibm, amdocs])
plt.title("IBM vs Amdocs Hiring")
plt.show()
