hasap = 5
while True:
    print("TMCELL hyzmatlary")
    print("1.Balansyny barlamak")
    print("2.Balansyny doldurmak")
    hyzmat = input('Hyzmat gornusini saylan(1, 2): ')
    if hyzmat == '1':
        tel_belgi = int(input('Tel belginiz '))
        if 60000000 <= tel_belgi <= 65999999 or 71000000 <= tel_belgi <= 71999999:
            print(f"Sizin hasabynyzda {hasap} TMT bar")
        else:
            print("Yalnysh telefon belgi girizdiniz!")
    elif hyzmat == "2":
        tel_belgi = int(input('Tel belginiz: '))
        if 60000000 <= tel_belgi <= 65999999 or 71000000 <= tel_belgi <= 71999999:
            tel_mocberi = int(input("Toleg mocberiniz(TMT): "))
            if 1 <= tel_mocberi <= 50:
                print(f"Sizin hasabynyz {hasap + tel_mocberi} TMT")
            else:
                print("Toleg mukdary 1-50 TMT aralygy bolmaly!")
        else:
            print("Yalnysh telefon belgi girizdiniz!")

    elif hyzmat == "3":
        break

    else:
        print("Yalnysh")