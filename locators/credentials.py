class Credentials:
    def __init__(self):
        self.my_email = "test@example.com"
        self.my_password = "password123"
        self.name = "Test User"
        self.incorrect_pass = "123"

    def email(self):
        # Генерация уникального email для регистрации
        import random
        return f"test{random.randint(1000, 9999)}@example.com"

    def password(self):
        # Генерация уникального пароля для регистрации
        import random
        return f"password{random.randint(1000, 9999)}"


cred = Credentials()