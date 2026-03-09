name = input("Enter vendor name: ")
year = int(input("Enter year of association: "))
contact = input("Enter contact number: ")
email = input("Enter email ID: ")

total = 0
for i in range(12):
    amt = float(input("Enter purchase amount for month " + str(i+1) + ": "))
    total += amt

print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact:", contact)
print("Email:", email)
print("Annual Purchase:", total)
