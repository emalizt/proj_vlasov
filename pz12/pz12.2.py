def letter_generator(input_string):
    for char in input_string:
        if char.isalpha():  # Проверяем, является ли символ буквой
            yield char

# Пример использования
input_str = "Hello, World! 123"
letters = ''.join(letter_generator(input_str))
print("Буквы из строки:", letters)
