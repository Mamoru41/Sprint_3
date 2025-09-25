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
    driver=webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Фикстура открытия главной страницы сайта
@pytest.fixture
def open_main_page(driver):
    driver.get(main_page)
    return driver

# Фикстура логина на сайте и открытия на главной странице
@pytest.fixture
def open_main_page_logged_in(driver):
    driver.get(login_page)
    driver.find_element(*loc.login_email_input).send_keys(cred.my_email)
    driver.find_element(*loc.login_password_input).send_keys(cred.my_password)
    driver.find_element(*loc.login_button).click()
    return driver

# Фикстура открытия страницы регистрации
@pytest.fixture
def open_registr_page(driver):
    driver.get(register_page)
    return driver

# Фикстура открытия страницы восстановления пароля
@pytest.fixture
def open_forgot_pass_page(driver):
    driver.get(forgot_pass)
    return driver