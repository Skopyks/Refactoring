
results = [15, 5, 50, 2.0, 100000, 2, 0]

count = len(results)

print(f"Кількість елементів у списку: {count}")

even_elements = [x for x in results if x % 2 == 0]
print("Парні елементи списку:", even_elements)
