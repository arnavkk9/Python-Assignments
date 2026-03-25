import pandas as pd

data = pd.read_excel("employee.xlsx")

auto = data[data["Department"] == "Automotive"]
print(auto)

emp_id = int(input())
details = data[data["Employee ID"] == emp_id]
print(details)

developers = data[data["Designation"] == "Developer"]
print(developers)
