import random
import string

def generate_email():
    """Генерирует уникальный email по формату: имя_фамилия_номеркогорты_3цифры@домен"""
    random_num = random.randint(100, 999)  # 3 цифры
    return f"mamoru40_{random_num}@yandex.ru"

def generate_password(length=8):
    """Генерирует случайный пароль"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def generate_name():
    """Генерирует случайное имя"""
    names = ["Иван", "Петр", "Мария", "Анна", "Сергей", "Ольга", "Александр", "Елена"]
    surnames = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Попов", "Васильев"]
    return f"{random.choice(names)}_{random.choice(surnames)}"