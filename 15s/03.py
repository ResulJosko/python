isgarler = { "Mekan" : {"hunari" : "programmist",
                        "bilimi" : "orta",
                        "yashy" : 22},

            "Oraz" : {"hunari" : "hasapchy",
                    "bilimi" : "yokary",
                    "yashy" : 30}
}

ady = input('Ady: ')
if ady in isgarler:
    isleg = input('Doly maglumat:(howa/yok) ')
    if isleg == "howa":
        print(isgarler[ady])
    else:
        mag = input('hunari/bilimi/yashy ')
        print(isgarler[ady][mag])
else:
    print(f"{ady} atly isgar yok")