
def analyze_text_file():
    with open('text18-4.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    print("Содержимое файла:")
    print("=" * 50)
    print(content)
    print("=" * 50)
    
    letter_count = 0
    for char in content:
        if char.isalpha():  
            letter_count += 1
    
    print(f"Количество букв в тексте: {letter_count}")
    return content

def create_poem_file(original_content):
    lower_content = ""
    for char in original_content:
        if char.isupper():  
            lower_content += char.lower()  
        else:
            lower_content += char 
    
    with open('poem_lowercase.txt', 'w', encoding='utf-8') as file:
        file.write(lower_content)
    
    print("Файл poem_lowercase.txt создан успешно!")
    

    print("\nПреобразованный текст:")
    print("=" * 50)
    print(lower_content)
    print("=" * 50)



create_sample_text_file()
text_content = analyze_text_file()
create_poem_file(text_content)
