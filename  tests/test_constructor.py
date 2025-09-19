import pytest
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestConstructor:
    """Тесты конструктора бургеров"""

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        """Фикстура подготовки для каждого теста"""
        self.main_page = MainPage(browser)
        self.main_page.open_main_page()
        return  # Используем return вместо yield, если нет cleanup кода

    def test_navigate_to_buns_section(self):
        """Тест перехода к разделу 'Булки'"""
        # Сначала переходим в другой раздел
        self.main_page.click_sauces_section()
        # Затем возвращаемся к булкам
        self.main_page.click_buns_section()

        assert self.main_page.is_section_active(MainPageLocators.BUNS_SECTION)

    def test_navigate_to_sauces_section(self):
        """Тест перехода к разделу 'Соусы'"""
        self.main_page.click_sauces_section()

        assert self.main_page.is_section_active(MainPageLocators.SAUCES_SECTION)

    def test_navigate_to_fillings_section(self):
        """Тест перехода к разделу 'Начинки'"""
        self.main_page.click_fillings_section()

        assert self.main_page.is_section_active(MainPageLocators.FILLINGS_SECTION)