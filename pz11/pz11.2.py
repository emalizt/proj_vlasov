# Часть 1: Анализ текстового файла
def analyze_text_file():
    # Читаем содержимое файла
    with open('text18-4.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Выводим содержимое файла
    print("Содержимое файла:")
    print("=" * 50)
    print(content)
    print("=" * 50)
    
    # Подсчитываем количество букв
    letter_count = 0
    for char in content:
        if char.isalpha():  # Проверяем, является ли символ буквой
            letter_count += 1
    
    print(f"Количество букв в тексте: {letter_count}")
    return content

# Часть 2: Создание нового файла с преобразованным текстом
def create_poem_file(original_content):
    # Преобразуем верхний регистр в нижний
    lower_content = ""
    for char in original_content:
        if char.isupper():  # Если символ в верхнем регистре
            lower_content += char.lower()  # Преобразуем в нижний
        else:
            lower_content += char  # Оставляем как есть
    
    # Создаем новый файл
    with open('poem_lowercase.txt', 'w', encoding='utf-8') as file:
        file.write(lower_content)
    
    print("Файл poem_lowercase.txt создан успешно!")
    
    # Выводим преобразованный текст
    print("\nПреобразованный текст:")
    print("=" * 50)
    print(lower_content)
    print("=" * 50)

# Создаем пример текстового файла для задачи 2
def create_sample_text_file():
    poem = """У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;

Идёт направо - песнь заводит,
Налево - сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;"""
    
    with open('text18-4.txt', 'w', encoding='utf-8') as file:
        file.write(poem)
    
    print("Пример файла text18-4.txt создан!")

# Запуск второй задачи
print("\n=== ЗАДАЧА 2 ===")
create_sample_text_file()
text_content = analyze_text_file()
create_poem_file(text_content)