def geometric(A, D):
    return [A * (D ** n) for n in range(10)]
A = 2  # Первый член
D = 3  # Знаменатель
progression = geometric(A, D)
print(progression)