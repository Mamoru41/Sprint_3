import pytest
from generators.user_generator import generate_user_data
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.registration_page_locators import RegistrationPageLocators
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.forgot_password_page import ForgotPasswordPage


class TestLogin:
    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_login_from_main_page_button(self, browser):
        """Тест входа через кнопку 'Войти в аккаунт' на главной"""
        main_page = MainPage(browser)
        login_page = LoginPage(browser)

        main_page.open_main_page()
        main_page.click_login_button()
        login_page.login("test_user@yandex.ru", "Password123")

        assert main_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)
        browser.quit()

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_login_from_personal_account_button(self, browser):
        """Тест входа через кнопку 'Личный кабинет'"""
        main_page = MainPage(browser)
        login_page = LoginPage(browser)

        main_page.open_main_page()
        main_page.click_personal_account_button()
        login_page.login("test_user@yandex.ru", "Password123")

        assert main_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)
        browser.quit()

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_login_from_registration_form(self, browser):
        """Тест входа через кнопку в форме регистрации"""
        registration_page = RegistrationPage(browser)
        login_page = LoginPage(browser)

        registration_page.open_registration_page()
        registration_page.click_login_link()
        login_page.login("test_user@yandex.ru", "Password123")

        assert login_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)
        browser.quit()

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_login_from_forgot_password_form(self, browser):
        """Тест входа через кнопку в форме восстановления пароля"""
        forgot_password_page = ForgotPasswordPage(browser)
        login_page = LoginPage(browser)

        forgot_password_page.open_forgot_password_page()
        forgot_password_page.click_login_link()
        login_page.login("test_user@yandex.ru", "Password123")

        assert login_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)
        browser.quit()