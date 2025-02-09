def get_number(prompt, number_type):
    return number_type(input(prompt))

int_number1 = get_number("Введіть перше ціле число: ", int)
int_number2 = get_number("Введіть друге ціле число: ", int)
float_number1 = get_number("Введіть перше дробове число: ", float)
float_number2 = get_number("Введіть друге дробове число: ", float)

print(f"Цілі числа: {int_number1} та {int_number2}")
print(f"Дробові числа: {float_number1} та {float_number2}")