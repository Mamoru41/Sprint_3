import pytest
import os
import sys

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(directory))
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import *
from locators import *
from credentials import *


# Фикстура определения веб драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Фикстура логина на сайте и открытия на главной странице
@pytest.fixture
def open_main_page_logged_in(driver):
    driver.get(login_page)
    driver.find_element(*loc.login_email_input).send_keys(cred.my_email)
    driver.find_element(*loc.login_password_input).send_keys(cred.my_password)
    driver.find_element(*loc.login_button).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))
    return driver


class TestConstructorTabs:
    """Тесты перехода по табам в конструкторе на главной странице"""

    def test_bulki_tab(self, open_main_page_logged_in):
        """Тест перехода по табу 'Булки'"""
        driver = open_main_page_logged_in
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))
        driver.find_element(*loc.sousy_tab).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.active_tab))
        driver.find_element(*loc.bulki_tab).click()
        tab_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.active_tab))
        assert tab_element.is_displayed()
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(loc.active_tab, 'Булки'))

    def test_sous_tab(self, open_main_page_logged_in):
        """Тест перехода по табу 'Соусы'"""
        driver = open_main_page_logged_in
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))
        driver.find_element(*loc.sousy_tab).click()
        tab_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.active_tab))
        assert tab_element.is_displayed()
        assert 'Соусы' in tab_element.text

    def test_nach_tab(self, open_main_page_logged_in):
        """Тест перехода по табу 'Начинки'"""
        driver = open_main_page_logged_in
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))
        driver.find_element(*loc.nachinki_tab).click()
        tab_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.active_tab))
        assert tab_element.is_displayed()
        assert 'Начинки' in tab_element.text