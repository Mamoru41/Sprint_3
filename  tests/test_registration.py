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


class TestRegistration:
    """Тесты функциональности регистрации пользователя"""

    def test_successfull_registration(self, open_registr_page):
        """Тест успешной регистрации"""
        driver = open_registr_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.registration_confirm_button))
        driver.find_element(*loc.registration_name_input).send_keys(cred.name)
        driver.find_element(*loc.registration_email_input).send_keys(cred.email())
        driver.find_element(*loc.registration_password_input).send_keys(cred.password())
        driver.find_element(*loc.registration_confirm_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.login_button))
        assert driver.current_url == login_page

    def test_empty_name_registration(self, open_registr_page):
        """Тест попытки регистрации с пустым именем"""
        driver = open_registr_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.registration_confirm_button))
        driver.find_element(*loc.registration_email_input).send_keys(cred.email())
        driver.find_element(*loc.registration_password_input).send_keys(cred.password())
        driver.find_element(*loc.registration_confirm_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.registration_confirm_button))
        assert driver.current_url == register_page

    def test_wrong_password_registration(self, open_registr_page):
        """Тест попытки регистрации с коротким паролем менее 6 символов"""
        driver = open_registr_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.registration_confirm_button))
        driver.find_element(*loc.registration_name_input).send_keys(cred.name)
        driver.find_element(*loc.registration_email_input).send_keys(cred.email())
        driver.find_element(*loc.registration_password_input).send_keys(cred.incorrect_pass)
        driver.find_element(*loc.registration_confirm_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.error_incorrect_password))

    def test_existing_user_registration(self, open_registr_page):
        """Тест попытки регистрации с уже зарегистрированным email"""
        driver = open_registr_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.registration_confirm_button))
        driver.find_element(*loc.registration_name_input).send_keys(cred.name)
        driver.find_element(*loc.registration_email_input).send_keys(cred.my_email)
        driver.find_element(*loc.registration_password_input).send_keys(cred.my_password)
        driver.find_element(*loc.registration_confirm_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.error_user_exists))