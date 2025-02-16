A = ["Inlis dili", "Kompyuter", "Matematika"]
with open("Kurslar.txt", "w") as fayl:
    for i in A:
        fayl.write(f"{i}\n")