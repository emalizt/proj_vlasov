def has_positive_elements(matrix):
    for row in matrix:
        for element in row:
            if element > 0:  # Проверяем, является ли элемент положительным
                return True
    return False

# Пример использования
matrix = [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9]
]

result = has_positive_elements(matrix)
print("Содержит ли матрица положительные элементы:", result)
