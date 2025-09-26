# Создаем несколько примеров матриц для проверки
matrix1 = [
    [1, -2, -3],
    [-4, 5, -6],
    [-7, -8, -9]
]

matrix2 = [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9]
]

matrix3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def check_positive_elements(matrix):
    """
    Проверяет, есть ли в матрице хотя бы один положительный элемент
    Возвращает TRUE если есть, FALSE если нет
    """
    has_positive = False  # Изначально предполагаем, что положительных нет
    
    # Проходим по всем элементам матрицы
    for i in range(len(matrix)):  # По строкам
        for j in range(len(matrix[i])):  # По столбцам
            if matrix[i][j] > 0:  # Если элемент положительный
                has_positive = True  # Нашли положительный элемент
                break  # Выходим из внутреннего цикла
        if has_positive:  # Если уже нашли положительный элемент
            break  # Выходим из внешнего цикла
    
    return has_positive

# Тестируем на разных матрицах
print("Проверка наличия положительных элементов:")
print("Матрица 1:", matrix1, "->", check_positive_elements(matrix1))
print("Матрица 2:", matrix2, "->", check_positive_elements(matrix2))
print("Матрица 3:", matrix3, "->", check_positive_elements(matrix3))