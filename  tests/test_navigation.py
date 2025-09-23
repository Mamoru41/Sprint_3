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

# Тест на переход по кнопке "Личный кабинет"
class TestNavigateToLK:
    def test_navigate_to_lk(self, open_main_page_logged_in):
        driver=open_main_page_logged_in
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))
        driver.find_element(*loc.lk_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.save_button))

# Тест на переход из личного кабинета в "Конструктор"
class TestNavigateToKonstr:
    def test_navigate_to_constr(self, open_main_page_logged_in):
        driver=open_main_page_logged_in
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))
        driver.find_element(*loc.lk_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.save_button))
        driver.find_element(*loc.logo_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))

# Тест на выход из аккаунта
class TestExitAccount:
    def test_exit_account(self, open_main_page_logged_in):
        driver=open_main_page_logged_in
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))
        driver.find_element(*loc.lk_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.save_button))
        driver.find_element(*loc.exit_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.login_button))