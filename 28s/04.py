class Sirket:
    self.ad = ad
    self.calisma = True

def program(self):
    saylaw = self.menuSecim()

    if saylaw == 1:
        self.calianEkle()
    elif saylaw == 2:
        self.isgarCykar()
    elif saylaw == 3:
        yylyk_gormek = input("Yylyk yagdayda gormek isleyarsinizmi? (hawa/yok): ")
        if yylyk_gormek == "hawa":
            self.berikmeliAylykGor(hasap = "yylyk")
        else:
            self.berikmeliAylykGor()
    elif saylaw == 4:
        self.maaslariVer()
    elif saylaw == 5:
        self.masrafGir()

def nemuSecim(self):
    try:
        saylaw = int(input(f"****{self.ad} Ulgamyna hosh geldiniz ****\n\n1-Calisan Ekle\n2-Calisan Cikar\n3-Verilik Maas Goster\n4-Maaslari ver\n5-Masraf gir\n\nSaylawynyzy girizin: "))
        while saylaw < 1 or saylaw > 6:
            saylaw = int(input("1-6 aralygynda saylaw girizin: "))
        return saylaw
    except ValueError:
        print("Nadogry girish. San girizin!")
        return self.menuSecim()

def calianEkle(self):
    ad = input("Ishgarin adyny girizin: ")
    soyad = input("Ishgarin soyadyny girizin: ")
    yas = input("Ishgarin yashyny girizin: ")
    cinsiyet = input("Ishgarin cinsiyetini girizin: ")
    maas = input("Ishgarin maasy girizin: ")

    with open("calisanlar.txt", "r") as dosya:
        calislanListesi = dosya.readlines()

    if len(calislanListesi) == 0:
        id = 1
    else:
        with open("calisanlar.txt", "a+") as dosya:
            id = int(dosya.readlines()[-1].split(")")[0]) + 1

    with open("calisanlar.txt", "r") as dosya:
        calisanlar = dosya.readlines()

        gorunerIsgarler = []
        for calisan in calisanlar:
            gorunerIsgarler.append(" ".join(calisan[:-1].split(" - ")))

        for idx, calisan in enumerate(gorunerIsgarler, start - 1)
            print(f"{idx}) {calisan}")

        saylaw = int(input(f"Cykarmak ishleyan ishgarin nomerini girizin (1-{len(gorunerIsgarler)}): "))
        while saylaw < 1 or saylaw > len(gorunerIsgarler):
            saylaw = int(input(f"(1-{len(gorunerIsgarler)}) aralygynda nomer girizin: "))

        calisanlar.pop(saylaw - 1)

        tazeIsgarler = []
        for sanaw, calisan in enumerate(calisanlar, start = 1):
            tazeIsgarler.append(f"{sanaw}) {calisan.split(') ')[1]}")

        with open("calisanlar.txt", "w") as dosya:
            dosya.writelines(tazeIsgarler)
        print("Ishgarler ustunikli cykaryldy.")
    except Exception as e:
        print(f"Yalnyshlyk yuze cykdy: {e}")

def berilmeliAylykGor(self, hasap = "aylyk"):
    try:
        with open("calisanlar.txt", "r") as dosya:
            calisanlar = dosya.readlines()

        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))

        if hasap == "aylyk":
            print(f"Bu ayda berilmeli umumy aylyk: {sum(maaslar)} TMT")
        elif hasap == "yylyk":
            print(f"Bu yylda berilmeli umumy aylyk: {sum(maaslar) * 12} TMT")
    except Exception as e:
        print(f"Yalnyshlyk yuze cykdy: {e}")

def maaslariVer(self):
    try:
        with open("calisanlar.txt", "r") as dosya:
            calisanlar = dosya.readlines()

        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        toplamMaas - sum(maaslar)

        try:
            with open("butce.txt", "r") as dosya:
                butce = int(dosya.read().strip())
        except FileNotFoundError:
            butce = 0

        butce -= toplamMaas

        with open("butce.txt, ")