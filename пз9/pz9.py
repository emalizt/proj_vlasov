dict = {
        "a" : 12,
        "b" : 14,
        "c" : 5,
        "d" : 2,
        "e" : 11,
        "f" : 17,
        "g" : 8,
        "h" : 1
}

list = list(dict.values())

first_half = list[:len(list) // 2]
second_half = list[len(list) // 2 :]
print("Исходный словарь: ", dict)

print("Сумма значений первой половины: ", sum(first_half))
print("Сумма значений второй половины: ", sum(second_half))
