v = float(input("Enter voltage: "))
r = float(input("Enter resistance: "))

i = v / r
print("Current:", i)

if i < 0.5:
    print("Low current")
elif i <= 2:
    print("Normal current")
else:
    print("High current")
