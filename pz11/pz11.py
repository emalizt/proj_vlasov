def process_text_file(input_filename, output_filename):
    with open(input_filename, 'r') as f:
        content = f.read()


    letter_count = sum(c.isalpha() for c in content)


    lower_content = content.lower()


    with open(output_filename, 'w') as f:
        f.write(lower_content)

    return letter_count


text_file = 'text18-4.txt'
new_text_file = 'lowercase_text.txt'


letter_count = process_text_file(text_file, new_text_file)


print(f"Количество букв в файле: {letter_count}")
