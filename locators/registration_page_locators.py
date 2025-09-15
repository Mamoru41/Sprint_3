from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    # Заголовок страницы регистрации
    REGISTRATION_HEADER = (By.XPATH, ".//h2[text()='Регистрация']")

    # Поле ввода имени
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")

    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")

    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")

    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")

    # Ссылка "Войти" (уже есть аккаунт)
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")

    # Сообщение об ошибке для некорректного пароля
    PASSWORD_ERROR = (By.XPATH, ".//p[contains(@class, 'input__error')]")

    # Индикатор успешной регистрации (редирект на главную)
    # Будем проверять элемент с главной страницы