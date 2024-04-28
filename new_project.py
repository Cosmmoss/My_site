from flask import Flask, render_template  # Импортируем библиотеку Flask, render_template
from flask_wtf import FlaskForm  # Импортируем библиотеку WTF
from wtforms import StringField, IntegerField, SubmitField, TelField, RadioField, SelectField  # Импортируем типы полей
# Импорт валидаторов из модуля wtforms.validators
from wtforms.validators import InputRequired, Email

# Создаем экземпляр Flask с названием приложения
app = Flask (__name__)

# Словарь с данными о пользователях
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

# Определение класса формы регистрации
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