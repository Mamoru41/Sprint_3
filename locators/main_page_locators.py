from selenium.webdriver.common.by import By


class MainPageLocators:
    # Заголовок главной страницы
    MAIN_HEADER = (By.XPATH, ".//h1[text()='Соберите бургер']")

    # Кнопка "Войти в аккаунт" на главной
    LOGIN_BUTTON_ON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")

    # Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")

    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")

    # Логотип Stellar Burgers
    STELLAR_BURGER_LOGO = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]")

    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']/..")
    SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']/..")
    FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']/..")

    # Активный раздел конструктора (для проверки)
    ACTIVE_SECTION = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]")

    # Кнопка "Оформить заказ" (индикатор успешного входа)
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")