import datetime
sagat = int(input("Enter the number of hours? "))
T = datetime.datetime.today()
H = datetime.timedelta(hours = sagat)
R = T + H
print("Date after", sagat, "hours", R.strftime("%d.%m.%Y %X"))