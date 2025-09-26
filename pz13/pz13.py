
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(len(matrix)): 
    for j in range(len(matrix[i])): 
        if i != j:  
            matrix[i][j] = matrix[i][j] * 2  
print("\nМатрица после преобразования:")
for row in matrix:
    print(row)
