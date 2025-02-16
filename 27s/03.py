import datetime

def birthday_day():
    try:
        birthday = input("Doglan gununizi girizin (YYYY-MM-DD): ")
        birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")
        print(f"Doglan gununiz: {birthday_date.strftime('%A')}")
    except ValueError:
        print("Yalnysh format! YYYY-MM-DD formatynda girizin")
birthday_day()