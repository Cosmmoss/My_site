# Лекция от 17.04.2024. Тема 3. Flask-WTF. Работа с формами.

# Импорт необходимых модулей из библиотек Flask и Flask-WTF
from flask import Flask, render_template  # Импортируем библиотеку Flask, render_template
from flask_wtf import FlaskForm  # Импортируем библиотеку WTF
from wtforms import StringField, IntegerField, SubmitField, TelField, RadioField, SelectField  # Импортируем типы полей
# Импорт валидаторов из модуля wtforms.validators
from wtforms.validators import InputRequired, Email

app = Flask (__name__)

class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])  # Поле для ввода почты с валидацией
    phone = TelField(validators=[InputRequired()])  # Поле для ввода телефона с валидацией
    name = StringField(validators=[InputRequired()])  # Поле для ввода имени с валидацией
    address = StringField()  # Поле для ввода адреса
    index = IntegerField()  # Поле для ввода индекса
    comment = StringField()  # Поле для ввода комментария
    sex = RadioField(label='Пол', choices = [('Мужской', 'Муж'), ('Женский', 'Жен')])  # Поле ввода пола
    education = SelectField('Образование', choices = [('Высшее', 'Высш.'), ('Среднее', 'Ср.')])  # Поле ввода образования
    submit = SubmitField(label = ('submit'))  # Кнопка для отправки формы

# Обработчик маршрута для главной страницы
@app.route('/')
def index():
    return 'Главная страница'

# Обработчик маршрута для страницы регистрации
@app.route('/registration', methods = ['GET', 'POST'])
def registration():
# Создаем экземпляр формы для регистрации
    form = RegistrationForm()
    # Проверяем, была ли форма отправлена и прошла ли валидацию
    if form.validate_on_submit():
        # Если форма прошла валидацию, получаем данные из полей формы
        email, phone, name, address, sex = form.email.data, form.phone.data, form.name.data, form.address.data, form.sex.data
        # Выводим данные формы в консоль для отладки
        print(email, phone, name, address, sex)
        # Возвращаем приветственное сообщение с использованием имени пользователя
        return f'Hello {name} welcome to our site!'
    
    # Если форма не была отправлена или не прошла валидацию,
    # отображаем HTML-шаблон с формой регистрации,
    # передавая объект формы для отображения введенных пользователем данных
    return render_template('reg_form_wtf.html', form=form)

if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False  # Отключаем проверку CSRF для WTForms
    app.run(debug=True)  # Запускаем приложение в режиме отладки
