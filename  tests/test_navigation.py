import pytest
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from test_data import TestData


class TestNavigation:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)
        self.login_page = LoginPage(browser)
        self.profile_page = ProfilePage(browser)
        # Логинимся перед каждым тестом (кроме logout)
        self.main_page.open_main_page()
        self.main_page.click_login_button()
        self.login_page.login(TestData.TEST_EMAIL, TestData.TEST_PASSWORD)
        yield
        # Закрытие браузера будет handled в фикстуре browser

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_navigate_to_personal_account(self, browser):
        """Тест перехода в личный кабинет"""
        self.main_page.click_personal_account_button()
        assert self.profile_page.is_profile_page_displayed()

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_navigate_from_profile_to_constructor_via_button(self, browser):
        """Тест перехода из личного кабинета в конструктор через кнопку"""
        # Переходим в личный кабинет
        self.main_page.click_personal_account_button()
        assert self.profile_page.is_profile_page_displayed()

        # Возвращаемся в конструктор через кнопку
        self.profile_page.click_constructor_button()
        assert self.main_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_navigate_from_profile_to_constructor_via_logo(self, browser):
        """Тест перехода из личного кабинета в конструктор через логотип"""
        # Переходим в личный кабинет
        self.main_page.click_personal_account_button()
        assert self.profile_page.is_profile_page_displayed()

        # Возвращаемся в конструктор через логотип
        self.profile_page.click_stellar_burger_logo()
        assert self.main_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_logout_from_account(self, browser):
        """Тест выхода из аккаунта"""
        # Переходим в личный кабинет
        self.main_page.click_personal_account_button()
        assert self.profile_page.is_profile_page_displayed()

        # Выходим из аккаунта
        self.profile_page.click_logout_button()
        assert self.login_page.is_element_present(LoginPageLocators.LOGIN_HEADER)