import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--headless', action='store_true', help='Run tests in headless mode')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser')
    headless = request.config.getoption('headless')

    if browser_name == 'chrome':
        options = Options()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f'Unsupported browser: {browser_name}')

    driver.implicitly_wait(10)
    yield driver
    driver.quit()