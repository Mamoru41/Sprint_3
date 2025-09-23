imimport pytest
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

# Тест на успешную регистрацию
class TestSuccessfullRegistration:
    def test_successfull_registration(self, open_registr_page):
        driver=open_registr_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.registration_confirm_button))
        driver.find_element(*loc.registration_name_input).send_keys(cred.name)
        driver.find_element(*loc.registration_email_input).send_keys(cred.email())
        driver.find_element(*loc.registration_password_input).send_keys(cred.password())
        driver.find_element(*loc.registration_confirm_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.login_button))
        assert driver.current_url == login_page

# Тест на попытку регистрации с пустым именем
class TestEmptiNameRegistration:
    def test_empti_nameR_rgistration(self, open_registr_page):
        driver=open_registr_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.registration_confirm_button))
        driver.find_element(*loc.registration_email_input).send_keys(cred.email())
        driver.find_element(*loc.registration_password_input).send_keys(cred.password())
        driver.find_element(*loc.registration_confirm_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.registration_confirm_button))
        assert driver.current_url == register_page

# Тест на попытку регистрации с коротким паролем менее 6 символов
class TestWrongPasswordRegistration:
    def test_wrong_password_registration(self, open_registr_page):
        driver=open_registr_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.registration_confirm_button))
        driver.find_element(*loc.registration_name_input).send_keys(cred.name)
        driver.find_element(*loc.registration_email_input).send_keys(cred.email())
        driver.find_element(*loc.registration_password_input).send_keys(cred.incorrect_pass)
        driver.find_element(*loc.registration_confirm_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc. error_incorrect_password))

# Тест на попытку регистрации с уже зарегистрированным email
class TestExistigUserRegistration:
    def test_existig_user_registration(self, open_registr_page):
        driver=open_registr_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.registration_confirm_button))
        driver.find_element(*loc.registration_name_input).send_keys(cred.name)
        driver.find_element(*loc.registration_email_input).send_keys(cred.my_email)
        driver.find_element(*loc.registration_password_input).send_keys(cred.my_password)
        driver.find_element(*loc.registration_confirm_button).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.error_user_exists))