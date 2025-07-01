import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix = np.where(np.eye(matrix.shape[0], dtype=bool), matrix, matrix * 2)


has_positive = np.any(matrix > 0)

print(matrix)
print(has_positive)
