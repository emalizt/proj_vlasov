# 1. Дано целое число N (1 < N < 26). Вывести N первых прописных (то есть заглавных) букв латинского алфавита.

N = int(input("Введите N (1 < N < 26): "))
result = ""
for i in range(N):
    result += chr(ord('A') + i)
print(result)