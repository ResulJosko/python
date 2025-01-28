program = {"hello" : "Salam",
            "apple" : "alma",
            "water" : "suw",
            "bread" : "corek"
}

while True:
    k = int(input("Soz salmak: "))
    if k == 1:
        a = input("Enter inlis soz: ")
        b = input("Enter tkm soz: ")
        program [a] = b
    
    if k == 2:
        for i, j in program.items():
            print(f"{i} {j}")
    
    if k == "done":
        break

        
