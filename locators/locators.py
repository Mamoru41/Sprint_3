from selenium.webdriver.common.by import By


class Locators:
    enter_button = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # Кнопка "Войти в аккаунт" на главной странице
    lk_button = (By.XPATH, '//*[@id="root"]/div/header/nav/a')  # Кнопка "Личный Кабинет" на главной странице
    logo_button = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a')  # Кнопка с логотипом на главной странице
    constructor_button = (By.XPATH,
                          '//*[@id="root"]/div/header/nav/ul/li[1]/a')  # Кнопка "Конструктор" на главной странице
    order_button = (By.XPATH, '//button[text()="Оформить заказ"]')  # Кнопка "Оформить заказ" на главной странице
    recover_button = (By.XPATH,
                      '//button[text()="Восстановить"]')  # Кнопка "Восстановить" на странице восстановления пароля
    save_button = (By.XPATH, '//button[text()="Сохранить"]')  # Кнопка "Сохранить" с личном кабинете

    login_from_register_button = (By.XPATH,
                                  '//*[@id="root"]/div/main/div/div/p/a')  # Кнопка входа на странице регистрации и в форме восстановления пароля
    registration_name_input = (By.XPATH,
                               '//label[text()="Имя"]/parent::*/input')  # Поле ввода имени на странице регистрации
    registration_password_input = (By.XPATH,
                                   '//label[text()="Пароль"]/parent::*/input')  # Поле ввода пароля на странице регистрации
    registration_confirm_button = (By.XPATH,
                                   '//button[text()="Зарегистрироваться"]')  # Кнопка "Зарегистрироваться" на странице регистрации
    registration_email_input = (By.XPATH,
                                '//label[text()="Email"]/parent::*/input')  # Поле ввода email на странице регистрации
    error_incorrect_password = (By.XPATH,
                                '//*[contains(text(),"Некорректный")]')  # Надпись об ошибке некорректного пароля
    error_user_exists = (By.XPATH,
                         '//*[contains(text(),"пользователь уже существует")]')  # Надпись об ошибке "Пользователь уже существует"

    login_email_input = (By.XPATH, '//label[text()="Email"]/parent::*/input')  # Поле ввода email на странице входа
    login_password_input = (By.XPATH, '//label[text()="Пароль"]/parent::*/input')  # Поле ввода пароля на странице входа
    login_button = (By.XPATH, '//button[text()="Войти"]')  # Кнопка "Войти" на странице входа
    exit_button = (By.XPATH, '//button[text()="Выход"]')  # Кнопка "Выйти" в личном кабинете

    bulki_tab = (By.XPATH, '//span[text()="Булки"]/parent::*')  # Кнопка раздела "Булки"
    sousy_tab = (By.XPATH, '//span[text()="Соусы"]/parent::*')  # Кнопка раздела "Соусы"
    nachinki_tab = (By.XPATH, '//span[text()="Начинки"]/parent::*')  # Кнопка раздела "Начинки"
    active_tab = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]')  # Активная секция в конструкторе