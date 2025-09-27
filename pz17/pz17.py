from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        password = request.form.get('password')
        age = request.form.get('age')
        gender = request.form.get('gender')
        hobbies = request.form.getlist('hobbies')
        country = request.form.get('country')
        city = request.form.get('city')
        about = request.form.get('about')
        hobbies_info = request.form.get('hobbies_info')
        math_result = request.form.get('math_result')
        
        # Проверка примера (пример: 5 + 3 = 8)
        if math_result != "8":
            flash('Неправильный ответ на математический пример!', 'error')
            return redirect(url_for('index'))
        
        # Проверка обязательных полей
        if not name or not password or not age:
            flash('Пожалуйста, заполните обязательные поля!', 'error')
            return redirect(url_for('index'))
        
        # Выводим полученные данные
        print("=== ДАННЫЕ РЕГИСТРАЦИИ ===")
        print(f"Имя: {name}")
        print(f"Пароль: {password}")
        print(f"Возраст: {age}")
        print(f"Пол: {gender}")
        print(f"Увлечения: {', '.join(hobbies) if hobbies else 'Нет'}")
        print(f"Страна: {country}")
        print(f"Город: {city}")
        print(f"О себе: {about}")
        print(f"Об увлечениях: {hobbies_info}")
        print(f"Результат примера: {math_result}")
        
        flash('Регистрация успешно завершена!', 'success')
        return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)