
magazines = {
    "Магистр": {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"},
    "ДомКниги": {"Толстой", "Грибоедов", "Чехов", "Пушкин"},
    "БукМаркет": {"Пушкин", "Достоевский", "Маяковский"},
    "Галерея": {"Чехов", "Тютчев", "Пушкин"}
}
magazines_with_mayakovsky = []
for magazine_name, books in magazines.items():
    if "Маяковский" in books:
        magazines_with_mayakovsky.append(magazine_name)
print("Книги Маяковского можно приобрести в следующих магазинах:")
for magazine in magazines_with_mayakovsky:
    print(f"- {magazine}")
