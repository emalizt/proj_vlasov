def process_text_file(input_filename, output_filename):
    with open(input_filename, 'r') as f:
        content = f.read()

    # Подсчет букв
    letter_count = sum(c.isalpha() for c in content)

    # Замена верхнего регистра на нижний
    lower_content = content.lower()

    # Запись в новый файл
    with open(output_filename, 'w') as f:
        f.write(lower_content)

    return letter_count

# Пример использования
text_file = 'text18-4.txt'
new_text_file = 'lowercase_text.txt'

# Подсчет букв и создание нового файла
letter_count = process_text_file(text_file, new_text_file)

# Вывод результатов
print(f"Количество букв в файле: {letter_count}")
