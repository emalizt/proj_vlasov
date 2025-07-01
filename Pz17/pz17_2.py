import tkinter as tk
from tkinter import messagebox

def display_letters():
    try:
        N = int(entry.get())  # Получаем ввод от пользователя
        if 1 < N < 26:
            letters = ''.join(chr(i) for i in range(65, 65 + N))  # Генерируем буквы
            messagebox.showinfo("Результат", f"Первые {N} заглавных букв латинского алфавита: {letters}")
        else:
            messagebox.showwarning("Ошибка", "Введите число от 2 до 25.")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное целое число.")

# Создаем основное окно
root = tk.Tk()
root.title("Генерация заглавных букв")

# Создаем виджеты
label = tk.Label(root, text="Введите целое число N (1 < N < 26):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Показать буквы", command=display_letters)
button.pack(pady=20)

# Запускаем основной цикл приложения
root.mainloop()
