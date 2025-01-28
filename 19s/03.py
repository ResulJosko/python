soz = "Gujurly Bilim okuw merkezi"
l = 0
cap = 0
small = 0

for i in soz:
    if i.isalpha():
        l += 1
        if i.isupper():
            cap += 1
        elif i.islower():
            small += 1
print(soz)
print(l)
print(cap)
print(small)
    