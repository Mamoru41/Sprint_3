import random

class cred:
    my_email = "lena112@yandex.ru" # предзарегистрированный email для проверки входа
    my_password = "qwerty123" # предзарегистрированный пароль для проверки входа

    name='Lena' # Имя для проверки формы регистрации
    incorrect_pass='123' # Короткий пароль для проверки некорректного пароля
    def email():   # Генерация email для регистрации по правилу Фамилия_Имя_когорта_<3 случайных цифры>@yandex.ru
        return f"elena_mirionkova_28{random.randint(100, 999)}@yandex.ru"
    def password(): # Генерация пароля для регистрации: от 6 до 8 произвольных цифр
        return f"{random.randint(100000, 99999999)}"