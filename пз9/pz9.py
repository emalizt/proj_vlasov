def sum_half_dict(input_dict):
    values = list(input_dict.values())
    if len(values) % 2 != 0:
        raise ValueError("Количество элементов в словаре должно быть четным.")
    mid_index = len(values) // 2
    first_half = values[:mid_index]
    second_half = values[mid_index:]
    sum_first_half = sum(first_half)
    sum_second_half = sum(second_half)
    print(f"Сумма первой половины: {sum_first_half}")
    print(f"Сумма второй половины: {sum_second_half}")
example_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6
}
sum_half_dict(example_dict)
