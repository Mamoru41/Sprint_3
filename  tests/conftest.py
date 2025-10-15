import pytest
from selenium import webdriver
from utils import generate_email, generate_password
from data import BASE_URL  # Импортируем напрямую BASE_URL

@pytest.fixture
def driver():
@@ -19,4 +20,4 @@ def random_password():

@pytest.fixture
def base_url():
    return BASE_URL  # Используем импортированную константу