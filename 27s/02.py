import calendar

def display_calendar():
    try:
        year = int(input("Yyly girizin: "))
        month = int(input("Ayy girizin: "))
        if 1 <= month <= 12:
            print(calendar.month(year, month))
        else:
            print("Yalnysh ay giriziniz!")
    except ValueError:
        print("Yalnysh san girizdiniz")
display_calendar()