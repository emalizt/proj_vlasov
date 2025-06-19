def multiply_elements(sequence):
    if len(sequence) < 2:
        raise ValueError("Последовательность должна содержать как минимум два элемента.")
    
    n = sequence[-1]  # Последний элемент
    result = [x * n for x in sequence[:-1]]  # Умножаем все элементы до n-1 на n
    return result

# Пример использования
numbers = [1, 2, 3, 4, 5]  # Пример последовательности
result = multiply_elements(numbers)
print("Результат умножения:", result)
