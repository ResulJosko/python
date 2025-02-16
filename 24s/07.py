import random

with open("Random.txt", "w") as file:
    for i in range(5):
        file.write(f"{random.randint(1000, 9999)}\n")