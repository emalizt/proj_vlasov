#Если в двумерном списке имеются положительные элементы, то вывести TRUE,
#иначе FALSE.
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
    has_positive = False  
    

    for i in range(len(matrix)): 
        for j in range(len(matrix[i])):  
            if matrix[i][j] > 0: 
                has_positive = True  
                break  
        if has_positive:  
            break  
    
    return has_positive


print("Проверка наличия положительных элементов:")
print("Матрица 1:", matrix1, "->", check_positive_elements(matrix1))
print("Матрица 2:", matrix2, "->", check_positive_elements(matrix2))
print("Матрица 3:", matrix3, "->", check_positive_elements(matrix3))
