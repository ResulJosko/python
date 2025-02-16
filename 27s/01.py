import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Bir san chakla (1-100 aralygynda) "))
            attempts += 1
            if guess < secret_number:
                print("Kabir uly san chakla!")
            elif guess > secret_number:
                print("Kabir kichi san chakla!")
            else:
                print(f"Dogry! {attempts} synanyshykda chakladynyz")
                break
        except ValueError:
            print("Yalnysh san girizdiniz!")
guess_the_number()