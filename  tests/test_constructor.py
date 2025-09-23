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

# Тест на переход по кнопке "Булки" в конструкторе на гравной странице
class TestBulkiTab:
    def test_bulki_tab(self, open_main_page_logged_in):
        driver=open_main_page_logged_in
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))
        driver.find_element(*loc.sousy_tab).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.active_tab))
        driver.find_element(*loc.bulki_tab).click()
        tab_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.active_tab))
        assert tab_element.is_displayed()
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(loc.active_tab,'Булки'))

# Тест на переход по кнопке "Соусы" в конструкторе на гравной странице
class TestSousTab:
    def test_sous_tab(self, open_main_page_logged_in):
        driver=open_main_page_logged_in
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))
        driver.find_element(*loc.sousy_tab).click()
        tab_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.active_tab))
        assert tab_element.is_displayed()
        assert 'Соусы' in tab_element.text

# Тест на переход по кнопке "Начинки" в конструкторе на гравной странице
class TestNachTab:
    def test_nach_tab(self, open_main_page_logged_in):
        driver=open_main_page_logged_in
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.order_button))
        driver.find_element(*loc.nachinki_tab).click()
        tab_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc.active_tab))
        assert tab_element.is_displayed()
        assert 'Начинки' in tab_element.text