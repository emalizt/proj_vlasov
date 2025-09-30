#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Минимальный элемент:
#Элементы, умноженные на первый максимальный элемент:
def create_initial_file():
     numbers = [15, -3, 8, -12, 25, -7, 10, 4, -18, 6]
    with open('numbers.txt', 'w', encoding='utf-8') as file:
        for number in numbers:
            file.write(str(number) + '\n')
    
    print("Файл numbers.txt создан успешно!")
    return numbers
def process_numbers():
    numbers = []
    with open('numbers.txt', 'r', encoding='utf-8') as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:  
                numbers.append(int(cleaned_line))
    count = len(numbers) 
    min_element = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_element:
            min_element = numbers[i]
    
    max_element = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_element:
            max_element = numbers[i]
    
    multiplied_numbers = []
    for number in numbers:
        multiplied_numbers.append(number * max_element)
    
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write("Исходные данные:\n")
        file.write(" ".join(str(x) for x in numbers) + "\n\n")
        
        file.write("Количество элементов:\n")
        file.write(str(count) + "\n\n")
        
        file.write("Минимальный элемент:\n")
        file.write(str(min_element) + "\n\n")
        
        file.write("Элементы, умноженные на первый максимальный элемент:\n")
        file.write(" ".join(str(x) for x in multiplied_numbers) + "\n")
    
    print("Файл result.txt создан успешно!")
    
    print("\nРезультаты обработки:")
    print("Исходные данные:", numbers)
    print("Количество элементов:", count)
    print("Минимальный элемент:", min_element)
    print("Максимальный элемент:", max_element)
    print("Умноженные элементы:", multiplied_numbers)
numbers_list = create_initial_file()
process_numbers()
