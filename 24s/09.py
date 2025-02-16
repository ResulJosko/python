with open("Talyplar.txt", "w") as file:
    for i in range(5):
        ady = input(f"{i + 1}-ady: ")
        file.write(f"{i + 1}-{ady}\n")