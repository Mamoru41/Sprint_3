import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import BASE_URL
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators
from helpers import generate_email, generate_password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestLogin:
    def test_login_via_personal_account(self, driver, random_email, random_password):
        """Тест проверяет вход через кнопку 'Личный кабинет'."""
        driver.get(BASE_URL)

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "/"))

        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url, "Не произошел переход на страницу логина"

        # Выполняем вход
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)

        email_input.send_keys(random_email)
        password_input.send_keys(random_password)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        )
        login_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/", "Не произошел переход на главную страницу после входа"

        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"

    def test_login_via_register_form(self, driver):
        """Тест проверяет переход на страницу логина со страницы регистрации."""
        driver.get(BASE_URL + "/register")

        WebDriverWait(driver, 10).until(EC.url_contains("/register"))
        assert "/register" in driver.current_url, "Не загрузилась страница регистрации"

        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        )
        login_link.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url, "Не произошел переход на страницу логина"

        login_form = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM)
        )
        assert login_form.is_displayed(), "Форма логина не отображается"

    def test_login_via_forgot_password(self, driver):
        """Тест проверяет переход на страницу логина со страницы восстановления пароля."""
        driver.get(BASE_URL + "/forgot-password")

        WebDriverWait(driver, 10).until(EC.url_contains("/forgot-password"))
        assert "/forgot-password" in driver.current_url, "Не загрузилась страница восстановления пароля"

        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)
        )
        login_link.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url, "Не произошел переход на страницу логина"

        login_form = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM)
        )
        assert login_form.is_displayed(), "Форма логина не отображается"

    def test_login_from_main_page(self, driver):
        """Тест проверяет вход через кнопку 'Войти в аккаунт' на главной странице."""
        driver.get(BASE_URL)

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/", "Не загрузилась главная страница"

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_ACCOUNT_BUTTON)
        )
        login_button.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url, "Не произошел переход на страницу логина"

        login_form = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM)
        )
        assert login_form.is_displayed(), "Форма логина не отображается"

