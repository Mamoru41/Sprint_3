from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Заголовок страницы профиля
    PROFILE_HEADER = (By.XPATH, ".//h2[text()='Профиль']")

    # Поле ввода имени
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")

    # Поле ввода email
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Логин']/following-sibling::input")

    # Поле ввода пароля
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")

    # Кнопка "Выйти"
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

    # Кнопка "Сохранить" (для изменений профиля)
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")

    # Ссылка "История заказов"
    ORDER_HISTORY_LINK = (By.XPATH, ".//a[text()='История заказов']")

    # Ссылка "Профиль"
    PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")