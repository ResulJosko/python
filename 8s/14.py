num1 = 0
num2 = 0
for i in range(1, 6):
    number = int(input(f"{i} number : "))
    if number > 0:
        num1 += number
    else:
        num2 += number

print(f"Sum of positive numbers: {num1}")
print(f"Sum of netative numbers: {num2}")