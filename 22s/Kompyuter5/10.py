import os

def ocurmek():
    time = int(input("Nace minutdan: "))
    os.system(f"shutdown/s/t {time}")
    print(f"Kompyuter {time} minutdan son ocer!")

def restart():
    time = int(input("Nace minutdan: "))
    os.system(f"shutdown/r/t {time}")
    print(f"Kompyuter {time} minutdan son restart bolar!")
    
def buyrugy_yzyna_almak():
    os.system("shutdown/a")
    print("Buyruk yzyna alyndy!")
    

def main():
    while True:
        choice = input("Saylan: ")
        if choice == '1':
            ocurmek()
        elif choice == '2':
            restart()
        elif choice == '3':
            buyrugy_yzyna_almak()
        elif choice == '4':
            print("Programmany ulalanynyz ucin sagbolun!")
            break
        else:
            print("Yalnys buyruk!")

main()