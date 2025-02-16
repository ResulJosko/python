with open("Sanlar.txt", "r") as fayl:
    A = fayl.read().split()
    B = []
    for i in A:
        B.append(int(i))

with open("Sanlar2.txt", "w") as fayl:
    fayl.write(f"In uly san: {max(B)}\n")
    fayl.write(f"In kici san: {min(B)}\n")
    fayl.write(f"Jemi: {sum(B)}\n")
    fayl.write(f"Ortaca baha: {sum(B)/len(B)}\n")