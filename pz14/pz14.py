def process_hotline_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    additions_count = 0
    updated_lines = []

    for line in lines:
        if "Горячая линия" in line:
            line = line.replace("Горячая линия", "Горячая линия Министерства образования Ростовской области")
            additions_count += 1
        updated_lines.append(line)
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)
    return additions_count
def count_phone_numbers(input_filename):
    with open(input_filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    count_ends_03 = 0
    count_ends_50 = 0
    ege_gia_numbers = []

    for line in lines:

        if "ЕГЭ" in line or "ГИА" in line:

            words = line.split()
            for word in words:
                if word.startswith('+7') or word.startswith('8'):
                    if word.endswith('03'):
                        count_ends_03 += 1
                    elif word.endswith('50'):
                        count_ends_50 += 1
                    ege_gia_numbers.append(word)

    return count_ends_03, count_ends_50, ege_gia_numbers


input_file = 'hotline.txt'
output_file = 'updated_hotline.txt'


additions = process_hotline_file(input_file, output_file)
print(f"Количество добавлений: {additions}")


count_03, count_50, ege_gia_numbers = count_phone_numbers(input_file)
print(f"Количество номеров, заканчивающихся на '03': {count_03}")
print(f"Количество номеров, заканчивающихся на '50': {count_50}")
print("Номера телефонов горячих линий, связанных с ЕГЭ/ГИА:")
for number in ege_gia_numbers:
    print(number)
