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


class TestLoginFunctionality:
    """Тесты функциональности входа в аккаунт с разных страниц и кнопок"""

    def test_account_entrance(self, open_main_page):
        """Тест входа по кнопке 'Войти в аккаунт' на главной странице"""
        driver = open_main_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.enter_button))
        driver.find_element(*loc.enter_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.login_button))
        driver.find_element(*loc.login_email_input).send_keys(cred.my_email)
        driver.find_element(*loc.login_password_input).send_keys(cred.my_password)
        driver.find_element(*loc.login_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))

    def test_lk_entrance(self, open_main_page):
        """Тест входа по кнопке 'Личный кабинет' на главной странице"""
        driver = open_main_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.enter_button))
        driver.find_element(*loc.lk_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.login_button))
        driver.find_element(*loc.login_email_input).send_keys(cred.my_email)
        driver.find_element(*loc.login_password_input).send_keys(cred.my_password)
        driver.find_element(*loc.login_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))

    def test_entrance_from_register_page(self, open_registr_page):
        """Тест входа по кнопке 'Войти' на странице регистрации"""
        driver = open_registr_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.registration_confirm_button))
        driver.find_element(*loc.login_from_register_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.login_button))
        driver.find_element(*loc.login_email_input).send_keys(cred.my_email)
        driver.find_element(*loc.login_password_input).send_keys(cred.my_password)
        driver.find_element(*loc.login_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))

    def test_entrance_from_forgot_pass(self, open_forgot_pass_page):
        """Тест входа по кнопке 'Войти' на странице восстановления пароля"""
        driver = open_forgot_pass_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.recover_button))
        driver.find_element(*loc.login_from_register_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.login_button))
        driver.find_element(*loc.login_email_input).send_keys(cred.my_email)
        driver.find_element(*loc.login_password_input).send_keys(cred.my_password)
        driver.find_element(*loc.login_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))