# вариант 4 Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
#Использовать локальные переменные
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

try:
    n = 60  # Можно изменить на любое другое число, если нужно
    result = sum_of_numbers(n)
    print("Сумма чисел от 1 до", n, "равна:", result)
except Exception as e:
    print("Произошла ошибка:", e)
