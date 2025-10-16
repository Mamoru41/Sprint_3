import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import BASE_URL
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators
from helpers import generate_email, generate_password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestNavigation:
    def test_go_to_profile(self, driver, random_email, random_password):
        """Тест проверяет переход в личный кабинет после авторизации."""
        driver.get(BASE_URL + "/login")

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

        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        profile_button.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url, "Не произошел переход в личный кабинет"

        profile_form = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_FORM)
        )
        assert profile_form.is_displayed(), "Форма профиля не отображается"

    def test_logout_from_profile(self, driver, random_email, random_password):
        """Тест проверяет выход из аккаунта через кнопку 'Выйти'."""
        driver.get(BASE_URL + "/login")

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

        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        profile_button.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url, "Не произошел переход в личный кабинет"

        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url, "Не произошел выход из аккаунта"

        login_form = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM)
        )
        assert login_form.is_displayed(), "Форма логина не отображается после выхода"

    def test_return_to_constructor_from_profile(self, driver, random_email, random_password):
        """Тест проверяет переход из ЛК в конструктор через кнопку 'Конструктор'."""
        driver.get(BASE_URL + "/login")

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

        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        profile_button.click()

        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url, "Не произошел переход в личный кабинет"

        constructor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/", "Не произошел возврат на главную страницу"

        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed(), "Кнопка оформления заказа не отображается на главной странице"