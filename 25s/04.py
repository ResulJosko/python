with open("Numbers.txt", "w") as fayl:
    i = 1
    while i <= 7:
        number = int(input(f"{i}-san: "))
        i += 1
        fayl.write(f"{number}   ")