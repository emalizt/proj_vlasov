#Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг
#конфет.Вариант 4
def calculate_candy_cost():
    try:
        price_per_kg = float(input("Введите цену 1 кг конфет: "))
        for i in range(1, 11):
            cost = price_per_kg * (i / 10)
            print(f"Стоимость {i / 10} кг конфет: {cost:.2f} руб.")
    except ValueError:
        print("Ошибка: введите корректное вещественное число для цены.")

calculate_candy_cost()