with open("Sanlar.txt", "w") as fayl:
    i = 1
    while i <= 5:
        num = int(input(f"{i}-san: "))
        i += 1
        fayl.write(f"{num}   ")