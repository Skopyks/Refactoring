results = list(operations.values())

print(f"Кількість елементів у списку: {len(results)}")

even_elements = [x for x in results if x % 2 == 0]
print("Парні елементи списку:", even_elements)