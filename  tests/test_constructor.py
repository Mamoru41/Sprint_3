import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestConstructor:
    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_navigate_to_buns_section(self, browser):
        """Тест перехода к разделу 'Булки'"""
        main_page = MainPage(browser)

        main_page.open_main_page()
        main_page.click_sauces_section()  # Сначала переходим в другой раздел
        main_page.click_buns_section()  # Затем возвращаемся к булкам

        assert main_page.is_section_active(MainPageLocators.BUNS_SECTION)
        browser.quit()

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_navigate_to_sauces_section(self, browser):
        """Тест перехода к разделу 'Соусы'"""
        main_page = MainPage(browser)

        main_page.open_main_page()
        main_page.click_sauces_section()

        assert main_page.is_section_active(MainPageLocators.SAUCES_SECTION)
        browser.quit()

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_navigate_to_fillings_section(self, browser):
        """Тест перехода к разделу 'Начинки'"""
        main_page = MainPage(browser)

        main_page.open_main_page()
        main_page.click_fillings_section()

        assert main_page.is_section_active(MainPageLocators.FILLINGS_SECTION)
        browser.quit()
    }
