#В последовательности на n целых чисел умножить элементы до n-1 на элемент
#n.

def multiply_elements(sequence):
    if len(sequence) < 2:
        raise ValueError("Последовательность должна содержать как минимум два элемента.")
    
    n = sequence[-1]
    result = [x * n for x in sequence[:-1]]
    return result


numbers = [1, 2, 3, 4, 5] 
result = multiply_elements(numbers)
print("Результат умножения:", result)
