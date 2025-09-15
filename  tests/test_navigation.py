import pytest
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage


class TestNavigation:
    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_navigate_to_personal_account(self, browser):
        """Тест перехода в личный кабинет"""
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        profile_page = ProfilePage(browser)

        # Логинимся и переходим в личный кабинет
        main_page.open_main_page()
        main_page.click_login_button()
        login_page.login("test_user@yandex.ru", "Password123")
        main_page.click_personal_account_button()

        assert profile_page.is_element_present(ProfilePageLocators.PROFILE_HEADER)
        browser.quit()

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_navigate_from_profile_to_constructor_via_button(self, browser):
        """Тест перехода из личного кабинета в конструктор через кнопку"""
        # ... аналогичная реализация
        browser.quit()

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_navigate_from_profile_to_constructor_via_logo(self, browser):
        """Тест перехода из личного кабинета в конструктор через логотип"""
        # ... аналогичная реализация
        browser.quit()

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_logout_from_account(self, browser):
        """Тест выхода из аккаунта"""
        profile_page = ProfilePage(browser)
        login_page = LoginPage(browser)

        # Логинимся и выходим
        # ... реализация входа
        profile_page.click_logout_button()

        assert login_page.is_element_present(LoginPageLocators.LOGIN_HEADER)
        browser.quit()