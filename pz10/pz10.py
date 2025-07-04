# Создаем словарь с магазинами и их коллекциями книг
book_stores = {
    'Магистр': ['Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'],
    'ДомКниги': ['Толстой', 'Грибоедов', 'Чехов', 'Пушкин'],
    'БукМаркет': ['Пушкин', 'Достоевский', 'Маяковский'],
    'Галерея': ['Чехов', 'Тютчев', 'Пушкин']
}


stores_with_mayakovsky = [store for store, books in book_stores.items() 
                         if 'Маяковский' in books]

print("Книги Маяковского можно приобрести в следующих магазинах:")
for store in stores_with_mayakovsky:
    print(f"- {store}")
