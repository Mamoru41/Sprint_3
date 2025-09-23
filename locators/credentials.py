from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    # Заголовок страницы восстановления пароля
    FORGOT_PASSWORD_HEADER = (By.XPATH, ".//h2[text()='Восстановление пароля']")

    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")

    # Кнопка "Восстановить"
    RESTORE_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")

    # Ссылка "Войти" (вспомнил пароль)
    LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")