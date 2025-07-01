import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Обработка данных формы (можно добавить обработку)
    messagebox.showinfo("Информация", "Данные подтверждены")

# Создание основного окна
root = tk.Tk()
root.title("Форма регистрации пользователя")

# Создание виджетов
tk.Label(root, text="Ваше имя:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Пароль:").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Возраст:").grid(row=2, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Пол:").grid(row=3, column=0, padx=10, pady=5)
gender_var = tk.StringVar(value="Мужской")
tk.Radiobutton(root, text="Мужской", variable=gender_var, value="Мужской").grid(row=3, column=1, sticky=tk.W)
tk.Radiobutton(root, text="Женский", variable=gender_var, value="Женский").grid(row=3, column=1, sticky=tk.E)

tk.Label(root, text="Ваши увлечения:").grid(row=4, column=0, padx=10, pady=5)
music_var = tk.BooleanVar()
video_var = tk.BooleanVar()
drawing_var = tk.BooleanVar()
tk.Checkbutton(root, text="Музыка", variable=music_var).grid(row=4, column=1, sticky=tk.W)
tk.Checkbutton(root, text="Видео", variable=video_var).grid(row=4, column=1, sticky=tk.E)
tk.Checkbutton(root, text="Рисование", variable=drawing_var).grid(row=4, column=1)

tk.Label(root, text="Ваша страна:").grid(row=5, column=0, padx=10, pady=5)
country_entry = tk.Entry(root)
country_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Ваш город:").grid(row=6, column=0, padx=10, pady=5)
city_entry = tk.Entry(root)
city_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Кратко о себе:").grid(row=7, column=0, padx=10, pady=5)
about_entry = tk.Text(root, height=5, width=30)
about_entry.insert(tk.END, "Краткая информация о ваших увлечениях")
about_entry.grid(row=7, column=1, padx=10, pady=5)

tk.Label(root, text="Решите пример, запишите результат в поле ниже:").grid(row=8, column=0, padx=10, pady=5)
result_entry = tk.Entry(root)
result_entry.grid(row=8, column=1, padx=10, pady=5)

# Кнопки
tk.Button(root, text="Отменить ввод", command=root.quit).grid(row=9, column=0, padx=10, pady=10)
tk.Button(root, text="Данные подтверждаю", command=submit_form).grid(row=9, column=1, padx=10, pady=10)

# Запуск приложения
root.mainloop()
