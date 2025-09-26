import re

def create_sample_file():
    sample_text = """Горячая линия поддержки:
Тел: +7(863)123-45-67
Тел: 8-800-555-35-35
Моб: +7918-555-44-33
Факс: (863)234-56-78
Экстренная связь: 112
Резервный: 8-900-123-45-50"""

    with open('hotline.txt', 'w', encoding='utf-8') as file:
        file.write(sample_text)
    print("Файл hotline.txt создан успешно!\n")

def process_hotline_file():
    with open('hotline.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    
    print("Исходное содержимое файла:")
    print("=" * 40)
    print(content)
    print("=" * 40)
    print()
    
    pattern_hotline = r'Горячая линия'
    new_content = re.sub(
        pattern_hotline, 
        r'Горячая линия\nМинистерства образования Ростовской области', 
        content, 
        count=1
    )
    
    print("Содержимое после добавления фразы:")
    print("=" * 40)
    print(new_content)
    print("=" * 40)
    print()
    
    pattern_ministry = r'Министерства образования Ростовской области'
    ministry_count = len(re.findall(pattern_ministry, new_content))
    print(f"Количество добавленных фраз: {ministry_count}")
    print()
    
    phone_pattern = r'\b[\d\-+()]{7,15}\b'
    all_phones = re.findall(phone_pattern, content)
    
    print("Все найденные номера телефонов:")
    for i, phone in enumerate(all_phones, 1):
        print(f"{i}. {phone}")
    print()
    
    phones_ending_3_or_50 = []
    for phone in all_phones:
        clean_phone = re.sub(r'\D', '', phone)
        if clean_phone:
            if clean_phone.endswith('3') or clean_phone.endswith('50'):
                phones_ending_3_or_50.append(phone)
    
    print("Номера телефонов, заканчивающиеся на '3' или '50':")
    for i, phone in enumerate(phones_ending_3_or_50, 1):
        print(f"{i}. {phone}")
    
    print(f"\nКоличество номеров, заканчивающихся на '3' или '50': {len(phones_ending_3_or_50)}")
    print()
    
    precise_phone_pattern = r'(\+?7?[-\s]?\(?\d{3}\)?[-\s]?\d{2,3}[-\s]?\d{2}[-\s]?\d{2})'
    hotline_phones = re.findall(precise_phone_pattern, content)
    
    print("Номера телефонов горячих линий:")
    for i, phone in enumerate(hotline_phones, 1):
        print(f"{i}. {phone}")
    
    with open('hotline_processed.txt', 'w', encoding='utf-8') as file:
        file.write("ОБРАБОТАННЫЕ ДАННЫЕ ГОРЯЧЕЙ ЛИНИИ\n")
        file.write("=" * 50 + "\n\n")
        file.write("Исходный текст с добавленной фразой:\n")
        file.write(new_content + "\n\n")
        file.write(f"Количество добавленных фраз: {ministry_count}\n\n")
        file.write("Все номера телефонов:\n")
        for i, phone in enumerate(all_phones, 1):
            file.write(f"{i}. {phone}\n")
        file.write("\n")
        file.write("Номера, заканчивающиеся на '3' или '50':\n")
        for i, phone in enumerate(phones_ending_3_or_50, 1):
            file.write(f"{i}. {phone}\n")
        file.write(f"Всего: {len(phones_ending_3_or_50)}\n\n")
        file.write("Номера горячих линий:\n")
        for i, phone in enumerate(hotline_phones, 1):
            file.write(f"{i}. {phone}\n")
    
    print(f"\nРезультаты сохранены в файл: hotline_processed.txt")

if __name__ == "__main__":
    print("=== ОБРАБОТКА ФАЙЛА ГОРЯЧЕЙ ЛИНИИ ===\n")
    create_sample_file()
    process_hotline_file()
