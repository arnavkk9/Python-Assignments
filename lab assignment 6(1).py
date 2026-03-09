text = input("Enter a string: ")

v = 0
c = 0
s = 0
l = 0

for ch in text:
    if ch in "aeiouAEIOU":
        v += 1
    elif ch.isalpha():
        c += 1

    if ch == " ":
        s += 1

    if ch.islower():
        l += 1

print("Number of Vowels:", v)
print("Number of Consonants:", c)
print("Number of Spaces:", s)
print("Number of Lowercase Letters:", l)
