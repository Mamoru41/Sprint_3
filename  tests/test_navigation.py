import pytest
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.login_page_locators import LoginPageLocators
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage


class TestNavigation:
    """Тесты навигации по приложению"""

    @pytest.fixture(autouse=True)
    def setup(self, browser, test_user_credentials):
        """Фикстура подготовки для каждого теста"""
        self.main_page = MainPage(browser)
        self.login_page = LoginPage(browser)
        self.profile_page = ProfilePage(browser)
        self.email = test_user_credentials["email"]
        self.password = test_user_credentials["password"]

        # Логинимся перед каждым тестом (кроме logout)
        self.main_page.open_main_page()
        self.main_page.click_login_button()
        self.login_page.login(self.email, self.password)
        yield

    def test_navigate_to_personal_account(self):
        """Тест перехода в личный кабинет"""
        self.main_page.click_personal_account_button()
        assert self.profile_page.is_profile_page_displayed()

    def test_navigate_from_profile_to_constructor_via_button(self):
        """Тест перехода из личного кабинета в конструктор через кнопку"""
        # Переходим в личный кабинет
        self.main_page.click_personal_account_button()
        assert self.profile_page.is_profile_page_displayed()

        # Возвращаемся в конструктор через кнопку
        self.profile_page.click_constructor_button()
        assert self.main_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)

    def test_navigate_from_profile_to_constructor_via_logo(self):
        """Тест перехода из личного кабинета в конструктор через логотип"""
        # Переходим в личный кабинет
        self.main_page.click_personal_account_button()
        assert self.profile_page.is_profile_page_displayed()

        # Возвращаемся в конструктор через логотип
        self.profile_page.click_stellar_burger_logo()
        assert self.main_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)

    def test_logout_from_account(self):
        """Тест выхода из аккаунта"""
        # Переходим в личный кабинет
        self.main_page.click_personal_account_button()
        assert self.profile_page.is_profile_page_displayed()

        # Выходим из аккаунта
        self.profile_page.click_logout_button()
        assert self.login_page.is_element_present(LoginPageLocators.LOGIN_HEADER)