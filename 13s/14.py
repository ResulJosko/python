numbers = [1, 2, 3, 4, 5, 6]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Jübüt sanlar:", even_numbers)
print("Täk sanlar:", odd_numbers)