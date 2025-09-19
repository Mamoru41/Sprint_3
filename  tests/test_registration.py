import pytest
from generators.user_generator import generate_user_data
from locators.registration_page_locators import RegistrationPageLocators
from locators.main_page_locators import MainPageLocators
from pages.registration_page import RegistrationPage


class TestRegistration:
    """Тесты регистрации пользователя"""

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        """Фикстура подготовки для каждого теста"""
        self.registration_page = RegistrationPage(browser)
        yield

    def test_successful_registration(self):
        """Тест успешной регистрации с валидными данными"""
        user_data = generate_user_data()

        self.registration_page.open_registration_page()
        self.registration_page.register_user(
            user_data['name'],
            user_data['email'],
            user_data['password']
        )

        # Проверяем редирект на главную страницу после успешной регистрации
        assert self.registration_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)

    def test_registration_with_short_password_shows_error(self):
        """Тест ошибки при регистрации с коротким паролем"""
        user_data = generate_user_data()

        self.registration_page.open_registration_page()
        self.registration_page.register_user(
            user_data['name'],
            user_data['email'],
            user_data['short_password']
        )

        # Проверяем отображение ошибки
        assert self.registration_page.is_element_present(RegistrationPageLocators.PASSWORD_ERROR)