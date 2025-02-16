def calculate_sum_and_average(start, end):
    total = sum(range(start, end + 1))
    count = end - start + 1
    average = total / count
    return total, average

try:
    start = int(input("Bashlangych sany girizin: "))
    end = int(input("Sonky sany girizin: "))
    total, average = calculate_sum_and_average(start, end)
    print(f"Jemi: {total}, Ortacha: {average}")
except ValueError:
    print("Yalnysh san girizdiniz!")