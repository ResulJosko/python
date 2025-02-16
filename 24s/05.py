import datetime
T = datetime.datetime.today()
G = datetime.timedelta(days = 1)

D = (T - G).strftime("%d.%m.%Y %A")
S = T.strftime("%d.%m.%Y %A")
E = (T + G).strftime("%d.%m.%Y %A")

with open("Sene.txt", "w") as fayl:
    fayl.write(f"{D}\n{S}\n{E}")