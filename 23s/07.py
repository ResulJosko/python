import datetime
gun = int(input("Enter the number of days? "))
T = datetime.datetime.today()
D = datetime.timedelta(days = gun)
R = T + D
print("Date after", gun, "days", R.strftime("%d.%m.%Y"))