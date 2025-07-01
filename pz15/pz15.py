import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Catalog (
    book_id INTEGER PRIMARY KEY,
    genre TEXT,
    country TEXT,
    series TEXT,
    author TEXT,
    title TEXT,
    year INTEGER,
    annotation TEXT
)
''')

def add_book(book_id, genre, country, series, author, title, year, annotation):
    cursor.execute('INSERT INTO Catalog VALUES (?, ?, ?, ?, ?, ?, ?, ?)', 
                   (book_id, genre, country, series, author, title, year, annotation))
    conn.commit()

def search_book(search_term):
    cursor.execute('SELECT * FROM Catalog WHERE title LIKE ? OR author LIKE ? OR genre LIKE ?', 
                   (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
    return cursor.fetchall()

def delete_book(book_id):
    cursor.execute('DELETE FROM Catalog WHERE book_id = ?', (book_id,))
    conn.commit()

def edit_book(book_id, genre, country, series, author, title, year, annotation):
    cursor.execute('UPDATE Catalog SET genre = ?, country = ?, series = ?, author = ?, title = ?, year = ?, annotation = ? WHERE book_id = ?', 
                   (genre, country, series, author, title, year, annotation, book_id))
    conn.commit()

add_book(1, 'Фантастика', 'США', 'Звёздные войны', 'Джордж Лукас', 'Новая надежда', 1977, 'Описание 1')
add_book(2, 'Фантастика', 'США', 'Звёздные войны', 'Джордж Лукас', 'Империя наносит ответный удар', 1980, 'Описание 2')
add_book(3, 'Фэнтези', 'Великобритания', 'Властелин колец', 'Дж. Р. Р. Толкин', 'Братство кольца', 1954, 'Описание 3')
add_book(4, 'Детектив', 'США', 'Шерлок Холмс', 'Артур Конан Дойл', 'Этюд в багровых тонах', 1887, 'Описание 4')
add_book(5, 'Приключения', 'Франция', 'Том Сойер', 'Марк Твен', 'Приключения Тома Сойера', 1876, 'Описание 5')
add_book(6, 'Научная фантастика', 'США', 'Дюна', 'Фрэнк Герберт', 'Дюна', 1965, 'Описание 6')
add_book(7, 'Ужасы', 'США', 'Сияние', 'Стивен Кинг', 'Сияние', 1977, 'Описание 7')
add_book(8, 'Роман', 'Россия', 'Война и мир', 'Лев Толстой', 'Война и мир', 1869, 'Описание 8')
add_book(9, 'Фантастика', 'США', '451 градус по Фаренгейту', 'Рэй Брэдбери', '451 градус по Фаренгейту', 1953, 'Описание 9')
add_book(10, 'Фэнтези', 'США', 'Гарри Поттер', 'Дж. К. Роулинг', 'Гарри Поттер и философский камень', 1997, 'Описание 10')

print(search_book('Гарри Поттер'))

delete_book(10)

edit_book(1, 'Фантастика', 'США', 'Звёздные войны', 'Джордж Лукас', 'Новая надежда', 1977, 'Обновлённое описание')

conn.close()
