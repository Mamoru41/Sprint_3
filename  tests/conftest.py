# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--headless', action='store_true', help='Run tests in headless mode')


@pytest.fixture(scope='session')
def browser_options(request):
    """Фикстура для создания опций браузера"""
    browser_name = request.config.getoption('browser')
    headless = request.config.getoption('headless')

    if browser_name == 'chrome':
        options = Options()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
    else:
        raise ValueError(f'Unsupported browser: {browser_name}')

    return options, browser_name


@pytest.fixture(scope='session')
def driver(browser_options):
    """Фикстура для инициализации и закрытия драйвера"""
    options, browser_name = browser_options

    if browser_name == 'chrome':
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(options=options)

    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def browser(driver):
    """Фикстура для тестовых методов, обеспечивающая чистую сессию"""
    driver.delete_all_cookies()
    yield driver
