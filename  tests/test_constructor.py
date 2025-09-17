import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestConstructor:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)
        self.main_page.open_main_page()
        yield
        # Закрытие браузера будет handled в фикстуре browser

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_navigate_to_buns_section(self, browser):
        """Тест перехода к разделу 'Булки'"""
        # Сначала переходим в другой раздел
        self.main_page.click_sauces_section()
        # Затем возвращаемся к булкам
        self.main_page.click_buns_section()

        assert self.main_page.is_section_active(MainPageLocators.BUNS_SECTION)

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_navigate_to_sauces_section(self, browser):
        """Тест перехода к разделу 'Соусы'"""
        self.main_page.click_sauces_section()

        assert self.main_page.is_section_active(MainPageLocators.SAUCES_SECTION)

    @pytest.mark.parametrize('browser', ['chrome'], indirect=True)
    def test_navigate_to_fillings_section(self, browser):
        """Тест перехода к разделу 'Начинки'"""
        self.main_page.click_fillings_section()

        assert self.main_page.is_section_active(MainPageLocators.FILLINGS_SECTION)
