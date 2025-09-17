import random
import string


def generate_user_data():
    """Генерирует данные для регистрации пользователя"""
    name = f"TestUser{random.randint(1000, 9999)}"
    email = f"test{random.randint(1000, 9999)}@example.com"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    short_password = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

    return {
        'name': name,
        'email': email,
        'password': password,
        'short_password': short_password
    }