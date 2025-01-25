def gosmak():
    print(f"Netije: {san1 + san2}")


def ayyrmak():
    print(f"Netije: {san1 - san2}")

def kopeltmek():
    print(f"Netije: {san1 * san2}")

def bolmek():
    if san2 == 0:
        print("0-la bolip bilsen bolda")
    
    else:
        print(f"Netije: {san1 / san2}")

def cykys():
        print("Cykdynyz!")



while True:
    san1 = int(input("Birinji sany girizin: "))
    san2 = int(input("Ikinji sany girizin: "))
    funksiya = input("Funksiya saylan: +, -, *, /\nFunksiya: ")
    if funksiya == "+":
        gosmak()

    elif funksiya == "-":
        ayyrmak()

    elif funksiya == "*":
        kopeltmek()

    elif funksiya == "/":
        bolmek()

    elif funksiya == "quit":
        cykys()
        break