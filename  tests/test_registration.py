import pytest
from generators.user_generator import generate_user_data
from locators.registration_page_locators import RegistrationPageLocators
from locators.main_page_locators import MainPageLocators
from pages.registration_page import RegistrationPage


class TestRegistration:
    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_successful_registration(self, browser):
        """Тест успешной регистрации с валидными данными"""
        user_data = generate_user_data()
        registration_page = RegistrationPage(browser)

        registration_page.open_registration_page()
        registration_page.register_user(user_data['name'], user_data['email'], user_data['password'])

        # Проверяем редирект на главную страницу после успешной регистрации
        assert registration_page.is_element_present(MainPageLocators.PLACE_ORDER_BUTTON)
        browser.quit()

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_registration_with_short_password_shows_error(self, browser):
        """Тест ошибки при регистрации с коротким паролем"""
        user_data = generate_user_data()
        registration_page = RegistrationPage(browser)

        registration_page.open_registration_page()
        registration_page.register_user(user_data['name'], user_data['email'], user_data['short_password'])

        # Проверяем отображение ошибки
        assert registration_page.is_element_present(RegistrationPageLocators.PASSWORD_ERROR)
        browser.quit()