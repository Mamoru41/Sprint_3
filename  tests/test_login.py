import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.forgot_password_page import ForgotPasswordPage


class TestLogin:
    """Тесты авторизации пользователя"""

    @pytest.fixture(autouse=True)
    def setup(self, browser, test_user_credentials):
        """Фикстура подготовки для каждого теста"""
        self.main_page = MainPage(browser)
        self.login_page = LoginPage(browser)
        self.registration_page = RegistrationPage(browser)
        self.forgot_password_page = ForgotPasswordPage(browser)
        self.email = test_user_credentials["email"]
        self.password = test_user_credentials["password"]
        yield

    def test_login_from_main_page_button(self):
        """Тест входа через кнопку 'Войти в аккаунт' на главной"""
        self.main_page.open_main_page()
        self.main_page.click_login_button()
        self.login_page.login(self.email, self.password)

        assert self.main_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)

    def test_login_from_personal_account_button(self):
        """Тест входа через кнопку 'Личный кабинет'"""
        self.main_page.open_main_page()
        self.main_page.click_personal_account_button()
        self.login_page.login(self.email, self.password)

        assert self.main_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)

    def test_login_from_registration_form(self):
        """Тест входа через кнопку в форме регистрации"""
        self.registration_page.open_registration_page()
        self.registration_page.click_login_link()
        self.login_page.login(self.email, self.password)

        assert self.main_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)

    def test_login_from_forgot_password_form(self):
        """Тест входа через кнопку в форме восстановления пароля"""
        self.forgot_password_page.open_forgot_password_page()
        self.forgot_password_page.click_login_link()
        self.login_page.login(self.email, self.password)

        assert self.main_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)