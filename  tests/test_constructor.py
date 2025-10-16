import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import BASE_URL
from locators import MainPageLocators, LoginPageLocators
from helpers import generate_email, generate_password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest


class TestBurgerConstructor:
    def test_burger_construction_and_order(self, driver, random_email, random_password):
        """Тест проверяет полный цикл: сборка бургера через перетаскивание и оформление заказа."""
        # Логинимся
        driver.get(f"{BASE_URL}/login")

        # Заполняем форму входа
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

        email_input.send_keys(random_email)
        password_input.send_keys(random_password)
        login_button.click()

        # Ожидаем загрузку главной страницы
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_SECTION)
        )

        # Перетаскиваем ингредиент в конструктор
        ingredient = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENT_ITEM)
        )
        constructor_area = driver.find_element(*MainPageLocators.CONSTRUCTOR_AREA)

        ActionChains(driver).drag_and_drop(ingredient, constructor_area).perform()

        # Проверяем, что ингредиент добавлен в конструктор
        added_ingredient = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ADDED_INGREDIENT)
        )
        assert added_ingredient.is_displayed(), "Ингредиент не был добавлен в конструктор"

        # Нажимаем кнопку "Оформить заказ"
        order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
        )
        order_button.click()

        # Проверяем появление модального окна с подтверждением заказа
        order_modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL)
        )
        assert order_modal.is_displayed(), "Модальное окно заказа не появилось"

        # Проверяем, что в модальном окне есть текст о начале приготовления
        order_text = driver.find_element(*MainPageLocators.ORDER_SUCCESS_TEXT)
        assert "идентификатор заказа" in order_text.text.lower(), "Текст подтверждения заказа не найден"