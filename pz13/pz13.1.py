def increase_non_diagonal_elements(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j: 
                matrix[i][j] *= 2
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

increase_non_diagonal_elements(matrix)
print("Матрица после увеличения элементов, не лежащих на главной диагонали:")
for row in matrix:
    print(row)
