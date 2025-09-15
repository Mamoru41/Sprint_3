from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Заголовок страницы входа
    LOGIN_HEADER = (By.XPATH, ".//h2[text()='Вход']")

    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")

    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, ".//a[text()='Зарегистрироваться']")

    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")

    # Индикатор успешного входа (редирект на главную)
    # Будем проверять элемент с главной страницы