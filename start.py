from flask import Flask, request, render_template
app = Flask (__name__)
users = {
   '1': {'name': 'Ivan',
       'age': 18,
       'sity': 'Moscow',
       'is_active': 1},
    '2': {'name': 'Boris',
        'age': 20,
        'sity': 'Krasnodar',
        'is_active': 1},
    '3': {'name': 'Inna',
        'age': 25,
        'sity': 'Yalta',
        'is_active': 1},
    '4': {'name': 'Oleg',
        'age': 42,
        'sity': 'Tula',
        'is_active': 1}
}
# Отображение маршрута для вывода главной страницы
@app.route('/')
def page():
    return render_template('page.html')

# Отображение маршрута для вывода таблицы пользователей
@app.route('/table')
def table():
    return render_template('table.html', context=users)

# Отображение маршрута для показа конкретного пользователя по номеру
@app.route('/user/<id>')
def user(id):
    if id not in users:
        return f'Пользователя под номером {id} не существует'
    else:
        return f"Здравствуйте, {users[id]['name']}, ваш номер {id}, ваш возраст - {users[id]['age']},\
        вы живёте в {users[id]['sity']}"
    
# Добавление нового пользователя    
@app.route('/add_user')
def add_user():
    # Получение данных о новом пользователе из запроса
    name = request.args.get('name')
    age = request.args.get('age')
    sity = request.args.get('sity')
    # Генерация уникального ID для нового пользователя
    new_id = str(int(max(users)) + 1)
    # Добавление нового пользователя в словарь
    users[new_id] = {
        'name': name,
        'age': age,
        'sity': sity}
    # Возвращение информации о добавленном пользователе в виде строки
    return f'name = {name}, age = {age}, sity = {sity}'

# Отображение маршрута для показа всех пользователей 
@app.route('/users_all')
def users_all():
    users_all = ''
    for i in range(1, len(users) + 1):
       i = str(i)
       users_all += f"Имя - {users[i]['name']}, возраст - {users[i]['age']}, город - {users[i]['sity']}; "
    return users_all

# Страницу contacts.html “прикрутил” к сайту
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')
# Страницу index.html “прикрутил” к сайту
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)