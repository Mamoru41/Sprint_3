import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data import TEST_EMAIL, TEST_PASSWORD, BASE_URL
from locators import MainPageLocators, LoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest


class TestBurgerConstructor:
    def test_burger_construction_and_order(self, driver):
        """Тест проверяет полный цикл: сборка бургера через перетаскивание и оформление заказа.

        Шаги:
        1. Авторизоваться в системе
        2. Перетащить ингредиент в конструктор
        3. Нажать кнопку 'Оформить заказ'
        4. Проверить появление модального окна с подтверждением заказа

        Ожидаемый результат:
        - Появление модального окна с текстом о начале приготовления заказа
        """
        # Логинимся
        driver.get(f"{BASE_URL}/login")

        # Ожидаем появление полей ввода
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME, "input"))