import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import BASE_URL
from locators import RegistrationPageLocators
from helpers import generate_email, generate_password, generate_name
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration:
    def test_successful_registration_format_1(self, driver):
        """Тест проверяет успешную регистрацию с валидными данными."""
        driver.get(BASE_URL + "/register")

        WebDriverWait(driver, 10).until(EC.url_contains("/register"))
        assert "/register" in driver.current_url, "Не загрузилась страница регистрации"

        # Генерируем уникальные данные
        name = generate_name()
        email = generate_email()
        password = generate_password()

        # Заполняем форму
        name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)

        name_input.send_keys(name)
        email_input.send_keys(email)
        password_input.send_keys(password)

        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
        )
        register_button.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url, f"Ожидался переход на логин, но URL: {driver.current_url}"

        login_form = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_FORM)
        )
        assert login_form.is_displayed(), "Форма логина не отображается после регистрации"

    def test_successful_registration_format_2(self, driver):
        """Тест проверяет успешную регистрацию с другим форматом email."""
        driver.get(BASE_URL + "/register")

        WebDriverWait(driver, 10).until(EC.url_contains("/register"))
        assert "/register" in driver.current_url, "Не загрузилась страница регистрации"

        # Генерируем уникальные данные с другим форматом
        name = generate_name()
        email = generate_email()  # Используем стандартный генератор
        password = generate_password()

        # Заполняем форму
        name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)

        name_input.send_keys(name)
        email_input.send_keys(email)
        password_input.send_keys(password)

        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
        )
        register_button.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url, f"Ожидался переход на логин, но URL: {driver.current_url}"

        login_form = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.LOGIN_FORM)
        )
        assert login_form.is_displayed(), "Форма логина не отображается после регистрации"