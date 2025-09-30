#Составить генератор (yield), который выводит из строки только буквы.
def letter_generator(input_string):
    for char in input_string:
        if char.isalpha():
            yield char

input_str = "Hello, World! 123"
letters = ''.join(letter_generator(input_str))
print("Буквы из строки:", letters)
